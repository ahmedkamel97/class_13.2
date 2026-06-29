"""A tiny Flask message board, built as a class exercise.

Visitors can read posts on the main board and leave their own message.
"""
import os
from datetime import datetime

from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-me')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'board.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    return redirect(url_for('main'))


@app.route('/main')
def main():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('main.html', posts=posts)


@app.route('/post', methods=['POST'])
def post():
    author = request.form.get('author', '').strip() or 'Anonymous'
    message = request.form.get('message', '').strip()
    if message:
        db.session.add(Post(author=author, message=message))
        db.session.commit()
    return redirect(url_for('main'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
