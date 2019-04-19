from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

@respond_to('きのうえ') #反応してほしい言葉
def mention_func(message):
    message.reply('だいすき（チュッ') # メンション