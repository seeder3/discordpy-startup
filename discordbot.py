from discord.ext import commands
from discord.ext import tasks
import random
import os
import traceback
import datetime
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = bot.get_channel(784788831253037077)
    await channel.send('Bot reloaded complete.')

# russiaコマンドで用いる日付判定関数
def otoware_fes():
    now = datetime.datetime.today()  # コマンド呼び出し時点での日時を取得
    if((now.day == 29) and (now.hour >= 15)):  # 各月29日の15時以降でfesモードon
        return True
    elif(30 <= now.day <= 31):  # 各月31日まで行う
        return True
    else:   # それ以外の日ではoff
        return False

# bot起動時に実行されるイベントハンドラを定義
@bot.event
async def on_ready():
    await greet()   # 挨拶する非同期関数を実行

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def command(ctx):
    await ctx.send('/russia -> ロシア国歌\n/mahjong ->雀魂\n/textage keyword -> textage検索\n/chimpo->おちんぽ')

@bot.command()
async def russia(ctx, number=1):
    if(number > 10):
        await ctx.send('1度に10回までしか回せません')
    else:
        if(otoware_fes()):
            B = 0.06
        else:
            B = 0.03
        for i in range(number):
            A = random.random()
            if(A >= B):
                await ctx.send('https://www.youtube.com/watch?v=a0g1MTsYZSE')
            else:
                await ctx.send('https://www.youtube.com/watch?v=KOBMxU164Oc')   # (B)%で音割れ

# 1分に一回ループ
@tasks.loop(minutes=1)
async def time_check():
    now = datetime.datetime.today()  # 現在時刻を取得
    if((now.day == 29) and (now.hour == 15)):
        channel = bot.get_channel(784788831253037077)
        await channel.send('音割れフェス開始! 期間中は/russiaでの音割れ出現確率2倍!(29日15時~月変更)')
        await asyncio.sleep(hours=1)
    if((now.day == 1) and (now.hour == 0)):
        channel = bot.get_channel(784788831253037077)
        await channel.send('音割れフェス終了')
        await asyncio.sleep(hours=1)
    if((now.day == 8) and (now.hour == 16)):
        channel = bot.get_channel(784788831253037077)
        await channel.send('毎月8日はINFINITASの日!(ログインBIT5倍,FREEチケット×1)')
        await asyncio.sleep(hours=1)

@bot.command()
async def mahjong(ctx):
    await ctx.send('https://game.mahjongsoul.com/')

@bot.command()
async def textage(ctx, arg=''):
    if not arg:
        await ctx.send('https://textage.cc/score/index.html?a011B000')
    else:
        code = []   # 各文字のutf-16文字コードを入れる配列
        string = list(arg)  # 文字を取得

        for i in range(len(string)):
            s = list((hex(ord(string[i]))))
            print(s)
            if(len(s) <= 4):
                t = s[0:6]
                t[1] = '0'
            else:
                t = s[2:6]
            code.append(''.join(t))
        await ctx.send('https://textage.cc/score/index.html?r211B000_' + (''.join(code)))

@bot.command()
async def lv11(ctx):
    await ctx.send('https://docs.google.com/spreadsheets/d/1e7gdUmBk3zUGSxVGC--8p6w2TIWMLBcLzOcmWoeOx6Y/edit#gid=411493762')

@bot.command()
async def lv12(ctx):
    id = ctx.author.id
    if(id == 379913769800826890):
        await ctx.send('https://sp12.iidx.app/sheets/9282-4798/clear?reverse_sheet=true')
    else:
        await ctx.send('https://sp12.iidx.app/sheets/2533-6500/clear?reverse_sheet=true')

@bot.command()
async def chimpo(ctx):
    await ctx.send('https://www.youtube.com/watch?v=0g3U4yUktvs')

@bot.command()
async def fuck(ctx):
    await ctx.send(':middle_finger:')

@bot.command()
async def anamei(ctx):
    await ctx.send('.　＿\n＿　\n＿　\n　＿\n　＿\n＿　\n＿　\n　＿\n＿　\n　＿\n＿　\n＿　\n＿　\n　＿\n＿　\n＿　')

@bot.command()
async def geri(ctx):
    await ctx.send('下痢の時は地力が1段階上昇するという民間伝承。\n参考動画:https://youtu.be/oRZqB8TUTNc')

@bot.command()
async def poem(ctx):
    await ctx.send('時は地獄の様相を呈してきた世紀末\n
                    \n
                    かつて乗合バスとして長年慕われ平和な時代を過ごしてきた俺は､燃料もバッテリーも抜かれスクラップ同然\n
                    顔なじみの乗客達が蹂躙され虐げられる惨状を割れたヘッドライトから見つめるしかなかった\n
                    リフレクターに溜まった雨は溢れ出し､きっと涙のように見えていたことだろう\n
                    \n
                    独り密やかに怒りの炎を燃やし続けるだけという無為の日々…いつしか意識は途絶えた\n
                    \n
                    だが､再び目覚めた時､猛烈な加速と高速巡航を両立させる大出力の電気式ハイブリッドシステムに換装し､複合装甲によるフルカバードボディと計62丁の重機関銃で武装した､地上で最強のマシンへと生まれ変わっていた\n
                    \n
                    今日も俺は荒野を爆走する\n
                    わずかな希望を停留させる人々を乗せて､共に戦いながら\n
                    地の果てにはあるだろう､穏やかな生活を取り戻せる場所に辿り着くまで\n')

time_check.start()

bot.run(token)
