from flask import Flask, render_template
from models import db, Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.sqlite3'
db.init_app(app)

@app.route('/')
def homepage():
    restaurant = Resturant.query.first()
    return render_template('homepage.html', Restaurant=Restaurant)
    