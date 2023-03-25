from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Date, LargeBinary
import json



local_server = True 
with open('config.json','r') as c:
    parameters = json.load(c)["parameters"]
    
local_server = True 
app = Flask(__name__)
app.jinja_env.variable_start_string = '{{ '
app.jinja_env.variable_end_string = ' }}'
if(local_server):
    app.config["SQLALCHEMY_DATABASE_URI"] = parameters['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = parameters['prod_uri']

db = SQLAlchemy(app)

class Post(db.Model):
    serial_number= db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    slug = db.Column(db.String(100),nullable=False)
    date = db.Column(db.Date)
    image = db.Column(db.LargeBinary)
    content = db.Column(db.String)
    
    # def __repr__(self):
    #     return f"<Post(id={self.id}, title='{self.title}', date='{self.date}')>"
    
# posts = Post.query.all()
# for post in posts:
#     print(post.serial_number, post.title, post.slug, post.date, post.image, post.content)



    
@app.route('/blogs/<string:post_slug>', methods=['GET'])
def post(post_slug):
    post = Post.query.filter_by(slug=post_slug).first()
    print(post)
    return render_template('blogs.html', parameters=parameters, post=post)


@app.route('/')
def index():
    return render_template('index.html', parameters=parameters)

@app.route('/blog')
def blog():
    print("hello")
    return render_template('blog.html', parameters=parameters)

@app.route('/login')
def login():
    return render_template('login.html' , parameters=parameters)

@app.route('/about')
def about():
    return render_template('about.html' , parameters=parameters)

@app.route('/contact')
def contact():
    return render_template('contact.html', parameters=parameters)

if __name__ == '__main__':
    app.run(debug=True)
    
    
# from flask import Flask, render_template,request
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine, Column, Integer, String, Date

# import json

# with open('config.json','r') as c:
#     parameters = json.load(c)["parameters"]

# app = Flask(__name__)
# app.jinja_env.variable_start_string = '{{ '
# app.jinja_env.variable_end_string = ' }}'

# if parameters.get('local_server'):
#     app.config["SQLALCHEMY_DATABASE_URI"] = parameters['local_uri']
# else:
#     app.config["SQLALCHEMY_DATABASE_URI"] = parameters['prod_uri']

# db = SQLAlchemy(app)

# class Post(db.Model):
#     serial_number = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     slug = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.Date)
#     image = db.Column(db.String(255))
#     content = db.Column(db.String)

#     def _repr_(self):
#         return f"<Post(id={self.id}, title='{self.title}', date='{self.date}')>"

    
# @app.route('/blogs/<string:post_slug>', methods=['GET'])
# def post(post_slug):
#     post = Post.query.filter_by(slug=post_slug).first()
#     print(post)
#     return render_template('blogs.html', parameters=parameters, post=post)



# @app.route('/')
# def index():
#     return render_template('index.html', parameters=parameters)

# @app.route('/blog')
# def blog():
#     return render_template('blog.html', parameters=parameters)

# @app.route('/login')
# def login():
#     return render_template('login.html', parameters=parameters)

# @app.route('/about')
# def about():
#     return render_template('about.html', parameters=parameters)

# @app.route('/contact')
# def contact():
#     return render_template('contact.html', parameters=parameters)

# if __name__== '_main_':
#     app.run(debug=True)
