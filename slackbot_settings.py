import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
AP= os.environ.get("API_KEY") 
# 環境変数の値をAPに代入
# SlackのAPIを利用するためのトークン
# Botの設定ページから「OAuth & Permissions」のページに遷移し、
# 「Bot User OAuth Access Token」をコピーして貼り付ける
API_TOKEN = AP

# 対応するメッセージがなかった場合に反応するメッセージ
DEFAULT_REPLY = "Context Aware GAN!!!!!!!!!!!!!!!!!!!!!!!!!!!"

PLUGINS = [
        'plugins',
]
