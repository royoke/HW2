## SI 364
## Winter 2018
## HW 2 - Part 1

## This homework has 3 parts, all of which should be completed inside this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask application code below so that the routes described in the README exist and render the templates they are supposed to (all templates provided are inside the templates/ directory, where they should stay).

## As part of the homework, you may also need to add templates (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
import requests
import json
from flask import Flask, request, render_template, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################




####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

@app.route('/artistform', methods = ['GET','POST'])
def artist_form():
	return render_template('artistform.html')

@app.route('/artistinfo', methods = ['GET','POST'])
def artist_info():
	artist = request.args['artist']
	if artist != '':
		baseURL = 'https://itunes.apple.com/search?'
		params = {}
		params['media'] = 'music'
		params['entity'] = 'musicTrack'
		params['term'] = artist
		data = requests.get(baseURL, params=params)
		artist_dict = json.loads(data.text)
		return render_template('artist_info.html', objects=artist_dict['results'])
	flash('An artist name is required!')
	return redirect(url_for('artist_form'))


























if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
