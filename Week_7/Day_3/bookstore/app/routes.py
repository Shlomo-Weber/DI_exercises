from app import app
from flask import Flask
from flask import render_template
from app.models import Book, Author
import requests
from app.forms import AddBook
from app import db
from flask import flash, redirect, url_for


@app.route('/')
def index():
    all_books = Book.query.all()
    authors = Author.query.all()
    return render_template('index.html', books=all_books, authors = authors)

@app.route('/author/<name>')
def author(name):
    books = Author.query.get(name = name).books.all()

    return render_template('author.html', books=books, author=name)

@app.route('/add', methods = ['GET', 'POST'])
def addbook():
    form = AddBook()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        price = form.price.data
        pub_date = form.pub_date.data

        if title.lower() in [book.title.lower() for book in Book.query.all()]:
            flash('This book already exists in the store')
            return redirect('addbook')

        if author.lower() in [auth.name.lower() for auth in Author.query.all()]:
            author = Author.query.filter_by(name=author)
        else:
            author = Author(name=author)
            db.session.add(author)

        book = Book(title=title, author=author, price=price, pub_date=pub_date)
        db.session.add(book)
        db.session.commit()
        flash (f'{title} successfully added to the store')
        return redirect('index')

    return render_template('addbook.html', form = form)