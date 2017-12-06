# Flask Web Development
## Creating an Anaconda Virtual environment


Conda allows us to create virtual environments: Python installations that are isolated from other installations. This allows us to have environments with different versions of packages or event different versions of Python.

I'm assuming you are in a bash shell, either on a Mac or Linux machine or using the bash shell in the Git for Windows package.

Open a bash terminal on your computer and type the following:

```bash
which conda
```

You should see something like this:

```bash
/Users/brian/anaconda/bin/conda
```

If you don't see this, then `conda` is not in your Path and your installation is not complete.

### Create a Virtual Environment

In your terminal, type

```bash
conda info -e
```

This provides *information (info)* on the *environments (-e)* you have created. If you have not created any virtual environments, you should only see a root environment.

In your terminal, type

```bash
conda create -n flask_demo python=3.5 flask
```

What is this command doing?

* `-n flask_demo`: This is providing the name for our environment.
* `python=3.5`: this is specifying which version of Python to use. The Anaconda installation has multiple versions of Python available.
* `flask`: Anaconda has a list of formulas for different Python applications.
  * `jupyter` will install the minimum packages needed to run Jupyter
  * `scikit-learn` will install the minimum packages need to use the machine learning package Scikit-learn
  * `flask` will create the minimum requirements for running flask


In your terminal type

```bash
which python
```

You should see something like this:

```
/Users/brian/anaconda/bin/python
```

This is the root Python for your Anaconda distribution. We want to use the Python in the new `flask_demo` environment we created.

In your terminal type

```bash
source activate flask_demo
```
You should now see something like the following:

```bash
(flask_demo) powderkeg:LectureMaterials brian$
```

The `(flask_demo)` indicates we are now in the `flask_demo` virtual environment. If we now type `which python`, we should see that the version of Python in our path is now found in `flask_demo`

```bash
$ which python
/Users/brian/anaconda/envs/flask_demo/bin/python
```
To exit the virtual environment type

```bash
source deactivate
```

## Cloning repository

* We are going to explore the Flask appliation described in  *Flask Web Development* by Miguel Grinberg
* The code for the book can be obtained from github
    * https://github.com/miguelgrinberg/flasky.
* A very nice aspect of this code is that there are different *tags*, so you can check out different versions of the project as it progresses

In your terminal, `cd` to a directory where you would like the repository to be located.

I generally create a directory under my home directory named `Code` where I put all of my (surprise) code.

Clone the `flasky` repository.

```bash
git clone https://github.com/miguelgrinberg/flasky.git
```

## Checking out various versions (tags) of the code

