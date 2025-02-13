from flask import Flask, flash, render_template, request, redirect, url_for, g, session
import sqlite3
import re
from datetime import datetime, timedelta, timezone
app = Flask(__name__)

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("unclecock.db")
        db.row_factory = sqlite3.Row
    return db

@app.route('/' , methods = ["GET", "POST"])
def initialize():
    session.clear()
    return redirect(url_for('home'))

@app.route('/home', methods = ["GET", "POST"])
def home():
    return render_template("home.html")

#---------播放頁面------------
@app.route('/play1',methods=['GET','POST'])
def play1():
    return render_template("play1.html")

@app.route('/play2',methods=['GET','POST'])
def play2():
    return render_template("play2.html")

@app.route('/play3',methods=['GET','POST'])
def play3():
    return render_template("play3.html")

@app.route('/play4',methods=['GET','POST'])
def play4():
    return render_template("play4.html")

@app.route('/play5',methods=['GET','POST'])
def play5():
    return render_template("play5.html")
#----------------------------

@app.route('/product1',methods=['GET','POST'])
def product1():
    return render_template("product1.html")

@app.route('/product2',methods=['GET','POST'])
def product2():
    return render_template("product2.html")

@app.route('/product3',methods=['GET','POST'])
def product3():
    return render_template("product3.html")

@app.route('/product4',methods=['GET','POST'])
def product4():
    return render_template("product4.html")

@app.route('/product5',methods=['GET','POST'])
def product5():
    return render_template("product5.html")

@app.route('/allproducts',methods=['GET','POST'])
def allproducts():
    return render_template("allproducts.html")

@app.route('/cart',methods=['GET','POST'])
def cart():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item1, item2, item3, item4, item5 FROM Carts WHERE username=?", (username,)).fetchone()
    item1 = False
    item2 = False
    item3 = False
    item4 = False
    item5 = False
    num = 0
    sum = 0
    if(tmp[0] == 1): 
        item1 = True
        num += 1
        sum += 999
    if(tmp[1] == 1): 
        item2 = True
        num += 1
        sum += 189
    if(tmp[2] == 1): 
        item3 = True
        num += 1
        sum += 139
    if(tmp[3] == 1): 
        item4 = True
        num += 1
        sum += 709
    if(tmp[4] == 1): 
        item5 = True
        num += 1
        sum += 289
    session["sum"] = sum
    return render_template("cart.html", num = num, item1 = item1, item2 = item2, item3 = item3, item4 = item4, item5 = item5, sum = sum)

@app.route('/register',methods=['GET','POST'])
def register():
    return render_template("register.html")

@app.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route('/egg',methods=['GET','POST'])
def egg():
    return render_template("egg.html")


@app.route('/logout',methods=['GET','POST'])
def logout(): 
    session.clear()
    flash("已登出","success")
    return redirect(url_for('home'))


@app.route('/info',methods=['GET','POST'])
def info(): 
    
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    else:
        username = str(session.get('username'))
        db_1 = get_db()
        cursor = db_1.cursor()
        tmp = cursor.execute("SELECT * FROM Purchased WHERE username=?", (username,)).fetchone()
        items = [False] * (len(tmp)+1)
        for i,element in enumerate(tmp):
            if element==1:
                items[i]=True
        return render_template("person.html",item1=items[1],item2=items[2],item3=items[3],item4=items[4],item5=items[5])

#------購買品項----------
@app.route('/go_item1',methods=['GET','POST'])
def go_item1():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item1 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item1 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item1=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('cart'))
    
@app.route('/go_item2',methods=['GET','POST'])
def go_item2():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item2 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item2 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item2=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('cart'))

@app.route('/go_item3',methods=['GET','POST'])
def go_item3():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item3 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item3 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item3=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('cart'))

@app.route('/go_item4',methods=['GET','POST'])
def go_item4():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item4 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item4 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item4=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('cart'))

@app.route('/go_item5',methods=['GET','POST'])
def go_item5():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item5 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item5 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item5=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('cart'))
#-------------------------------------------

#------加入品項----------
@app.route('/add_item1',methods=['GET','POST'])
def add_item1():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item1 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item1 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item1=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('allproducts'))
    
