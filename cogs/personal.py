''' Personal editable command cog made by SoulBlaze
    to edit only change the ones with the hashtags'''


import os
import discord
from discord.ext import commands
import json
import random



class Personal:
    def __init__(self, bot):
        self.bot = bot




    @commands.command()
    async def lover(self,ctx,*,args = None):

        if args.lower() == 'shan':

            em = discord.Embed()
            em.description = "Swirlcat's precious everything"#update this to update the text part of the personal commands
            em.set_image(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074887905705984/image.gif")#change the link in the "" to change the image added to it

            await ctx.send(embed = em)

        elif args.lower() == 'shwirlcat':

            em = discord.Embed()
            em.description = "Shan's nomable sweetheart"#update this to update the text part of the personal commands
            em.set_image(url = "https://cdn.discordapp.com/attachments/409425345498972170/443074887905705984/image.gif")#change the link in the "" to change the image added to it


            await ctx.send(embed = em)

        else:
            await ctx.send("Please type the name of the lover :wink:")





    @commands.command()
    async def compliment(self,ctx, *, args = None):
        with open('data/compliments.json') as f:
            compliments = json.load(f) #any changes in compliments will be done in the json folder mentioned in the above line
        i = random.choice(compliments)

        await ctx.send("Dear **"+args+"**, "+i)




    @commands.command()
    async def letter(self,ctx):

        em = discord.Embed()
        em.set_thumbnail(url = "https://cdn.discordapp.com/avatars/443020772584325120/3c39894ada2bdbf4cee3b418b132fe52.png?size=1024") #change the link within the collons to change the picture
        em.description = """
**My beautiful SwirlyGirly,**

I know we have had a couple of bad days recently and they are weighing heavily on you but believe me sweetheart I don’t want that for you. I want to take you and your heart away from the troubles you faced in the past. I promise you with all that I am that I will save you from anything you are running from. I will keep you in my life until the day I die (you know it’s hard for me to talk about that) and I will keep you even after that. I have experienced love before and it was no where near as amazing as what you show me everyday. I honestly believe I am one of the luckiest people on the planet. The jerks who have held you before were fools to let your hand go and that’s a mistake I will never make. I love you sewel with all of my heart and my soul. I am eternally yours and you are eternally mine. I want to share with you all that I can and I may not be the first to do somethings with you but I will definitely be the last. I love you sweetheart more than I could ever express to you or to anyone I will just have to show the day I watch you walk down the isle and say I do.

**With all my heart, Your Shanny**
""" # update this box to change anything in the letter
        em.colour = discord.Colour.red()

        await ctx.send(embed = em)








def setup(bot):
	bot.add_cog(Personal(bot))
