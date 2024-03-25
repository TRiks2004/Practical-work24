"""
Routes and views for the bottle application.
"""

from bottle import route, view, redirect
from datetime import datetime

@route('/')
@route('/home')
def home():
    return redirect('/about')

@route('/contact')
@view('contact')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/about')
@view('layout')
def about():
    return dict()
