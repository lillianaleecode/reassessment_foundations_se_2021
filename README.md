#0 I got a new computer so I started to install a bunch of things such as the code editor Visual Studio Code.
Everything I installed was on Python 3.9.6 64-bit interpreter, my modules were installed here such as The Flask-SQLAlchemy.

#1 Since I got a Mac, I had to install Homebrew in my computer so that I can install other stuff like Heroku
#2 I installed Heroku, Python 3 and Pip3
#3 I installed Flask with 'pip3 install flask'
#4 for the database, I installed flask sql alchemy with 'pip3 install flask-sqlalchemy'
#5 Backend: to create the database, in the terminal I created the db with 'from app import db', and later 'db.create_all'
    -after creating the db, we can add entries to it, so for it we import models. 
        'from app importBlogPost'
    -how to retrieve info (print out) of our database from the terminal?: 
        answer(example): 'BlogPost.query.all()' it should print out a list.
    -how to add to the db from the temrinal?:
        answer: db.session.add(BlogPost("the fields from our model goes here"))
        example: db.session.add(BlogPost(title='Blog #1', content="here some info', author='me!'))
        
        after adding posts, we can check them with 'BlogPost.query.all(). So for example, if we want to check only the title of blog post #1, then we should write in the terminal:
        'BlogPost.query_all()[0].title'

    to delete posts : 
        db.session.delete(BlogPost.query.get(1))
        db.session.commit()
#6 I installed 'pip3 install requests'

Steps I took for creating this project:
#part -1 installing all sort of requirements for the project
#part 0 set up the project with basic Flask structure content 
#part 1. created static dummy content before creating stuff for the databases
#part 1. created basic routes such as /home /index.
#part 2.a SETTING UP THE DATABASE with sqlite
#part 2.b CREATING MODELS with classes
#part 3 creating our database posts.db from the terminal
#part4 creating content posts with the route 'posts'
#part 5 creating DELETE and EDIT route



Deploying to HEROKU:

#1 I installed Heroku with :'brew tap heroku/brew && brew install heroku'
#1.2 and later did also: 'pip3 install gunicorn'
#1.3 now we need to let heroku know we are using gunicorn. by writing in the terminal: 'touch Procfile'
and after it, a Procfile file will be created in my folder. 
#1.4 inside this file, I just need to write "web: gunicorn" to let heroku know I'm using gunicorn, and "app:app" to let heroku know that the app we are using is from my file called app.py
#2 Heroku needs to know all the requirements, so I retrieve it with 'pip3 freeze > requirements.txt'.
A new file called "requirements.txt" will be created in my folder.
#3 Heroku ues Github so I need to push my code to Github.
3.1 'git init'
3.2 'git add .'
3.3 'git status' (I see my stuff)
3.4 'git commit -m 'Reassessment Project'' (creates stuff)
3.5 'git remote add origin 'https://github.com/lillianaleecode/reassessment_foundations_se_2021.git''
3.6 'git push -u origin master'
3.7 I sign in with my github credentials and the terminal will display a link to my github to view it

#4 after having my code in Github, now in my terminal I'll type 'heroku login'. it will take me to the website to sign in.
#5 now type in the terminal 'heroku create'. the terminal gave me this following link: 'https://pacific-fortress-91430.herokuapp.com/'
#6 i renamed the link by typing in the terminal 'heroku rename reassessmentlillianalee' and I got this link https://reassessmentlillianalee.herokuapp.com/ 
#7 now I just push the code to heroku by writing 'git push heroku master' in the terminal.
now my project is live in 'https://reassessmentlillianalee.herokuapp.com/' :D yey!
