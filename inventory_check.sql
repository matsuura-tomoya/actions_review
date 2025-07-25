-- 商品テーブルの定義例
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    stock_quantity INT NOT NULL
);

-- サンプルデータの挿入
INSERT INTO products (product_id, product_name, stock_quantity) VALUES
(101, 'ノートパソコン', 35),
(102, 'ワイヤレスマウス', 150),
(103, 'メカニカルキーボード', 48);


-- 在庫が50個未満の商品をリストアップするクエリ
SELECT
    product_id,
    product_name,
    stock_quantity
FROM
    products
WHERE
    stock_quantity < 50
ORDER BY
    stock_quantity ASC;