import sqlite3
import flask

# Flaskアプリケーションのインスタンスを作成（Webフレームワークの文脈を持たせるため）
app = flask.Flask(__name__)

@app.route("/users")
def get_user():
    """
    ユーザーIDを元にデータベースから情報を取得する（脆弱な例）
    """
    # WebリクエストのパラメータからユーザーIDを取得
    user_id = flask.request.args.get('id')

    # データベース接続
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # --- ▼ ここが脆弱性のポイント！ ▼ ---
    # 外部からの入力(user_id)を、エスケープせずに直接SQL文に埋め込んでいる
    query = "SELECT * FROM users WHERE user_id = '" + user_id + "'"
    # --- ▲ ここまでが脆弱性のポイント！ ▲ ---

    try:
        cursor.execute(query)
        user_data = cursor.fetchone()
        return str(user_data)
    except sqlite3.Error as e:
        return f"Database error: {e}"
    finally:
        conn.close()

# Snykはコードをスキャンするだけで、このコードを実行する必要はありません。