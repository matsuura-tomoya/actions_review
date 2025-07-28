-- 2025年上半期の優良顧客リストを取得するクエリ

-- CTE（共通テーブル式）でまず注文を絞り込む
WITH Orders_CTE AS (
    SELECT
        c.customer_id,
        c.name,
        c.email,
        p.product_id,
        p.category,
        o.order_date,
        oi.quantity * oi.price as total_price
    FROM
        customers c
    JOIN
        orders o ON c.customer_id = o.customer_id
    JOIN
        order_items oi ON o.order_id = oi.order_id
    JOIN
        products p ON oi.product_id = p.product_id
    WHERE
        o.order_date >= '2025-01-01' AND o.order_date < '2025-07-01'
        AND (p.category = 'Electronics' OR p.category = 'Books')
)
-- 最終的な結果を選択
SELECT
    customer_id,
    name,
    email,
    COUNT(product_id) AS number_of_orders
FROM
    Orders_CTE
GROUP BY
    customer_id,
    name,
    email
HAVING
    COUNT(product_id) >= 3
ORDER BY
    number_of_orders DESC,
    customer_id;