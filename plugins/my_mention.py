from slackbot.bot import respond_to, listen_to  # @botname: で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ


@listen_to('きのうえ') #反応してほしい言葉
def mention_func(message):
    message.reply('だいすき（チュッ') # メンション
    message.react('kissing_heart')


@listen_to('りゅう')
def ryu_func(message):
    message.reply('頭が虹色')
    message.react('ultra')


@respond_to('かっこいい')
def cool_func(message):
    message.reply('せやろ。もっと言ってくれていいで。')
    message.react('sunglasses')


@listen_to('辛い')
def encourage_func(message):
    message.reply('元気出せよ。今度肉奢ったる。')
    message.react('meat_on_bone')


@listen_to('疲れた')
def sinpai_func(message):
    message.reply('大丈夫？休むのも大事やで。')


@listen_to('楽しかった')
def sinchoku_func(message):
    message.reply('あれ？研究の進捗は?')
    message.react('kenkyu1')
    message.react('kenkyu2')
    message.react('kenkyu3')
    message.react('kenkyu4')
    message.react('kenkyu5')
    message.react('kenkyu6')


@listen_to('時間')
def speed_func(message):
    message.reply('まぁ、時間をコントロールしてこそ社会人みたいなとこあるしな')


@listen_to('しますか?')
def onechance_func(message):
    message.reply('わんちゃんあり')
