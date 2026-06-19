from flask import Flask, render_template,request,redirect,url_for,flash,session
from database import get_products, get_stock,get_sales,insert_products,insert_sales,insert_stock,check_available_stock,check_user_exists,create_user,sales_per_day,sales_per_product,profit_per_day,profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps 

app = Flask(__name__)
app.secret_key = 'Gfghjk'


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    
    return  render_template('index.html')

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected


@app.route('/products')
@login_required
def products():

    products_data = get_products()
    return render_template('products.html',products_data=products_data)
    
    
@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method == 'POST':
        product_name = request.form['p_name']
        buying_price = request.form['b_price']
        selling_price = request.form['s_price']
  

        new_product = (product_name,buying_price,selling_price)
        insert_products(new_product)
        flash("product added succeccfully",'success')
    return redirect(url_for('products'))


@app.route('/sales')
@login_required
def sales():
    sales_data = get_sales()
    return  render_template("sales.html",sales_data = sales_data)

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method == 'POST':
       sales_id = request.form['sales_id']
       product_id= request.form['p_id']
       quantity = request.form['quantity']
       created_at = request.form['c_at']

       new_sales = (sales_id,product_id,quantity, created_at )
       insert_products(new_sales)
       print("sales added succeccfully")
    return redirect(url_for('sales'))


@app.route('/make_sale',methods=['GET','POST'])
def make_sale():
    if request.method == 'POST':
        pid = request.form['pid']
        quantity = request.form['quantity']

        new_sale = (pid,quantity)
        available_stock = check_available_stock(pid)

        if available_stock < float(quantity):
            flash("Insufficient stock to complete sale",'danger')
            return redirect(url_for('sales'))

        insert_sales(new_sale)
        flash("Sale added successfully",'success')
    return redirect(url_for('sales'))



@app.route('/stock')
@login_required
def stock():
    stock_data = get_stock()
    return  render_template("stock.html",stock_data = stock_data)



@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method == 'POST':
       stock_id = request.form['stock_id']
       product_id= request.form['p_id']
       stock_quantity = request.form['stock_quantity']
       created_at = request.form['c_at']

       new_stock = (stock_id,product_id,stock_quantity, created_at )
       insert_products(new_stock)
       print("stock added succeccfully")
    return redirect(url_for('stock'))

#@app.route('/stock')
#def stock_remaining():
    #stock_remaining = check_available_stock
    #return  render_template("stock.html", stock_remaining =  stock_remaining)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone']
        password = request.form['password']

        existing_user = check_user_exists(email)
        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,email,phone_number,hashed_password)
            create_user(new_user)
            flash("User created successfully",'success')
            return redirect(url_for('login'))
        else:
            flash("User already exists,please login instead",'danger')
        
    return render_template('register.html')



@app.route('/dashboard')
@login_required
def dashboard():
    product_sales = sales_per_product()
    product_profit = profit_per_product()

    daily_sales = sales_per_day()
    daily_profit = profit_per_day
#product data
    product_names = [i[0] for i in product_sales]
    prod_profit  = [float(i[1]) for i in product_profit]
    product_sales = [float(i[1]) for i in product_sales]
#days data
    dates = [str(i[0]) for i in daily_sales]
    day_sales = [float(i[1]) for i in daily_sales]
    daily_profit = [float(i[1]) for i in daily_profit]

    return  render_template("dashboard.html")
    product_names  = product_names,prod_profit = prod_profit, product_sales = product_sales
    dates =dates, day_sales =day_sales,day_profit = day_profit

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user_exists(email)
        if not registered_user:
            flash("User doesn't exist,please register",'danger')
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                session['email'] = email
                flash("Login successful",'success')
                return redirect(url_for('dashboard'))
            else:
                flash("Incorrect password,try again",'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("@logged out successfully",'success')
    return redirect(url_for('login'))

app.run(debug=True)