from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

    
import json

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Update with your SMTP server
app.config['MAIL_PORT'] = 465  # Update with your SMTP port
app.config['MAIL_USE_SSL'] = True
#app.config['MAIL_USERNAME'] = 'sohamnilvaze.39@gmail.com'  # Update with your email
app.config['MAIL_USERNAME'] = 'soham_vaze'
app.config['MAIL_PASSWORD'] = 'Soham@2004'  # Update with your email password
app.config['SECRET_KEY'] = '32350f84288e0445d47cb9e5d16e136e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
mail = Mail(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_message_category = 'info'

migrate= Migrate(app,db)

from tut3 import routes
