from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail
from flask_mail import Message

#Open .json file and loading its parameters to use in our app

jason = open("config.json","r+")
param = json.load(jason)["params"]

#defining flask app and connecting database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = param["database_url"]
db = SQLAlchemy(app)

#defining mail app and configuring mail settings
app.config.update(
    MAIL_SERVER = param["Mail_server"],
    MAIL_PORT = "465",
    MAIL_USE_SSL = True,
    MAIL_USERNAME = param["Email_From"],
    MAIL_PASSWORD = param["Email_account_password"]
)
mail = Mail(app)

#Making a Model class
#Name of this class should be same name of your table
#First letter of class will be capital

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=False)
    message = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)

#try a manual database entry
#entry = Contact(name="zawar", email="zawar@gmail.com", subject="stay humle and work hard", message="new message is here")
#database entry is working fine


#Handling website URL routes
#root
@app.route("/")
def root_function():
    return render_template("index.html", p=param)


#Function for contact me page of my website
@app.route("/contact", methods = ["POST"])
def contact_form():
    if(request.method == "GET"):
        return render_template("your submit button is gone to GET request")
    if(request.method == "POST"):
        a = request.form.get("name")
        b = request.form.get("email")
        c = request.form.get("subject")
        d = request.form.get("message")
        entry = Contact(name=a,email=b,subject=c,message=d)
        db.session.add(entry)
        db.session.commit()
        msg = Message(c,
                      body=d,
                      sender=param["Email_From"],
                      recipients=[b])
        mail.send(msg)
        return render_template("form submission successfull")

app.run(debug=True)