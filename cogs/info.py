'''

Actual Cog from ami, selfbot.


'''


import discord
from discord.ext import commands
from urllib.parse import urlparse
from ext import embedtobox
import datetime
import asyncio
import psutil
import random
import os
import io
import json


class Information:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member : discord.Member=None):
        '''Returns someone's avatar url'''
        if ctx.author.guild_permissions.manage_messages == True:
            await ctx.message.delete()
        mem = member or ctx.author
        avatar = mem.avatar_url_as(format = None, static_format = 'png')
        if ctx.author.guild_permissions.embed_links == True:
            color = await ctx.get_dominant_color(avatar)
            em = discord.Embed(url = avatar, color = color)
            em.set_author(name = str(mem), icon_url = avatar)
            em.set_image(url = avatar)
            await ctx.send(embed = em)
        else:
            await ctx.send(avatar)


    @commands.command(aliases=['ui'], no_pm=True)
    @commands.guild_only()
    async def user(self, ctx, *, member : discord.Member=None):
        '''Getting The user Information'''
        server = ctx.guild
        user = member or ctx.message.author
        avi = user.avatar_url
        roles = sorted(user.roles, key=lambda c: c.position)

        for role in roles:
            if str(role.color) != "#000000":
                color = role.color
        if 'color' not in locals():
            color = 0

        rolenames = ', '.join([r.name for r in roles if r.name != "@everyone"]) or 'None'
        time = ctx.message.created_at
        passed = (ctx.message.created_at - user.created_at).days
        created_at = "{}.  **({})** days ago.".format(user.created_at.strftime("%d %b %Y"), passed)
        passed1 = (ctx.message.created_at - user.joined_at).days
        joined_at = "{}.  **({})** days ago.".format(user.joined_at.strftime("%d %b %Y"), passed1)
        member_number = sorted(server.members, key=lambda m: m.joined_at).index(user) + 1
        em = discord.Embed(colour=color, timestamp=time)
        em.set_thumbnail(url=avi)
        em.add_field(name='Name:', value=user.name, inline = False)
        em.add_field(name='NickName:', value=user.nick, inline = False)
        em.add_field(name='Member No:',value=str(member_number), inline = False)
        em.add_field(name='Status:', value=user.status, inline = False)
        #em.add_field(name='Account Created:', value=user.created_at.__format__('%A, %d. %B %Y'), inline = False)
        em.add_field(name='Account Created:', value= created_at, inline = False)
        #em.add_field(name='Join Date:', value=user.joined_at.__format__('%A, %d. %B %Y'), inline = False)
        em.add_field(name='Join Date:', value=joined_at, inline = False)
        em.add_field(name='Roles:', value=rolenames, inline=True)
        em.set_footer(text='User ID: '+str(user.id))
        em.set_author(name=user, icon_url=server.icon_url)

        try:
            await ctx.send(embed=em)
        except discord.HTTPException:
            em_list = await embedtobox.etb(em)
            for page in em_list:
                await ctx.send(page)



    @commands.command(aliases=['bot', 'info'])
    async def about(self, ctx):
        '''About The bot, info, usage, process'''
        about = """A personal BOT For `Shan#1250` and `swirlcat#6666`\n```Made by SoulBlaze```"""

        embed = discord.Embed()
        embed.colour = await ctx.get_dominant_color(ctx.author.avatar_url)

        embed.set_author(name='Shwirl BOT', icon_url=ctx.author.avatar_url)

        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)



        now = datetime.datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)


        fmt = '{h}h {m}m {s}s'
        if days:
            fmt = '{d}d ' + fmt
        uptime = fmt.format(d=days, h=hours, m=minutes, s=seconds)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074793189670922/image.jpg")
        embed.add_field(name='Owner', value='#Shan#1250', inline = False)
        embed.add_field(name='About', value=about, inline = False)
        embed.add_field(name='Uptime', value=uptime, inline = False)
        embed.add_field(name='Guilds', value=len(self.bot.guilds), inline = False)
        embed.add_field(name='Total Users (Online/Total)', value=f'{total_online}/{total_unique}', inline = False)
        memory_usage = self.bot.process.memory_full_info().uss / 1024**2
        cpu_usage = self.bot.process.cpu_percent() / psutil.cpu_count()
        embed.add_field(name='Process: ', value=f'{memory_usage:.2f} MiB\n{cpu_usage:.2f}% CPU', inline = False)
        embed.set_footer(text='Thank You For Using Me', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed=embed)



def setup(bot):
	bot.add_cog(Information(bot))
