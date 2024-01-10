from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Homepage.html")

@views.route('/start-recycling-categories')
def SRCategories():
    return render_template("SRCategories.html")

@views.route('/create-post')
def CreatePost():
    return render_template("Create-Post.html")

@views.route('/forum')
def forum():
    return render_template("Forum.html")

@views.route('/post')
def post():
    return render_template("Post-page.html")