-- ユーザーとその注文情報を取得するためのSQLクエリ
-- Wiki自動生成のテストに使用します。

/*
 テーブル定義の例
 この部分は実際にDBに存在することを想定しています。
*/
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    registration_date DATE
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- テストデータの挿入例
INSERT INTO users (user_id, user_name, registration_date) VALUES
(1, '田中 太郎', '2023-01-15'),
(2, '鈴木 花子', '2023-02-20');

INSERT INTO orders (order_id, user_id, order_date, amount) VALUES
(101, 1, '2024-03-10', 5000.00),
(102, 2, '2024-03-12', 7500.00),
(103, 1, '2024-04-01', 3200.00);


-- メインのクエリ: 特定のユーザーの注文一覧を取得する
SELECT
    u.user_name,
    o.order_id,
    o.order_date,
    o.amount
FROM
    users u
JOIN
    orders o ON u.user_id = o.user_id
WHERE
    u.user_id = 1
ORDER BY
    o.order_date DESC;