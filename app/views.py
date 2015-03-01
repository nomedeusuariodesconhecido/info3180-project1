"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Required, Email
from wtforms.fields import TextField
from app import db
from app.models import Profile


class CreateProfileForm(Form):
    first_name = TextField('First Name', validators=[Required()])
    last_name = TextField('Last Name', validators=[Required()])
    image = TextField('Image', validators=[Required(), Email()])





###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
  
  

@app.route('/profile/', methods=['POST', 'GET'])
def add_profile():
  form = CreateProfileForm()
  if request.method == "POST":
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return "{} {} this was a post".format(first_name, last_name)
  return render_template('add_profile.html', form=form)

@app.route('/profiles/')
def list_all_profiles():
  return "List All Profiles"

@app.route('/profile/<int:id>')
def display_profile():
  return "profile {}".format(id)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
