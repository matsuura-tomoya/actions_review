import snowflake.connector


def generate_report(region_input: str):
    """
    指定された地域の売上レポートを生成する。
    この関数にはSQLインジェクションの脆弱性が含まれている。
    """

    # ... Snowflakeへの接続設定（省略） ...
    # conn = snowflake.connector.connect(...)
    # cursor = conn.cursor()

    # ▼▼ ここが脆弱なポイント ▼▼
    # 外部からの入力(region_input)を、直接SQL文に埋め込んでいる。
    # Snyk Codeは、このような危険なパターンを「SQLインジェクション」として検出します。
    query = f"""
        WITH sales_details AS (
          SELECT
            s.product_id,
            s.customer_id,
            s.quantity * s.unit_price AS total_amount
          FROM
            sales AS s
          WHERE
            s.sale_date >= DATEADD(month, -3, CURRENT_DATE())
        )
        SELECT
          p.product_category,
          ROUND(SUM(sd.total_amount), 2) AS total_revenue
        FROM
          sales_details AS sd
        JOIN
          products AS p ON sd.product_id = p.product_id
        JOIN
          customers AS c ON sd.customer_id = c.customer_id
        WHERE
          c.region = '{region_input}' -- ← 危険な埋め込み！
        GROUP BY
          p.product_category
        ORDER BY
          total_revenue DESC;
    """
    # ▲▲ ここまで ▲▲

    print("--- 実行されるクエリ ---")
    print(query)
    # cursor.execute(query) # 実際にDBにクエリを送信
    # ...


# --- 実行例 ---

# 正常な呼び出し
print("【正常な呼び出し】")
generate_report("関東")

# 悪意のある呼び出し（SQLインジェクション攻撃）
print("\n【悪意のある呼び出し】")
# WHERE句を無効化し、全ての地域のデータを盗み見る攻撃
generate_report("' OR '1'='1")
