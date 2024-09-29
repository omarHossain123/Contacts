from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Specifies the location of the local SQL light database we're storing on our machine 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# Makes it so we're not tracking all of the modifications we make to the database 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

# Creates a database instance which gives us access to the database we specified above
db = SQLAlchemy(app)
