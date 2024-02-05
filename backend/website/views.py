from flask import Blueprint, render_template, request, flash, redirect, url_for,abort, current_app
from flask_login import login_required, current_user
from .models import Post, Discussions, IMG
from . import db
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError
import os

views = Blueprint('views', __name__)

UPLOAD_FOLDER = r'backend\website\static\images\UPLOADED IMG'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    discussions = Discussions.query.all()
    return render_template("Forum.html", user=current_user, discussions=discussions)

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
        elif pic and allowed_file(pic.filename):
            try:
                filename = secure_filename(pic.filename)
                mimetype = pic.mimetype

                # Save the file to the designated folder
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                pic.save(file_path)

                # Save the filename to the database
                new_image = IMG(img_filename=file_path, name=filename, mimetype=mimetype, user_id=current_user.id)
                db.session.add(new_image)
                db.session.commit()

                # Create a new discussion associated with the uploaded image
                new_discussion = Discussions(
                    dTitle=dTitle, 
                    dDescription=dDescription,
                    user_id=current_user.id,
                    image_id=new_image.id
                )
                db.session.add(new_discussion)
                db.session.commit()

                flash('Discussion created!', category='success')
                return redirect(url_for('views.forumClicked'))
            except IntegrityError as e:
                db.session.rollback()
                if 'UNIQUE constraint failed: img.img' in str(e):
                    flash('Image file name is not unique', category='error')
                else:
                    flash('An error occurred during discussion creation', category='error')

    return render_template("Create-Forum.html", user=current_user)


@views.route('/Discussion/<int:discussion_id>')
def forumPost(discussion_id):
    discussion_data = Discussions.query.get(discussion_id)

    if not discussion_data:
        abort(404)

    return render_template("Forum-Clicked.html", user=current_user, discussion_data=discussion_data)


@views.route('/post')
@login_required
def post():
    return render_template("Post-page.html", user=current_user) 

@views.route('/login')
def login():
    return render_template("Login.html", user=current_user)

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

@views.route('/account')
@login_required
def account():
    return render_template("Account.html", user=current_user) 