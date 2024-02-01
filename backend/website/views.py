from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, Discussions, IMG
from . import db
from werkzeug.utils import secure_filename
import os
from sqlalchemy.exc import IntegrityError

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

@views.route('/createForum', methods=['GET', 'POST'])
@login_required
def forumClicked():
    if request.method == "POST":
        dTitle = request.form.get('discussionTitle')
        dDescription = request.form.get('discussionDescription')
        pic = request.files['pic']

        if not all([dTitle, dDescription]):
            flash('Please fill up all the required forms', category='error')
        elif len(dTitle) > 70:
            flash('Title reached maximum limit of characters', category='error')
        else:
            try:
                filename = secure_filename(pic.filename)
                mimetype = pic.mimetype
                img = IMG(img=pic.read(), mimetype=mimetype, name=filename)
                new_discussion = Discussions(dTitle=dTitle, dDescription=dDescription)
                db.session.add(img)
                db.session.add(new_discussion)
                db.session.commit()
                flash('Discussion created!', category='success')
            except IntegrityError as e:
                db.session.rollback()  # Rollback the transaction to avoid leaving the database in an inconsistent state
                if 'UNIQUE constraint failed: img.img' in str(e):
                    flash('Image file name is not unique', category='error')
                else:
                    flash('An error occurred during discussion creation', category='error')
    
    return render_template("Create-Forum.html", user=current_user)

@views.route('/Discussion')
def forumPost():
    return render_template("Forum-Clicked.html", user=current_user)

@views.route('/post')
@login_required
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
        instruction_title = request.form.get('instructionTitle')
        instruction_description = request.form.get('stepDescription')
        reference = request.form.getlist('references[]')
        print("Received references:", reference)
        image = request.files.get('instructionImage')
        image_filename = save_image(image)

        if not all([category, title, description, instruction_title, instruction_description, reference]):
            flash('Please fill up all the required forms', category='error')
        elif len(title) > 70:
            flash('Title reached maximum limit of characters', category='error')
        elif len(instruction_title) > 70:
            flash('Instruction title reached maximum limit of characters', category='error')

        else:
            new_post = Post(
                category=category, 
                title=title,
                description=description,
                instruction_title=instruction_title,
                instruction_description=instruction_description,
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