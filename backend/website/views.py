from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
from . import db
import os

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

        if len(category) == 0 or len(title) == 0:
            flash('Please fill up all the required forms', category='error')
        elif len(title) > 70:
            flash('Title reached maximum limit of characters', category='error')

        else:
            new_post = Post(
                category=category, 
                title=title,
                user_id=current_user.id)
            db.session.add(new_post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.CreatePost'))

    return render_template("Create-Post.html", user=current_user)

def save_image(image):
    if image:
        image_name = image.filename
        image_path = os.path.join('backend/website/static/uploaded', image_name)  # Adjust the path as needed
        image.save(image_path)
        return image_name 
    return None

@views.route('/account')
@login_required
def account():
    return render_template("Account.html", user=current_user) 