@app.route('/add_item2',methods=['GET','POST'])
def add_item2():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item2 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item2 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item2=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('allproducts'))

@app.route('/add_item3',methods=['GET','POST'])
def add_item3():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item3 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item3 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item3=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('allproducts'))

@app.route('/add_item4',methods=['GET','POST'])
def add_item4():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item4 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item4 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item4=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('allproducts'))

@app.route('/add_item5',methods=['GET','POST'])
def add_item5():
    if session.get('username') == None:
        flash("請先登入","error")
        return redirect(url_for('login'))
    
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item5 FROM Purchased WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("您已擁有此商品","error")
            return redirect(url_for('allproducts'))
    tmp = cursor.execute("SELECT item5 FROM Carts WHERE username=?", (username,)).fetchone()
    for i in tmp:
        if i == 1:
            flash("此商品已在購物車中","error")
            return redirect(url_for('allproducts'))
    
    cursor.execute("UPDATE Carts SET item5=1 WHERE username = ?;", (username,))
    db_1.commit()
    flash("已加入購物車","success")
    return redirect(url_for('allproducts'))
#-------------------------------------------

#--------刪除物品----------
@app.route('/delete_item1',methods=['GET','POST'])
def delete_item1():
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    cursor.execute("UPDATE Carts SET item1=0 WHERE username = ?;", (username,))
    db_1.commit()
    flash("刪除成功","success")
    return redirect(url_for('cart'))

@app.route('/delete_item2',methods=['GET','POST'])
def delete_item2():
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    cursor.execute("UPDATE Carts SET item2=0 WHERE username = ?;", (username,))
    db_1.commit()
    flash("刪除成功","success")
    return redirect(url_for('cart'))

@app.route('/delete_item3',methods=['GET','POST'])
def delete_item3():
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    cursor.execute("UPDATE Carts SET item3=0 WHERE username = ?;", (username,))
    db_1.commit()
    flash("刪除成功","success")
    return redirect(url_for('cart'))

@app.route('/delete_item4',methods=['GET','POST'])
def delete_item4():
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    cursor.execute("UPDATE Carts SET item4=0 WHERE username = ?;", (username,))
    db_1.commit()
    flash("刪除成功","success")
    return redirect(url_for('cart'))

@app.route('/delete_item5',methods=['GET','POST'])
def delete_item5():
    username = str(session.get('username'))
    db_1 = get_db()
    cursor = db_1.cursor()
    cursor.execute("UPDATE Carts SET item5=0 WHERE username = ?;", (username,))
    db_1.commit()
    flash("刪除成功","success")
    return redirect(url_for('cart'))
#-------------------------

@app.route("/login_submit", methods=["GET", "POST"])
def login_submit():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        db_1 = get_db()
        cursor = db_1.cursor()
        user = cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (name, password)).fetchone()
        if user:
            cursor.execute("UPDATE Users SET logindate=? WHERE username=?", (str(datetime.now(timezone(timedelta(hours=+8))))[0:19], name))
            user = cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (name, password)).fetchone()
            print(str(datetime.now(timezone(timedelta(hours=+8))))[0:19])
            session["username"] = name
            session['email']=user['email']
            session['registerdate']=user['registerdate']
            session['logindate']=user['logindate']
            db_1.commit()           
            flash("成功登入, 歡迎🐔"+name, 'success')
            return redirect(url_for('home'))
        else:
            if cursor.execute("SELECT * FROM Users WHERE username=?", (name,)).fetchone():
                flash("密碼錯誤", 'error')
                return redirect(url_for('login'))
            else:
                flash("使用者不存在 請註冊", 'error')
                return redirect(url_for('login'))
    
    return redirect(url_for('login'))

