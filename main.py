from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Configure CKEditor for rich text editing
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_CONFIG'] = {'versionCheck': False}
ckeditor = CKEditor(app)

# Set secret key for Flask application (used for forms and sessions)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize Bootstrap for improved UI
Bootstrap5(app)

# Database configuration and initialization
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'  # SQLite database for storing blog posts
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define a form for creating and editing blog posts
class BlogForm(FlaskForm):
    title = StringField("Blog title", validators=[DataRequired()])  # Title of the blog post
    subtitle = StringField("Subtitle", validators=[DataRequired()])  # Subtitle of the blog post
    author_name = StringField("Author's name", validators=[DataRequired()])  # Author's name
    background_url = StringField("Background url", validators=[DataRequired(), URL()])  # Background image URL
    body = CKEditorField('Body', validators=[DataRequired()])  # Main content of the blog post
    submit = SubmitField("Submit")  # Submit button

# Define the BlogPost model for the database
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)  # Unique ID for each blog post
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)  # Title of the post
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)  # Subtitle of the post
    date: Mapped[str] = mapped_column(String(250), nullable=False)  # Date of creation
    body: Mapped[str] = mapped_column(Text, nullable=False)  # Content of the post
    author: Mapped[str] = mapped_column(String(250), nullable=False)  # Author's name
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)  # URL for the background image

# Create all database tables
with app.app_context():
    db.create_all()

# Route for displaying all blog posts
@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()  # Retrieve all blog posts from the database
    return render_template("index.html", all_posts=posts)

# Route for displaying a single blog post by ID
@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)  # Retrieve post by ID or return 404 if not found
    return render_template("post.html", post=requested_post)

# Route for creating a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def add_new_post():
    form = BlogForm()
    if form.validate_on_submit():  # Validate form submission
        new_post = BlogPost(
            date=date.today().strftime("%B %d, %Y"),  # Set current date
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.author_name.data,
            img_url=form.background_url.data,
            body=form.body.data,
        )
        db.session.add(new_post)  # Add new post to the database
        db.session.commit()  # Save changes
        return redirect(url_for('get_all_posts'))  # Redirect to homepage
    return render_template("make-post.html", form=form, edit=0)  # Render form for new post

# Route for editing an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)  # Retrieve post by ID or return 404 if not found
    form = BlogForm(
        title=post.title,
        subtitle=post.subtitle,
        author_name=post.author,
        background_url=post.img_url,
        body=post.body,
    )
    if form.validate_on_submit():  # Validate form submission
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author_name.data
        post.img_url = form.background_url.data
        post.body = form.body.data
        db.session.commit()  # Save changes
        return redirect(url_for("show_post", post_id=post.id))  # Redirect to updated post
    return render_template("make-post.html", form=form, edit=1)  # Render form for editing

# Route for deleting a blog post
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)  # Retrieve post by ID or return 404 if not found
    try:
        db.session.delete(post)  # Delete the post from the database
        db.session.commit()  # Save changes
    except Exception as e:
        print(f"Error {e}")  # Log error
        db.session.rollback()  # Rollback changes on error
    return redirect(url_for("get_all_posts"))  # Redirect to homepage

# Route for "About" page
@app.route("/about")
def about():
    return render_template("about.html")

# Route for "Contact" page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Run the application in debug mode on port 5003
if __name__ == "__main__":
    app.run(debug=True, port=5003)
