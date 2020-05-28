#tokens (written by me) library not included.
#by sszymoon#7106

import tokens
from PIL import Image
import urllib.parse
import random
import colors
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~:')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name='hide \'n\' seek', type=discord.ActivityType.playing))
    print('Ready as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send('An error raised while executing command: `{0}`'.format(error))
    
@bot.command()
async def ban(ctx, reason):
    pass

@bot.command(aliases=['vis_color','colour','vis_colour'])
async def color(ctx, hexval):
    try:
        if '#' in hexval:
            hexval = hexval.translate({ord('#'): None})
        myrgb = tuple(colors.hex(hexval).rgb)
        r, g, b = myrgb[0], myrgb[1], myrgb[2]
        color_img = Image.new('RGB', (200, 200), color = (int(r), int(g), int(b)))
        color_img.save('color_img.png')
        sendimg=open('color_img.png', 'rb')
        await ctx.send(file=discord.File(sendimg, 'color.png'))
        sendimg.close()
    except:
        await ctx.send('Cannot generate picture from given hex value.')
                       
@commands.cooldown(1, 10, commands.BucketType.guild)
@bot.command(aliases=['latency'])
async def ping(ctx):
    await ctx.send('`Bot ping: {0}ms Bot latency: {1}ms`'.format(round(bot.latency*1000), round(bot.latency,2)))

@bot.command()
async def gsearch(ctx, *, keyword):
    keyword = urllib.parse.quote(keyword, safe='')
    link = 'https://www.google.com/search?q='+keyword
    embedlink=discord.Embed(
        title='Google Search',
        description=link,
        colour=discord.Colour.green()
    )

    await ctx.send(embed=embedlink)

@bot.command()
async def gimage(ctx, *, keyword):
    keyword = urllib.parse.quote(keyword, safe='')
    link = 'https://www.google.com/search?tbm=isch&q='+keyword
    embedlink=discord.Embed(
        title='Google Image Search',
        description=link,
        colour=discord.Colour.green()
    )

    await ctx.send(embed=embedlink)

@bot.command()
async def invite(ctx):
    thisEmbed=discord.Embed(
        title='Server Invite',
        description='Click on link below\nhttps://discord.gg/PRdgmr3',
        colour=discord.Colour.from_rgb(255,255,0)
    )
    await ctx.send(embed=thisEmbed)

bot.run(tokens.tilde)