def validate_card_number(card_number, selected_card):
#* Visa: 匹配以 4 开头,共 13 位或 16 位的卡号。
#* Mastercard: 保持不变,以 51-55 开头,共 16 位。
#* UnionPay: 匹配以 62 开头,共 16-19 位的卡号。
#* JCB: 匹配以 3528-3589 开头,共 16-19 位的卡号。
    visa_pattern = r'^4\d{12}(\d{3})?$'
    mastercard_pattern = r'^5[1-5]\d{14}$'
    unionpay_pattern = r'^62\d{14,17}$'
    jcb_pattern = r'^35(28|29|[3-8]\d)\d{12}(\d{2,3})?$'

    if selected_card.endswith('visa.png'):
        return bool(re.match(visa_pattern, card_number))
    elif selected_card.endswith('mastercard.jpg'):
        return bool(re.match(mastercard_pattern, card_number))
    elif selected_card.endswith('UnionPay.png'):
        return bool(re.match(unionpay_pattern, card_number))
    elif selected_card.endswith('jcb.png'):
        return bool(re.match(jcb_pattern, card_number))
    else:
        return False

@app.route('/purchase',methods=['GET','POST'])
def purchase():
    username = str(session.get('username'))
    selected_card = request.form.get('selected_card')
    cardnumber = request.form.get('card-number')
    expiration = request.form.get('expiration')
    cvv = request.form.get('cvv')
    if session.get('sum') == 0:
        flash("購物車中沒有任何物品", 'error')
        return redirect(url_for('cart'))
    if not selected_card:
        flash("請選擇一種支付方式", 'error')
        return redirect(url_for('cart'))
    if not validate_card_number(cardnumber, selected_card):
        flash("無效的信用卡卡號", 'error')
        return redirect(url_for('cart'))
    expiration_pattern = r'^(0[1-9]|1[0-2])\/\d{2}$'
    if not re.match(expiration_pattern, expiration):
        flash("無效的expiration", 'error')
        return redirect(url_for('cart'))
    cvv_pattern=r'^(\d{3}|\d{4})$'
    if not re.match(cvv_pattern, cvv):
        flash("無效的cvv", 'error')
        return redirect(url_for('cart'))
    db_1 = get_db()
    cursor = db_1.cursor()
    tmp = cursor.execute("SELECT item1, item2, item3, item4, item5 FROM Carts WHERE username=?", (username,)).fetchone()
    for i,element in enumerate(tmp,start=1):
        if element==1:
            cursor.execute(f"UPDATE Purchased SET item{i}=1 WHERE username=?", (username,))
            cursor.execute(f"UPDATE Carts SET item{i}=0 WHERE username=?", (username,))
            db_1.commit()
    flash("購買成功", 'success')
    return redirect(url_for('home'))



@app.route("/register_submit", methods=["GET", "POST"])
def register_submit():
    if request.method=="POST":
        name = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        db_1=get_db()
        cursor=db_1.cursor()
        user=cursor.execute("SELECT * FROM Users WHERE username=?", (name,)).fetchone()
        err=""
        err_con=False
        if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9-]*$', name):
            err=err+"使用者名稱僅允許輸入 a-Z、0-9 以及 - 號 (非首位字元)"
            err_con=True
        if len(password) <= 8 or not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char in '@$!%*?&' for char in password):
            err=err+"密碼必須超過8個字元且包含英文大小寫和特殊字元 "
            err_con=True

        if not re.match(r"[^@]+@[^@]+.[^@]+", email) or "gmail.com" not in email:
            err=err+"電子郵件需須滿足XXX@gmail.com"
            err_con=True

        if err_con==True:
            flash(err, 'error')
            return redirect(url_for('register'))
        

        if user!=None:
            flash("此名稱已被使用", 'error')
            return redirect(url_for('register'))
        else:
            cursor.execute('INSERT INTO Users VALUES (?, ?, ?, ?, ?)', (name, email, password,str(datetime.now(timezone(timedelta(hours=+8))))[0:19],"0"))
            cursor.execute('INSERT INTO Carts VALUES (?, ?, ?, ?, ?, ?)', (name, 0, 0, 0, 0, 0))
            cursor.execute('INSERT INTO Purchased VALUES (?, ?, ?, ?, ?, ?)', (name, 0, 0, 0, 0, 0))
            db_1.commit()
            flash("已成功註冊", 'success')
            return redirect(url_for('login'))
    return redirect(url_for('register'))


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.secret_key = 'password'
    app.run(port=6012)
