import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='Emmy3986',dbname='mydukaa')

cur = conn.cursor()

cur.execute("select * from products")
products_data = cur.fetchall()
# print(products_data)

cur.execute("select * from sales")
sales_data = cur.fetchall()
# print(sales_data)

#cur.execute("insert into products(name,buying_price,selling_price)values('eraser',35,70)")
#insert_products(values):
#conn.commit()

def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data


def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

def insert_products(values):
    cur.execute(f"insert into products(name,buying_price, selling_price)values{values}")
    conn.commit()

# product1 = ('shoes',2000,2500)
# product2 = ('phone',10000,15000)
# insert_products(product1)
# insert_products(product2)



#def insert_products2(values):
    #cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)", values)
    #conn.commit()

#product3 = ('laptop',40000,50000)
#insert_products2(product3)

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)", values)
    conn.commit()

#sales1=(1,200)
#sales2=(2,250)


def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data


def insert_stock(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    conn.commit()

#stock1=(1,400)
#stock2=(2,800)


def get_stock():
    cur.execute("select * from stock")
    stock_data = cur.fetchall()
    return stock_data

def check_available_stock(pid):
    cur.execute("select sum (stock_quantity) from stock where pid=%s",(pid))
    total_stock = cur.fetchone()[0] or 0

    cur.execute("select sum(sales].quantity) from sales where pid = %s",(pid))
    total_sold = cur.fetchone()[0] or 0

    return total_stock-total_sold

def check_user_exists(email):
    cur.execute("select * from users where email=%s ",(email, ))
    user= cur.fetchone()
    return user

def create_user(user_details):
    cur.execute("insert into users(full_name,email,phone_number,password)values(%s,%s,%s,%s)",user_details)
    conn.commit()

def sales_per_day():
    cur.execute("""
      select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as
      total_sales from sales join products on products.id = sales.pid  group by date;
    """)
    daily_sales = cur.fetchall()
    return daily_sales
def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price -
        products.buying_price)) as total_sales from sales join products on products.id = sales.pid
         group by date;
    
    """)
    daily_profit = cur.fetchall()
    return daily_profit



def sales_per_product():
    cur.execute("""
        select products.name as p_name , sum(sales.quantity * products.selling_price)  as total_sales
        from products join sales on sales.pid = products.id group by p_name;
    """)
    product_sales = cur.fetchall()
    return product_sales


def profit_per_product():
    cur.execute("""
        select products.name as p_name , sum(sales.quantity *( products.selling_price - 
        products.buying_price))  as total_sales from products join sales on sales.pid = products.id group by p_name;
    """)
    product_profit = cur.fetchall()
    return product_profit
