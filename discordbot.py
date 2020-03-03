#インストールしたdiscord.pyの読み込み
import discord 
import os
#randomモジュールの読み込み
import random
#reライブラリの読み込み
import re
#datetimeの読み込み
import datetime

#翠のトークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

#接続に必要なオブジェクトを生成
client = discord.Client()

#起動時に動作する処理
@client.event
async def on_ready():
    print('Hello World,プログラム「Project-SUI-」、起動しました')

#メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    #メッセージ送信者がbotだった場合の無視処理
    if message.author.bot:
            return

#サーバーステータス
 #サーバー人数
    if '翠、今のサーバーステータスを教えて' in message.content:
        await message.channel.send(f'現在就寝中のノイマンちゃんに代わり翠がお伝えします。今のサーバー人数は{len(message.guild.members)}人です！')

#会話
 #おはよう
    #「おはよう」と発言したら「おはようございます、(送信したユーザーネーム)様！」と返す処理
    G_lis = ['今日も一日頑張りましょうね！','いってらっしゃいませー！']
    respon = random.choice(G_lis)
    if message.content.startswith('おはよ') or message.content == 'ぐっもーにん':
        await message.channel.send('おはようございます、' + message.author.name + '様！( ⑉¯ ꇴ ¯⑉ )\n' + respon)
 #おやすみ
    #「おやすみ」と発言したら「おやすみなさい！」と返す処理
    if message.content.startswith('おやすみ'):
        await message.channel.send('おやすみなさい、良い夢を見てくださいね！(｡•̀ᴗ-)✧')	
 #おわ
    #「おわ」でメッセージが終わった場合労う
    if 'おわ' in message.content:
        await message.channel.send('お疲れ様です！∠(｀･ω･´)')	
 #にゃあ
    #「にゃあ」と言ったら猫の真似をする			
    if message.content == '翠、猫の真似して欲しい！' or message.content == '翠、癒して！':
        await message.channel.send('ฅ(๑>ㅅ<๑)ฅﾆｬｰ')
 #起きてる？ 
    #「起きてる？」と言ったら返事する
    if message.content == '翠、起きてる？':
        await message.channel.send('私はいつも起きてますよ！何かご用ですか？((っ•ω•⊂))')
 #褒め
    #「可愛い」と言うと照れる
    if message.content == '翠、可愛い！' or message.content == '翠、かわいい！':
        await message.channel.send('( ﻿˶﻿ˆ꒳ˆ˵﻿ )ｴﾍﾍ、ありがとうございます！スイ、頑張りますね！')

 #御籤 
    #「翠、おみくじ引かせて！」って言うとおみくじ引く
    if '翠、御籤引かせて' in message.content or '翠、今日の運勢' in message.content:
        prob = random.random()
    
        if prob < 0.3:
            await message.channel.send('凶です……外出を控えることをオススメします(  ･᷄ὢ･᷅  )')
        
        elif prob < 0.65:
            await message.channel.send('吉です！何かいい事があるかもですね！')
        
        elif prob < 0.71:
            await message.channel.send('末吉……どれくらい運がいいんでしょうね？•́ω•̀)?')
        
        elif prob < 0.76:
            await message.channel.send('半吉は吉の半分、つまり運がいいのです！')
        
        elif prob < 0.80:
            await message.channel.send('小吉ですね！ちょっと優しくされるかも？')
        
        elif prob < 0.83:
            await message.channel.send('吉の中で1番当たっても微妙に感じられる……つまり末吉なのです( ´･ω･`)')
       
        elif prob <= 1.0:
            await message.channel.send('おめでとうございます！大吉ですよ！(๑>∀<๑)♥')
 #忍殺語
    if message.content == '変わり身のジツ！':
        await message.channel.send('イヤーッ！(｢･ω･)｣ｱﾁｮ')
 #宝具
    if message.content == ('翠、剣禅一如見せて！'):
    
        probability = random.random()
    
        if  probability > 0.75:
            await message.channel.send('いざ。剣は生死の狭間にて大活し、禅は静思黙考の内大悟へ至る。我が剣に、お前は何れを見るものか。『剣術無双・剣禅一如』((꜆꜄ ˙꒳˙)꜆꜄꜆')
        elif probability < 0.75:
            await message.channel.send('参る……。我が心は不動。しかして自由にあらねばならぬ。即ち是、無念無想の境地なり。『剣術無双・剣禅一如』( ´−ω−`)')
 #年月日
    if all(s in message.content for s in['今日','何日']):
        date = datetime.datetime.now()
        await message.channel.send(f'今日は{date.year}年{date.month}月{date.day}日ですね！')    
    if all(s in message.content for s in ['今','何時']):
        date = datetime.datetime.now()
        await message.channel.send(f'今は{date.hour}時{date.minute}分{date.second}秒ですよ！')

#埋込みメッセージ「議題」
    if '議題作成' in message.content:
        match = re.search(r".*タイトルは(.+)、サブタイトルは(.+)。.*", message.content)
        if match:
            title, subtitle = match.groups()
            embed = discord.Embed(title=title, description=subtitle,color=discord.Color.green())
            await message.channel.send(embed=embed)

#自動会話
 #笑
    lis = ['笑うのは体にいいことなのです！','ꉂꉂ(>ᗜ<*)']
    res = random.choice(lis)
    
    if (message.content.endswith(('笑','w')) and random.random() > 0.75):
        await message.channel.send(res)
 #ほえー
    li = ['ほえー','わー','えへっ']
    resp = random.choice(li)
    
    if message.content == 'おはよ':
        pass
    elif (message.content.endswith(('よ','かぁ')) and random.random() < 0.4):
        await message.channel.send(resp)

#ロール付与

async def add_role(role_name:str):
        if role_name in message.content:
            for role in message.guild.roles:
                if role.name == role_name:
                    if not message.author in role.members:
                        await message.author.add_roles(role)

def add_role(role_name:str,message:discord.Message):
    if role_name in message.content:
        for role in message.guild.roles:
            if role.name == role_name:
                if not message.author in role.members:
                    await message.author.add_roles(role)
                    
    # 発言が自己紹介チャンネルだったら
    if message.channel.name == "自己紹介":
        lang_list = ["c", "c++", "c#", "python", "unity", "java", "javascript", "html", "css", "wordpress"]
        for lang in lang_list:

            # メッセージの中に言語が含まれていれば
            if lang in message.content:
                guild = message.guild
                role = discord.utils.find(lambda r: r.name == lang, guild.roles)
                if role is not None:
                    member = message.author

                    # 役職を付与する
                    await member.add_roles(role)

#ウェルカムメッセージ

get_channel_id = {673412098683830284:673412099350855702,633956743616921620:634257472865173525}

@client.event
async def on_member_join(member):
   global get_channel_id
   await client.get_channel(get_channel_id[member.guild.id]).send(f'ようこそ、**{member.mention}**さん！あなたの訪問を歓迎させていただきます、翠です！')

#リムーブメッセージ
@client.event
async def on_member_remove(member):
    global get_channel_id
    await client.get_channel(get_channel_id[member.guild.id]).send(f'**{member.name}がサーバーを離れました。**')

#botの起動とdiscordサーバーへの接続
client.run(TOKEN)
