from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def help(ctx):
    await ctx.send('/russia -> ロシア国歌\n/mahjong ->雀魂\n/textage -> textage譜面一覧')
    
@bot.command()   
async def russia(ctx):
    await ctx.send('https://www.youtube.com/watch?v=a0g1MTsYZSE')

@bot.command()   
async def mahjong(ctx):
    await ctx.send('https://game.mahjongsoul.com/')

@bot.command()   
async def textage(ctx):
    await ctx.send('https://textage.cc/score/index.html?a011B000')

bot.run(token)
