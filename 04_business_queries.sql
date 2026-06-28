USE supply_chain_analytics;

SELECT COUNT(*) AS Total_Orders
FROM orders;

SELECT
SUM(o.quantity * p.unit_price) AS Total_Revenue
FROM orders o
JOIN products p
ON o.product_id = p.product_id;

SELECT
p.product_name,
SUM(o.quantity) AS Total_Sold
FROM orders o
JOIN products p
ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY Total_Sold DESC
LIMIT 10;

SELECT
c.customer_name,
COUNT(o.order_id) AS Total_Orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
ORDER BY Total_Orders DESC
LIMIT 10;

SELECT
w.warehouse_name,
SUM(i.stock_quantity) AS Total_Stock
FROM inventory i
JOIN warehouses w
ON i.warehouse_id = w.warehouse_id
GROUP BY w.warehouse_name
ORDER BY Total_Stock DESC;

SELECT
product_id,
warehouse_id,
stock_quantity
FROM inventory
WHERE stock_quantity < 50
ORDER BY stock_quantity;

SELECT
s.supplier_name,
COUNT(o.order_id) AS Orders_Supplied
FROM suppliers s
JOIN orders o
ON s.supplier_id = o.supplier_id
GROUP BY s.supplier_name
ORDER BY Orders_Supplied DESC;

SELECT
MONTH(order_date) AS Month,
COUNT(*) AS Total_Orders
FROM orders
GROUP BY MONTH(order_date)
ORDER BY Month;

SELECT COUNT(*) AS Delayed_Deliveries
FROM deliveries
WHERE delivery_status='Delayed';

SELECT
delivery_status,
COUNT(*) AS Total
FROM deliveries
GROUP BY delivery_status;

