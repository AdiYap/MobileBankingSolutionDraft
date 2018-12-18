"""
Routes and views for the flask application.
"""


from datetime import datetime
from flask import render_template
from MobileBankingSolutionDraft import app

@app.route('/')
@app.route('/home')



def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/transfer')
def transfer():
    """Renders the contact page."""
    return render_template(
        'transfer.html',
    )

@app.route('/bills')
def bills():
    """Renders the about page."""
    return render_template(
        'bills.html',
    )
