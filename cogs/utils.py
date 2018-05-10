''' from ami and selfbot '''

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

            general = "`avatar`,`about`,`invite`,`say`,`lover`,`user`, `interaction`, `compliment`, `letter`, `help`"

            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074340263690241/image.jpg")
            em.set_author(name = 'Help Menu~',icon_url = ctx.author.avatar_url )
            em.description = "My **Prefix** is **shwirl**.To use the commands do shwirl[command].\nFor more info on commands do `shwirlhelp commands`"
            em.add_field(name = '**Commands:**', value = general, inline = False)
            em.colour = discord.Colour.red()
            em.set_footer(text = "Shwirl BOT",icon_url = self.bot.user.avatar_url)

            await ctx.send(embed = em)


        elif args.lower() == 'commands':


            invite = "Invite me to your server.\n**Uses:** `shwirlinvite`"
            avatar = "Get your avatar.\n**Uses:** `shwirlavatar`,`shwirlavatar @mention`"
            about = "Get more info about me.\n**Uses:** `shwirlabout`"
            help = "Shows the list of commands and their expanded category.\n**Uses:** `shwirlhelp` or `shwirlhelp [Commands]`"
            interaction = "Interactive commands like\n`hug`,`cuddle`,`kiss`,`nom`, `lick`, `poke`.\n**Uses:**`shwirl[action] @metion` Without []"
            personal = "Shows lover commands of shwirl.\n**Uses:** `shwirllover shan` or `shwirllover swirlcat`"
            say = "Make me say something.\n**Uses:**`shwirlsay [sentence]` without []"
            user = "Shows user info of member.\n**Uses:**`shwirluser` or `shwirluser @mention`"
            letter = "Shows A Love Letter :heart:.\n**Uses:**`shwirlletter`"
            compliment = "Sends a random compliment.\n**Uses:**`shwirlcompliment @mention`"



            em = discord.Embed()
            em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074887905705984/image.gif")
            em.set_author(name = 'Commands Help~',icon_url = ctx.author.avatar_url )
            em.description = "These are commands of the bot."
            em.add_field(name = '**1.Lover**', value = personal, inline = False)
            em.add_field(name = '**2.Avatar:**', value = avatar, inline = False)
            em.add_field(name = '**3.Say:**', value = say, inline = False)
            em.add_field(name = '**4.Interactive:**', value = interaction, inline = False)
            em.add_field(name = '**5.User:**', value = user, inline = False)
            em.add_field(name = '**6.Letter:**', value = letter, inline = False)
            em.add_field(name = '**7.Compliment:**', value = compliment, inline = False)
            em.add_field(name = '**8.About:**', value = about, inline = False)
            em.add_field(name = '**9.Invite:**', value = invite, inline = False)
            em.add_field(name = '**10.Help:**', value = help, inline = False)
            em.colour = discord.Colour.blue()
            em.set_footer(text = "Shwirl BOT",icon_url = self.bot.user.avatar_url)

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
