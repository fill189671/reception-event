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
#@client.event
#async def on_ready(): # 起動したら
#	chID = int(os.environ['DISCORD_CH_ID']) # 受付するチャンネルID(int)
#	channel = client.get_channel(chID)
#	await channel.send("受付を開始。さあ、開場だ！") # 起動ワードを発言

# 受付
@client.event
async def on_member_join(member): # 新規メンバーが参加してきたら
	chID = int(os.environ['DISCORD_CH_ID']) # 受付するチャンネルID(int)
	channel = client.get_channel(chID)
	await channel.send(member.mention + 'ようこそニューロエイジへ！アンタのTwitterアカウントを教えてくれ。ただし＠マークは抜きでな。余計な文字も抜きで頼むぜ。（例：ONlineONly_TNX）') # 名前を訊く

@client.event
async def on_message(message): # メッセージが送られたら
	chID = int(os.environ['DISCORD_CH_ID']) # 受付するチャンネルID(int)
	table = [{"name":"A卓","rl":"あるば","mem":["meganeoki_game","WaterMargin36","kokonoe0722","g_a_trpg"],"uw_ch":650660171613339658,"za_ch":650660422684508161},\
{"name":"B卓","rl":"湊","mem":["psyka294","yuge_taro","liarnose","yakin3913"],"uw_ch":650660275178962974,"za_ch":650660455752269824},\
{"name":"C卓","rl":"SONE","mem":["vankittea","SeleneRosedream","potechi_lja","gikoneko_24"],"uw_ch":650660304698605568,"za_ch":650660485070323714},\
{"name":"D卓","rl":"ViVi","mem":["higecythe","Atai_marukyu","kinoakira","Sakoy_trpg"],"uw_ch":650660330518609920,"za_ch":650660508424208405},\
{"name":"E卓","rl":"ソエジマ","mem":["yukaristos","straytalkie","dragoste_eu"],"uw_ch":650660357114691617,"za_ch":650660545308917783}] # 卓情報（herokuの環境変数に格納）
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
