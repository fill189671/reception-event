# インストールした discord.py を読み込む
import discord
#rondomをインポート
import random
#osをインポート
import os
import copy


# 自分のBotのアクセストークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready(): # 起動したら
	chID = os.environ['DISCORD_CH_ID'] # 受付するチャンネルID(int)
	channel = client.get_channel(chID)
	await channel.send("受付を開始。さあ、開場だ！") # 起動ワードを発言

# 受付
@client.event
async def on_member_join(member): # 新規メンバーが参加してきたら
	chID = os.environ['DISCORD_CH_ID'] # 受付するチャンネルID(int)
	channel = client.get_channel(chID)
	await channel.send(member.mention + 'ようこそニューロエイジへ！アンタのTwitterアカウントを教えてくれ。ただし＠マークは抜きでな。余計な文字も抜きで頼むぜ。（例：ONlineONly_TNX）') # 名前を訊く

@client.event
async def on_message(message): # メッセージが送られたら
	chID = os.environ['DISCORD_CH_ID'] # 受付するチャンネルID(int)
	table = os.environ['EVENT_TABLE'] # 卓情報（herokuの環境変数に格納）
	if message.channel.id ==chID and client.user != message.author : # 受付チャットの発言、かつ送り主が自分自身でなければ
		for t in table : #卓ごとの
			for m in t['mem'] : #各参加者リストの
				if message.content in m and message.content.startswith('@') != True : #@から始まらず、参加者名簿の名前に一致する内容だったら
					role = discord.utils.get(message.guild.roles, name=str(t['name'])) #付与する役職を取得
					await message.channel.send(message.author.mention + ' やあお友達、参加者名簿との確認が済んだぜ。アンタは{0}RLの{1}だな。以降は <#{2}>もしくは <#{3}> で{0}RLの指示に従ってくれ。GOOD LUCK！'.format(t['rl'],t['name'],t['uw_ch'],t['za_ch'])) # 受付メッセージを送信
					await message.author.add_roles(role) # 新しい役職を付与
					break # 一致したのでループを抜ける
		else : # 全ての名簿と不一致だった場合
			await message.channel.send(message.author.mention + ' Ooops！悪いなお友達、名簿の確認がうまくいかなかった。もう一度頼むぜ。') #もう一度入力してもらう
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
