from flask import Flask , render_template , request , flash,redirect
from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()
DB_NAME = "database.db"


app = Flask(__name__)
app.secret_key = "secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

@app.route("/login" ,methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(email, password)
    return render_template("login.html")

@app.route("/signup" , methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        name = request.form.get("name")

        if len(email) < 4:
            flash('Email must be at least 4 characters' , category='error')
        elif len(name) < 2:
            flash('Name must be at least 2 characters' , category='error')
        elif password2 != password:
            flash('both passwords must match' , category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters' , category='error')
        else:
            #create a new account
            flash('Account Created!' , category='success')
            time.sleep(1)
            return redirect('login')

        
    return render_template("signup.html")

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)