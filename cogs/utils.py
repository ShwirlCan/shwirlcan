
import discord
from discord.ext import commands
from discord.ext.commands import TextChannelConverter
from contextlib import redirect_stdout
from ext.utility import load_json
from urllib.parse import quote as uriquote
from lxml import etree
from ext import fuzzy
from ext import embedtobox
from PIL import Image
import unicodedata
import traceback
import textwrap
import aiohttp
import inspect
import asyncio
import time
import re
import io
import os
import random

class Utility:
    '''Useful commands to make your life easier'''
    def __init__(self, bot):
        self.bot = bot
        self.lang_conv = load_json('data/langs.json')
        self._last_embed = None
        self._rtfm_cache = None
        self._last_google = None
        self._last_result = None



    @commands.command(name='help')
    async def help(self, ctx, *, args = None):

        if args is None:

            general = "`avatar`,`about`,`invite`,`say`,`shan`,`swirlcat`,`interaction`,`help`"

            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg")
            em.set_author(name = 'Help Menu~',icon_url = ctx.author.avatar_url )
            em.description = "My **Prefix** is **shwirl**.To use the commands do shwirl[command]"
            em.add_field(name = '**Commands:**', value = general, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "Shwirl",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed = em)


        elif args.lower() == 'commands':


            invite = "Invite me to your server.\n**Uses:** `shwirlinvite`"
            avatar = "Get your avatar.\n**Uses:** `shwirlavatar`,`shwirlavatar @mention`"
            about = "Get more info about me.\n**Uses:** `shwirlabout`"
            help = "Shows the list of commands and their expanded category.\n**Uses:** `shwirlhelp` or `shwirlhelp [Commands]`"
            interaction = "Interactive commands like\n`hug`,`cuddle`,`kiss`,`lick`,`nom`,`toungebite`"
            personal = "Shows personal commands of shwirl.\n**Uses:** `shwirl shan` or `shwirl swirlcat`"
            say = "Make me say something.\n**Uses:**`shwirlsay [sentence]` without []"



            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/388676126383276032/390477398287843329/images_5.jpg")
            em.set_author(name = 'Commands Help~',icon_url = ctx.author.avatar_url )
            em.description = "These are commands of the bot."
            em.add_field(name = '**1.User Info:**', value = user, inline = False)
            em.add_field(name = '**2.Personal Commands**', value = personal, inline = False)
            em.add_field(name = '**3.Avatar:**', value = avatar, inline = False)
            em.add_field(name = '**4.Say:**', value = say, inline = False)
            em.add_field(name = '**5.Interactive:**', value = interaction, inline = False)
            em.add_field(name = '**6.About:**', value = about, inline = False)
            em.add_field(name = '**7.Invite:**', value = invite, inline = False)
            em.add_field(name = '**8.Help:**', value = help, inline = False)
            em.colour = discord.Colour.teal()
            em.set_footer(text = "Shwirl",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed=em)



        else:
            await ctx.send('That does not exist. Check your **spelling!**')


    @commands.command()
    async def say(self,ctx,*,args=None):
        if args is None:
            await ctx.send('Type something you want me to say first!')
        else:
            await ctx.send(args)


def setup(bot):
    bot.add_cog(Utility(bot))
