
from flask import Flask,render_template,request,redirect,url_for,make_response,abort
from werkzeug.routing import BaseConverter
from werkzeug.utils import secure_filename
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)

moment =Moment(app)
manager = Manager(app)

Bootstrap(app)

nav = Nav()

nav.register_element('top', Navbar('Flask',
                                  View('home','index'),
                                  View('home', 'index'),
                                  View('home', 'index'),
                                  View('home', 'index'),
                                  ))
nav.init_app(app)

@app.route('/')
def index():
    return render_template('index.html', title='Welcome to python world')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']


    return render_template('login.html',method=request.method)
@app.route('/service')
def service():
    return 'Service'

@app.route('/about')
def about():
    return 'About'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404


@app.route('/user/<username>')
def username(username):
    return render_template('user.html', username=username)
@app.route('/moment')
def moment_time():
    return render_template('index.htm',currenr_time= datetime.utcnow())

@manager.command
def dev():
    from livereload import Server
    live_server = Server(app.wsgi_app)
    live_server.watch("*", "*.*")
    live_server.serve(open_url=True)

if __name__ == '__main__':
    #manager.run()
   app.run(debug=True)
