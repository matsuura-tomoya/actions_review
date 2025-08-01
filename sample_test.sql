-- select_active_users.sql

-- usersテーブルから有効なユーザー情報を取得する

-- usersテーブルから、最終ログインが2024年1月1日以降で、
-- かつアカウントが有効（is_active = true）なユーザーの
-- ID、名前、メールアドレスを選択する。
-- 結果はユーザーIDの昇順で並べ替える。

SELECT
    user_id,
    user_name,
    email
FROM
    users
WHERE
    last_login_date >= '2024-01-01'
    AND is_active = TRUE
ORDER BY
    user_id ASC;
