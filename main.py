from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def signup():
    return render_template('index.html', title="signup")

@app.route('/welcome')
def welcome():
    return render_template('signup_confirmation.html', title="welcome", username="Michael")

if __name__ == '__main__':
    app.run(debug=True)