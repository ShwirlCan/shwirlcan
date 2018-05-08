''' A rewritten cog, consisting of old commands has kiss, hug commands.


Originally by Liam and noble
Rewritten by Liam for Shwirlcan

'''
import os
import discord
import json
import random
from discord.ext import commands
from cleverwrap import CleverWrap
import requests
from bs4 import BeautifulSoup

class Gen:
    def __init__(self, bot):
        self.bot = bot



    @property
    def kiss_gif(self):
        links = ["https://cdn.discordapp.com/attachments/409425345498972170/442980477570121738/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980593119264768/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980620025462796/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980664481021973/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980801382973440/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980848657235968/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980952726306817/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442980994677473281/image.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def cuddle_gif(self):
        links = ["https://cdn.discordapp.com/attachments/409425345498972170/442989023644876810/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442989029835800578/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442989038560083968/image.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def hug_gif(self):
        links = ["https://cdn.discordapp.com/attachments/409425345498972170/442983103791759370/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442983142039486474/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442983178135666688/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442983257294766080/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442983403491688448/image.gif"]
        choice_made= random.choice(links)
        return choice_made
    @property
    def nom_gif(self):
        links = ["https://cdn.discordapp.com/attachments/409425345498972170/442984727704502273/image.gif","https://cdn.discordapp.com/attachments/409425345498972170/442984736571260928/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442984798684708874/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442984809976037377/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442984826522435584/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/442985511213072384/image.gif"]
        choice_made= random.choice(links)
        return choice_made

    @property
    def lick_gif(self):
        links = ["https://cdn.discordapp.com/attachments/409425345498972170/443359304616116224/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/443359460396892160/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/443359487059820544/image.gif", "https://cdn.discordapp.com/attachments/409425345498972170/443359494295257088/image.gif", "https://cdn.discordapp.com/attachments/335346728897216512/443402975432671232/uALJJV2.gif"]
        choice_made= random.choice(links)
        return choice_made



    @commands.command()
    async def kiss(self, ctx, *, args):
        '''Kissing gif send, PS: missing args will show up at logs'''
        kiss = self.kiss_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(kiss))
        await ctx.send(content = "**{0} got kissed by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def nom(self, ctx, *, args):
        '''bitting gif send, PS: missing args will show up at logs'''
        nom = self.nom_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(nom))
        await ctx.send(content = "**{0} is being nommed by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def cuddle(self, ctx, *, args):
        '''cuddeling gif send, PS: missing args will show up at logs'''
        cuddle = self.cuddle_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(cuddle))
        await ctx.send(content = "**{0} is being cuddled by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def hug(self, ctx, *, args):
        '''hugging gif send, PS: missing args will show up at logs'''
        hug = self.hug_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(hug))
        await ctx.send(content = "**{0} got hugged by {1.mention}**".format(args, ctx.message.author), embed =em)

    @commands.command()
    async def lick(self, ctx, *, args):
        '''licking gif send, PS: missing args will show up at logs'''
        lick = self.lick_gif
        em = discord.Embed()
        em.set_image(url = "{}".format(lick))
        await ctx.send(content = "**{0} got licked by {1.mention}**".format(args, ctx.message.author), embed =em)



    @commands.command()
    async def invite(self,ctx):

        await ctx.send("<https://discordapp.com/oauth2/authorize?client_id=443020772584325120&scope=bot&permissions=305196166>")


    @commands.command()
    async def shan(self,ctx):

        em = discord.Embed()
        em.description = "Swirlcat's precious everything"#update this to update the text part of the personal commands
        em.set_image(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074887905705984/image.gif")#change the link in the "" to change the image added to it


        await ctx.send(embed = em)



    @commands.command()
    async def swirlcat(self,ctx):

        em = discord.Embed()
        em.description = "Shan's nomable sweetheart"#update this to update the text part of the personal commands
        em.set_image(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074887905705984/image.gif")#change the link in the "" to change the image added to it


        await ctx.send(embed = em)


def setup(bot):
	bot.add_cog(Gen(bot))
