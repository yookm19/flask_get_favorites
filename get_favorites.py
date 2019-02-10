# 必要なモジュールのインポート

from flask import Flask, render_template, request, redirect, url_for
import requests
from base64 import b64decode, b64encode
from flask_cors import CORS
import json


#データベースの設定

app = Flask(__name__)

CORS(app)

#関数の設定

@app.route("/")
def top():
    user_id = request.args.get('uid')
    count = request.args.get('count')
    # user_id = "1425393612" #引数として渡すようにする
    headers = { "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8" }
    data = { "grant_type":"client_credentials" }
    oauth2_url = "https://api.twitter.com/oauth2/token"
    r = requests.post(oauth2_url, data=data, headers=headers, auth=("ASWHVhMdDeUoDxEzeSmfgwuVq", "hq1bmBt3vj6QjRhQcchhyoULGQZlrjIC05OUkJyzShRdYZXe4q"))
    bearer_token = r.json()["access_token"]

    # ===== 3. Userのtimelineを取得 =====
    url = "https://api.twitter.com/1.1/favorites/list.json?user_id={}&count={}".format(user_id,count)
    headers = {
        "Authorization": "Bearer {}".format(bearer_token)
    }
    r = requests.get(url, headers=headers)
    tweets = r.json()

    # Twitter APIから取得したjson形式のデータをビュー側へ返す
    # 詰まってる。。。
    return json.dumps(tweets,ensure_ascii=False)
    # return tweets[5]["text"]
    # favorites_tweets = []
    # for i in range(len(tweets)):
    #     tweet = json.dumps(tweets[i])
    #     # tweet = tweet["text"]
    #     # return tweet
    #     favorites_tweets.append(tweet)

    # return favorites_tweets




#実行

if __name__ == '__main__':
    app.run(debug=True)