A nice feature of this repository is that there are different `tags` corresponding to
* ``git tag`` (lists all the tags in the repository)
* ``git checkout 2b`` (checks out the code corresponding to tag 2b
* ``git checkout .`` (discard all local changes)

## Why Web Applications?

Web applications are an important means of interacting with users. They also nicely integrate many of the topics we have covered. In fact, the code for web application will look very similar to code that we have already written:

* Dictionaries will be used to pass variables to and from web-pages
* Functions will handle events
* classes will be defined and mapped to databases
* etc.

### Basic Anatomy of a Web App

* Client makes request
* Server determines how to respond to request
* Model is updated by request
* User is directed/redirected to the next/new/same url  (view).


>Clients such as web browsers send requests to the web server, which in turn sends them to the Flask application instance. The application instance needs to know what code needs to run for each URL requested, so it keeps a mapping of URLs to Python functions. The association between a URL and the function that handles it is called a *route.* (*Flask Web Development,* p. 8)

## Why Flask?

Flask is a simple Python web framework that allows you to create a simple web app with a single file or create very complex website. [Here](http://flask.pocoo.org/community/poweredby/) is a list of various websites built with Flask. The chief data scientist for the New York Times has praised Flask as indispensable for the NYT's mission.


## Flask Design Philosophy

* Keep the core simple
* Add functionality with extensions

## Clone the GitHub repository associated with *Flask Web Development* by Miguel Grinberg
```
git clone https://github.com/miguelgrinberg/flasky.git
```
###  cd to ``flasky`` and checkout tag 2a
```
cd flasky
git checkout 2a
```

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
```

This code is missing a vital component: nothing is executed. I think this is sabotage to get you to buy the book!

We need to add the following to the end of the file:

```python
if __name__ == '__main__':
    app.run(debug=True)
```
### We can run ``hello.py`` in pyCharm
* Open ``hello.py`` in pyCharm
* run the program
* Open web browser to ``localhost:5000`` or ``127.0.0.1:5000``

### Decorators in Python

* Decorators were introduced in Python version 2.4
* They are used in Flask to describe how we handle web addresses
  * A Decorator takes a web address (relative to the site root address) and connects that path with a particular function that will **handle** that address.
* Remember decorators are functions that modify functions
#### [Useful blog about decorators in Python](https://pythonconquerstheuniverse.wordpress.com/2012/04/29/python-decorators/)


Now stash or discard your changes and checkout version 2c.

### Fancier program
* ``git checkout 2c``

### Analysis of ``hello.py``
```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    manager.run()

```

#### Code Highlights
* ``__name__`` is the name we discussed in conjunction with modules.
    * If we are using the file as an executable program (not importing it as a module) then ``__name__`` is equal to ``__main__``
* ``@app.route("/")`` This is how we specify web addresses on our site
* with each web address we provide a function that **handles** the selection of that web page (event)

Try running the application now:

```bash
python hello.py
```
You should get an error message:


```python
ImportError: No module named 'flask_script'
```

### Extending Flask

As compared to [django](https://www.djangoproject.com/), Flask is a very minimalist package that assumes you will use additional packages to provide needed functionality when desired.

>Flask is designed to be extended. It intentionally stays out of areas of important functionality such as database and user authentication, giving you the freedom to select the packages that fit your application the best, or to write your own if you so desire. (*Flask Web Development*)

* While Flask is part of Anaconda, Flask extensions are not so install them with ``pip``. In the terminal type

```bash
pip install flask-script
```
Now try rerunning hello.py:

```bash
python hello.py
```

You should get a usage message:

~~~
usage: hello.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help         show this help message and exit
~~~

#### Code Analysis

* We create a ``Manager`` object from our app.
* This manager now controls how we run the code by providing *command line arguments.* For example, we can
    * Change which port the program runs on
    * run a shell with the app context
    * specify whether to run the program in debug mode

Our ``hello.py`` is now expecting a command line argument to tell the manager what it should do. If we simply run the script we'll get a help message.

![run hello.py](./run1.png)

We need to configure pyCharm to run ``hello.py``  with the appropriate command line argument.

![config menu](./edit_run_configs.png)
![config menu](./edit_run_configs2.png)


### Requests and Contexts

>When Flask receives a request from a client, it needs to make a few objects available to the view function that will handle it. A good example is the request object, which encapsulates the HTTP request sent by the client.
>
>The obvious way in which Flask could give a view function access to the request object is by sending it as an argument, but that would require every single view function in the application to have an extra argument. Things get more complicated if you consider that the request object is not the only object that view functions might need to access to fulfill a request.
>
>To avoid cluttering view functions with lots of arguments that may or may not be needed, Flask uses contexts to temporarily make certain objects globally accessible. (*Flask Web Development*, p. 12)

Change hello.py to contain the following code:

```python
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
```

#### Code Analysis
```python
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent
```

`request` is a global variable (not passed into `index`) created by Flask.

## Using Templates

* Control functions return strings for rendering
* If we let the returned strings become too complex, we will have violated our MVC architecture
    * view in control

>A template is a file that contains the text of a response, with placeholder variables for the dynamic parts that will be known only in the context of a request. The process that replaces the variables with actual values and returns a final response string is called rendering. For the task of rendering templates, Flask uses a powerful template engine called Jinja2. (p. 21)

```
git checkout 3a
```
Complete `hello.py` by adding

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### Project now has a directory ``templates``

```
Brians-MacBook-Pro-2:flasky brian$ tree .
.
├── LICENSE
├── README.md
├── hello.py
└── templates
    ├── index.html
    └── user.html
```
* The name of the files (sans the suffix) match the names of control functions in our app

### What is in user.html?

```html
<h1>Hello, {{ name }}!</h1>
```

* Template files contain **presentation logic**
    * HTML with Jinja2 code for inserting a variable (*name*)
* **Templates** have their own language that is **NOT** Python

#### Variable Substitution
```python
t=\
"""
{{name}}
"""
```

#### Control structures

```python
t=\
"""
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}
"""
```

#### Loops


```python
t=\
"""
<ul>
{% for comment in comments %}
    <li>{{ comment }}</li>
{% endfor %}
</ul>
"""
```

#### macros (functions)


```python
t=\
"""
{% import 'macros.html' as macros %}
<ul>
{% for comment in comments %}
{{ macros.render_comment(comment) }}
{% endfor %}
</ul>
"""
```

### Templates can be *inherited*

Create a base template that defines the *look* of your site then inherit and modifies the base template.

```python
t=\
"""
{% extends "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
{{ super() }}
<style>
</style>
{% endblock %}
{% block body %} <h1>Hello, World!</h1> {% endblock %}
"""
```
```python
from flask import Flask, render_template
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
```
## Static Files

>In its default configuration, Flask looks for static files [(e.g. images, CSS files, JavaScript files)] in a subdirectory called static located in the application’s root folder. (p. 32)

## Additional Flask extensions

We are going to install some additional extension for web forms, JavaScript and CSS files, date and time management.

### Using bootstrap

```bash
git checkout 3b
```
In order for this to run we need to install `flask-bootstrap`

```
pip install flask-bootstrap
```
### Moment

```bash
git checkout 3e
pip install flask-moment
```

We now have date-time information at our index.html

## Forms

```bash
pip install flask-wtf

```
Forms are how the user will input data into our application.

* Forms are classes that inherit from Form
    * Form fields are class attributes
    * Attributes must be of specific types (e.g. StringField, SubmitFiled)
    * Fields can have validators that assure that the entered data matches data type/constraints

### Example Form

```python
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
```

### Available Field Validators

| Validator | Description |
|----------:|:------------|
|Email     | Validates an email address|
|EqualTo   | Compares the values of two fields; useful when requesting a password to be entered twice for confirmation |
|IPAddress | Validates an IPv4 network address |
|Length    |Validates the length of the string entered|
|NumberRange | Validates that the value entered is within a numeric range|
|Optional    | Allows empty input on the field, skipping additional validators|
|Required    |Validates that the field contains data|
|Regexp      |Validates the input against a regular expression|
|URL         |Validates a URL|
|AnyOf       |Validates that the input is one of a list of possible values|
|NoneOf      | Validates that the input is none of a list of possible values|

### Form Handling

* Tell app.route what HTTP methods you are going to allow

```python
@app.route('/', methods=['GET', 'POST'])
def index3():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index3'))
    return render_template('index3.html', form=form, name=session.get('name'))
```

>The redirect URL used in this case is the root URL, so the response could have been written more concisely as redirect('/'), but instead Flask’s URL generator function url_for() is used. **The use of url_for() to generate URLs is encouraged** because this function generates URLs using the URL map, so URLs are guaranteed to be compatible with defined routes and any changes made to route names will be automatically available when using this function. (p. 45)

### Pull up Version 4c

```
git checkout 4c
pip install flask_wtf
```

```python
@app.route('/', methods=['GET', 'POST'])
def index4():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index4'))
    return render_template('index4.html', form=form, name=session.get('name'))
```

## Databases

* Flask does not come with native database support

```
git chekcout 5a
pip install flask-sqlalchemy
```

* SQLAlchemy maps our objects to our database tables
* Other ORM options available as well NoSQL mappers

```
git checkout 5a
```

```python
import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname("./"))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


```

## Models

* Models are classes that inherit from db.Model
* Attributes are instances of db.Column
    * Created from db.Integer, db.String(64), etc.
* SQLAlchemy requires that you specify a primary\_key

### Relationships

>Relational databases establish connections between rows in different tables through the use of relationships. The relational diagram in Figure 5-1 expresses a simple relationship between users and their roles. This is a one-to-many relationship from roles to users, because one role belongs to many users and users have only one role. (p. 56)

* db.relationship
* **Note ForeignKey** to specify relationships

> The best way to learn how to work with these models is in a Python shell. (p. 57)

### Working with a Shell activated with the "shell" command line argument

#### Check Database Status periodically

```python
hello.py shell  
from hello import db  
db.create_all()  

db.drop_all()  
db.create_all()  


from hello import Role, User  
admin_role = Role(name='Admin')  
mod_role = Role(name='Moderator')  
user_role = Role(name='User')  
user_john = User(username='john', role=admin_role)   
user_susan = User(username='susan', role=user_role)   
user_david = User(username='david', role=user_role)  

db.session.add(admin_role)
db.session.add(mod_role)

db.session.add_all([admin_role, mod_role, user_role,user_john, user_susan, user_david])


db.session.commit()  
```

[Install a SQLite3 editor](http://sqlitebrowser.org/)

## Using databases in view/control functions
```
git checkout 5b
```

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

```

## Single file vs multifile applications
~~~~
|-flasky  
  |-app/  
    |-templates/  
    |-static/  
    |-main/  
      |-__init__.py  
      |-errors.py  
      |-forms.py  
      |-views.py  
    |-__init__.py  
    |-email.py  
    |-models.py  
  |-migrations/  
  |-tests/  
    |-__init__.py  
    |-test*.py  
  |-venv/  
  |-requirements.txt  
~~~~
