from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Homepage.html", user=current_user)

@views.route('/start-recycling-categories')
def SRCategories():
    return render_template("SRCategories.html")

@views.route('/forum')
def forum():
    return render_template("Forum.html")

@views.route('/post')
def post():
    return render_template("Post-page.html") 

# CAN BE VIEWED WHEN LOGGED IN
@views.route('/create-post')
@login_required
def CreatePost():
    return render_template("Create-Post.html")

@views.route('/account')
@login_required
def account():
    return render_template("Account.html") 