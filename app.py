####IMPORT MODULES ####

from flask import Flask
from flask import request, redirect #part 4 request for @app.route('/posts')
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy #part 2 required for databases
from datetime import datetime #import required sice we are using it in Class BlogPost for 'data_posted'

app = Flask(__name__)

#### DATABASE ####

#part 2.a SETTING UP THE DATABASE, telling flask where our database will be stored, this case I'm using sqlite
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db' # Im using sqlite because it is easy for debugging mode since it stores locally in a file, for production, it can be swap to others db such as MySQL 
db = SQLAlchemy(app)#defined the path where it could be stored. (/// = relative path to app.py. this one is cleaner) (//// means absolute path)

#part 2.b CREATING MODELS with classes
#(class BlogPost) the class called blogpost and it will inherit from our database 'Model'
#(id) first thing that a Model have is the id. and we will create it with columns. 
# (id) the type of data will be integer and it is set to primary_key=True, it means the id will be the main distinguisher btw different blog posts.
#(title) nullable=False means it is required and it cannot be empty, set the string max of 100 characters.
#(content) it is set to text, no restrictions of how much text I could add.
#(author) to autocomplete to N/A, we set it to default='N/A'
#(function def __repr__) this function is going to print out whatever we post.
#part 3 creating our database posts.db from the terminal
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self).id


#part 1. dummy content we are creating for posts.html that will be replaced with the dinamic input we created with class BlogPost
all_posts = [
    {
        'title': 'POst1',
        'content': 'this is content',
        'author': 'Lilly'
    },
    {
        'title': 'POst2',
        'content': 'this is content 2'
    },

]


#### ROUTES ####


@app.route('/posts', methods=['GET', 'POST'])
def posts():
#part4 creating content posts
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        #part 4.b now we add this post to our db
        db.session.add(new_post) # it sabes the post in the db temporarily
        db.session.commit() #it saves the post in the db permanently
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.all() #here we are calling all the query of the db 'BlogPosts.query.all()'
        #all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts) 
    #we create a variable called posts to call out the dictionary all_posts created before
    
@app.route('/')
@app.route('/home')
def hello():
    return render_template('index.html')

#@app.route('/home/<string:name>') #example to dinamic URl with <string:name>
#def hello(name):
#    return "Hello!" + name

#part 5 creating DELETE and EDIT route
@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST']) #if we are editing, it means we need to post
def edit(id):

    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title'] # "request.form['title']" is taking the info and saving it (overwriting) in "post.title"
        post.author = request.form['author'] 
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post) #post=post sends the post we are editing over so we can autofill the fields in edit form.

#debug mode is on
if __name__ == "__main__":
    app.run(debug=True) 
