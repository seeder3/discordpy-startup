from discord.ext import commands
import random
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(784788831253037077)
    await channel.send('Bot reload complete.')

# bot起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def command(ctx):
    await ctx.send('/russia -> ロシア国歌\n/mahjong ->雀魂\n/textage -> textage譜面一覧')

        
    
@bot.command()   
async def russia(ctx):
    a = random.random()
    if (a < 0.03)
        await ctx.send('https://www.youtube.com/watch?v=a0g1MTsYZSE')
    else
        await ctx.send('https://www.youtube.com/watch?v=KOBMxU164Oc') #3%で音割れ

@bot.command()   
async def mahjong(ctx):
    await ctx.send('https://game.mahjongsoul.com/')

@bot.command()   
async def textage(ctx):
    await ctx.send('https://textage.cc/score/index.html?a011B000')

@bot.command()
async def chimpo(ctx):
    await ctx.send('https://www.youtube.com/watch?v=0g3U4yUktvs')
    

bot.run(token)
