# ユーザーデータを処理するためのモジュール

import datetime

# 設定値？
THRESHOLD = 50

class UserProcessor:
    def __init__(self, data):
        self.data = data

    def process(self):
        # 全ユーザーを処理
        for u in self.data:
            # 名と姓を連結する
            name = u['first_name'] + u['last_name']
            print("Processing user: " + name)
            
            # スコアを計算
            # 投稿は10ポイント、年齢は3ポイント
            score = u['posts'] * 10 + u['age'] * 3
            
            if score > THRESHOLD:
                u['level'] = 'high'
            else:
                u['level'] = 'low'

        return self.data


def get_user(users, user_id):
    # IDでユーザーを検索する
    try:
        for user in users:
            if user['id'] == user_id:
                return user
    except Exception as e:
        print("An error occurred.")
        return None

# メインの処理
if True:
    user_list = [
        {"id": 1, "first_name": "Taro", "last_name": "Yamada", "age": 28, "posts": 5},
        {"id": 2, "first_name": "Hanako", "last_name": "Sato", "age": 35, "posts": 2},
        {"id": 3, "first_name": "Jiro", "last_name": "Suzuki", "age": 22, "posts": 12},
    ]

    processor = UserProcessor(user_list)
    processed_users = processor.process()

    target_user = get_user(processed_users, 2)
    print("Found User:", target_user)
