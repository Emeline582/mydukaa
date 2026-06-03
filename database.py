import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='Emmy3986',dbname='mydukaa')

cur = conn.cursor()

cur.execute("select * from products")
products_data = cur.fetchall()
print(products_data)

cur.execute("select * from sales")
sales_data = cur.fetchall()
print(sales_data)

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


def get_data(table):
    cur.execute(f"select * from {table}")
    data = cur.fetchall()
    return data

def insert_products(values):
    cur.execute(f"insert into products(name,buying_price, selling_price)values{values}")
    conn.commit()

product1 = ('shoes',2000,2500)
product2 = ('phone',10000,15000)
#insert_products(product1)
#insert_products(product2)
print(products_data)


def insert_products2(values):
    cur.execute("insert into products(name,buying_price,selling_price)values(%s,%s,%s)", values)
    conn.commit()

product3 = ('laptop',40000,50000)
insert_products2(product3)

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)", values)
    conn.commit()

sales1=(1,200)
sales2=(2,250)

insert_sales(sales1)
insert_sales(sales2)

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

def insert_stock(values):
    cur.execute(f"insert into stock(pid,stock_quantity)values{values}")
    conn.commit()

stock1=(1,400)
stock2=(2,800)

insert_stock(stock1)
insert_stock(stock2)

def get_stock():
    cur.execute("select * from stock")
    stock_data = cur.fetchall()
    return stock_data