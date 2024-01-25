from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Homepage.html", user=current_user)

@views.route('/start-recycling-categories')
def SRCategories():
    return render_template("SRCategories.html", user=current_user)


@views.route('/start-recycling-plastic')
def SRPlastic():
    return render_template("SR-Plastic.html", user=current_user)

@views.route('/start-recycling-paper')
def SRPaper():
    return render_template("SR-Paper.html", user=current_user)

@views.route('/start-recycling-textile')
def SRTextile():
    return render_template("SR-Textile.html", user=current_user)

@views.route('/start-recycling-glass')
def SRGlass():
    return render_template("SR-Glass.html", user=current_user)

@views.route('/forum')
def forum():
    return render_template("Forum.html", user=current_user)

@views.route('/forumClicked')
def forumClicked():
    return render_template("Forum-Clicked.html", user=current_user)

@views.route('/post')
def post():
    return render_template("Post-page.html", user=current_user) 

@views.route('/login')
def login():
    return render_template("Login.html", user=current_user)

# CAN BE VIEWED WHEN LOGGED IN
@views.route('/create-post', methods=['GET', 'POST'])
@login_required
def CreatePost():
    if request.method == "POST":
        category = request.form.get('chosenCat')
        title = request.form.get('postTitle')
        description = request.form.get('postDescription')
        materials = request.form.get('postMaterial')
        instruction_title = request.form.get('instructionTitle')
        instruction_description = request.form.get('stepDescription')
        reference = request.form.get('postReference')

        if not category or len(title) == 0 or len(description) == 0 or len(materials) == 0 or len(instruction_title) == 0 or len(instruction_description) == 0 or len(reference) == 0:
            flash('Please fill up all the required forms', category='error')
        #elif len(title) > 16:
        #   flash('Title reached maximum limit of characters', category='error')

#        else:
#            new_post = Post(category=category, title=title)
#            db.session.add(new_post)
#            db.session.commit()
#            flash('Post created!', category='success')


    return render_template("Create-Post.html", user=current_user)

@views.route('/account')
@login_required
def account():
    return render_template("Account.html", user=current_user) 