#//https://blog.pythonanywhere.com/158/
#from app import db, User
#from werkzeug.security import generate_password_hash
#admin = User(username="admin", password_hash=generate_password_hash("new-secret"))
#db.session.add(admin)
#bob = User(username="bob", password_hash=generate_password_hash("super-secret"))
#db.session.add(bob)
#caroline = User(username="caroline", password_hash=generate_password_hash("8fwe5jYCE98lXl0ZovYW"))
#db.session.add(caroline)
#db.session.commit()
#
#
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, LoginManager, logout_user, UserMixin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="sammy",
    password="password",
    hostname="localhost",
    databasename="comment",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = "SOMETHING RANDOM"
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password_hash = db.Column(db.String(162))

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()


class Comment(db.Model):

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    posted = db.Column(db.DateTime, default=datetime.now)
    commenter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    commenter = db.relationship('User', foreign_keys=commenter_id)


@app.route("/", methods=["GET", "POST"])
def index():
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.filter_by(commenter_id=current_user.id))

    #comment = Comment(content=request.form["contents"], commenter=current_user)
    #db.session.add(comment)
    #db.session.commit()
    return redirect(url_for('index'))



@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_page.html", error=False)

    user = load_user(request.form["username"])
    if user is None:
        return render_template("login_page.html", error=True)

    if not user.check_password(request.form["password"]):
        return render_template("login_page.html", error=True)

    login_user(user)
    return redirect(url_for('index'))



@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))