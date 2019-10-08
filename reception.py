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
	chID = 630771316102004736 # 受付するチャンネルID(int)
	channel = client.get_channel(chID)
	await channel.send("受付を開始。さあ、開場だ！") # 起動ワードを発言

# 受付
@client.event
async def on_member_join(member): # 新規メンバーが参加してきたら
	await message.channel.send('{member.mention} ようこそニューロエイジへ！アンタのTwitterアカウントを教えてくれ。ただし＠マークは抜きでな。余計な文字も抜きで頼むぜ。（例：ONlineONly_TNX）') # 名前を訊く

@client.event
async def on_message(message): # メッセージが送られたら
	if message.channel.id == 630771316102004736 : # 受付チャットの発言にのみ反応
		t = [
		{'name':'a卓','rl':'中野','mem':['SanpaiMikan','gray_vb42','YuiooQa'],'uw_ch':607230283908907018,'za_ch':607230574767112194}, # A卓RL、参加者一覧、アンダーワークID、雑談ID
		{'name':'b卓','rl':'ハニワ','mem':['plusmint','massujazeyo','NktAts'],'uw_ch':607230504290353152,'za_ch':607230631277101107}, # B卓RL、参加者一覧、アンダーワークID、雑談ID
		{'name':'c卓','rl':'神姫','mem':['camelia_ml','cat_ate_teacher','kinoakira'],'uw_ch':607237345808220161,'za_ch':607237388376211490} # C卓RL、参加者一覧、アンダーワークID、雑談ID
		]
		if client.user != message.author : # 送り主が自分自身でなければ
			for table in t : #卓ごとの
				if message.content in table['mem'] : #参加者名簿の名前に一致するものがあったら
					role = discord.utils.get(message.guild.roles, name=str(table['name'])) #付与する役職を取得
					await message.channel.send(message.author.mention + ' やあお友達、参加者名簿との確認が済んだぜ。アンタは{0}RLの{1}だな。以降は <#{2}>もしくは <#{3}> で{0}RLの指示に従ってくれ。GOOD LUCK！'.format(table['rl'],table['name'],table['uw_ch'],table['za_ch'])) # 受付メッセージを送信
					await message.author.add_roles(role) # 新しい役職を付与
					break # 一致したのでループを抜ける
			else : # 全ての名簿と不一致だった場合
				await message.channel.send(message.author.mention + ' Ooops！悪いなお友達、名簿の確認がうまくいかなかった。もう一度頼むぜ。') #もう一度入力してもらう
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
