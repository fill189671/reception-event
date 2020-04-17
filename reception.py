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
	chID = 590957330582208514 # 受付するチャンネルID(int)
	msCh = client.get_channel(chID)
	flag = 'off' # 寝たフラグを作る
	table = [] # 卓リストを宣言
	table_num_env = os.environ['EVENT_TABLE'] # 卓番号リストを取得（環境変数に入れる。例：a,b,c,d,e）
	table_num = table_num_env.split(",") # 卓番号リストを作成
	for h,i in enumerate(table_num) : # 卓数だけ繰り返す
		table[h] = {} # 辞書型で空の卓情報を宣言
		table_mem_env = os.environ['mem_'+ str(i)] # 各卓の参加者（環境変数に格納） mem_a,mem_b,mem_c... の形で変数宣言しとく。中身は"meganeoki_game","WaterMargin36","kokonoe0722","g_a_trpg"
		table_mem = table_mem_env.split(",") # 各卓の参加者をリスト化
		table_info_env = os.environ['info_'+ str(i)] # 各卓情報（環境変数に格納） info_a,info_b,info_c...の形で変数宣言しとく。中身は"name":"A卓","rl":"あるば","uw_ch":int(650660171613339658),"za_ch":int(650660422684508161,"mem":[meganeoki_game","WaterMargin36","kokonoe0722","g_a_trpg])
		table_list = table_info_env.split(",") # 各卓情報をキーと値をセット値にリスト化
		for tab_list in table_list : # セットリスト化した卓情報を一つずつ取り出し
			tab_dic = tab_list.split(":") # キーと値に分けてリスト化
			table[h][tab_dic[0]] = tab_dic[1] # キーと値として卓情報に追加
	if message.channel.id ==chID and client.user != message.author : # 受付チャットの発言、かつ送り主が自分自身でなければ
		for t in table : #卓ごとの
			for m in t['mem'] : #各参加者リストの
				if message.content in m and message.content.startswith('@') != True : #@から始まらず、参加者名簿の名前に一致する内容だったら
					role = discord.utils.get(message.guild.roles, name=str(t['name'])) #付与する役職を取得
					await message.channel.send(message.author.mention + ' やあお友達、参加者名簿との確認が済んだぜ。アンタは {0} RLの** {1} **だ。以降は <#{2}>もしくは <#{3}> でRLの指示に従ってくれ。GOOD LUCK！'.format(t['rl'],t['name'],t['uw_ch'],t['za_ch'])) # 受付メッセージを送信
					await message.author.add_roles(role) # 新しい役職を付与
					flag = 'on' # フラグを立てる
					break # 一致したのでループを抜ける
			if flag == 'on' :
				break # 一致したのでループを抜ける
		else : # 全ての名簿と不一致だった場合
			await message.channel.send(message.author.mention + 'Ooops！悪いなお友達、名簿の確認がうまくいかなかった。もう一度頼むぜ。') #もう一度入力してもらう
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

#@client.event
#async def on_message(message): # メッセージが送られたら
#	chID = int(os.environ['DISCORD_CH_ID']) # 受付するチャンネルID(int)
#	table = int(os.environ['EVENT_TABLE']) # 卓情報（herokuの環境変数に格納）
#	flag = 'off' # 寝たフラグを作る
#	if message.channel.id ==chID and client.user != message.author : # 受付チャットの発言、かつ送り主が自分自身でなければ
#		for t in table : #卓ごとの
#			for m in t['mem'] : #各参加者リストの
#				if message.content in m and message.content.startswith('@') != True : #@から始まらず、参加者名簿の名前に一致する内容だったら
#					role = discord.utils.get(message.guild.roles, name=str(t['name'])) #付与する役職を取得
#					await message.channel.send(message.author.mention + ' やあお友達、参加者名簿との確認が済んだぜ。アンタは{0}RLの{1}だな。以降は <#{2}>もしくは <#{3}> で{0}RLの指示に従ってくれ。GOOD LUCK！'.format(t['rl'],t['name'],t['uw_ch'],t['za_ch'])) # 受付メッセージを送信
#					await message.author.add_roles(role) # 新しい役職を付与
#					flag = 'on' # フラグを立てる
#					break # 一致したのでループを抜ける
#			if flag == 'on' :
#				break # 一致したのでループを抜ける
#		else : # 全ての名簿と不一致だった場合
#			await message.channel.send(message.author.mention + ' Ooops！悪いなお友達、名簿の確認がうまくいかなかった。もう一度頼むぜ。') #もう一度入力してもらう
