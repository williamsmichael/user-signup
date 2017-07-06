from flask import Flask, render_template, request, url_for, redirect
import re

app = Flask(__name__)


def check_username(username):
    error_username = ""

    if len(username) not in range(3, 21):
        error_username = 'Username must be 3 - 20 characters'

    if ' ' in username:
        error_username = 'Username does not permit spaces'

    return error_username


def check_pw(pw_a, pw_b):
    error_pw = ""

    if pw_a != pw_b:
        error_pw = 'Passwords must match'

    if len(pw_a) not in range(3, 21):
        error_pw = 'Password must be 3 - 20 characters'

    return error_pw


def check_email(email):
    error_email = ""

    if len(email) not in range(3, 21) and email:
        error_email = 'Email must be 3 - 20 characters'

    if ' ' in email:
        error_email = 'Email does not permit spaces'

    if "@" and "." not in email and email:
        error_email = "Email must contain @ and ."

    if not re.match(r"\w+[.|\w]\w+@\w+[.]\w+[.|\w+]\w+", email):
        error_email = "some kind of error?"

    return error_email


@app.route('/welcome', methods=['POST'])
def welcome():

   if request.method == 'POST': 

        username = request.form['username'].strip()
        pw_a = request.form['pw_a']
        pw_b = request.form['pw_b']
        email = request.form['email'].strip()

        error_username = check_username(username)
        error_pw = check_pw(pw_a, pw_b)
        error_email = check_email(email)

        # errors exist
        if not all(x is "" for x in (error_username, error_pw, error_email)):
            return redirect("/?error_username=" + error_username + "&error_pw=" + error_pw + "&error_email=" + error_email + "&username=" + username + "&email=" + email)

        # no errors exist
        return render_template('welcome.html', title='welcome', username=username)


@app.route('/', methods=['POST', 'GET'])
def index():

    if request.args.get("username") is None:
        username = ""
    else:
        username = request.args.get("username")

    if request.args.get("email") is None:
        email = ""
    else:
        email = request.args.get("email")

    error_username = request.args.get("error_username")
    error_pw = request.args.get("error_pw")
    error_email = request.args.get("error_email")

    return render_template('index.html', title='signup', username=username, email=email, error_username=error_username, error_pw=error_pw, error_email=error_email)


if __name__ == '__main__':
    app.run(debug=True)