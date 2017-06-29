from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="hello")

@app.route('/signup')
def signup():
    return render_template('signup.html', title="signup")

@app.route('/welcome', methods=['POST'])
def welcome():
    username = request.form['username']
    pw_1 = request.form['pw_1']
    pw_2 = request.form['pw_2']
    email = request.form['email']

    return render_template('signup_confirmation.html', title='welcome', username=username)

if __name__ == '__main__':
    app.run(debug=True)