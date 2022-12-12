import imp
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
basicAuth = HTTPBasicAuth()

users = {
    "user1":generate_password_hash("pass1"),
    "user2":generate_password_hash("pass2")
}

@basicAuth.verify_password
def verifypassword(username,password):
    if username in users and \
        check_password_hash(users.get(username),password):
            return username

@app.route('/')
@basicAuth.login_required

def index():
    return "Hello, %s!" %basicAuth.current_user()

if __name__ == '__main__':
    app.run(debug=True)(host="1.1.1.1")
