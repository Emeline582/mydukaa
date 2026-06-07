Write sql queries that fetch the following data: -> sales_per_day => sales , date sales = revenue -> profit_per_day -> sales_per_product -> profit_per_product

15000 * 3 = 45000 (quantity , selling_price , date)

sales per day select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as total_sales from sales join products on products.id = sales.pid group by date;

profit per day select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price - products.buying_price)) as total_sales from sales join products on products.id = sales.pid group by date;

sales per product select products.name as p_name , sum(sales.quantity * products.selling_price) as total_sales from products join sales on sales.pid = products.id group by p_name;

profit per product select products.name as p_name , sum(sales.quantity *( products.selling_price - products.buying_price)) as total_sales from products join sales on sales.pid = products.id group by p_name;