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
import pip
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



    @commands.command(aliases=['bot', 'info'])
    async def about(self, ctx):
        '''About The bot, info, usage, process'''
        about = """A personal BOT For `Shan#1250` and `swirlcat#6666`"""

        embed = discord.Embed()
        embed.colour = await ctx.get_dominant_color(ctx.author.avatar_url)

        embed.set_author(name='Shwirl', icon_url=ctx.author.avatar_url)

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
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/338630075710701578/398862345125756938/images_2.jpeg?width=290&height=411")
        embed.add_field(name='Owner', value='Liam#3273\nID:300944772971888640', inline = False)
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
