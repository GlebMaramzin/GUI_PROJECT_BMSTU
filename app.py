from flask import Flask, render_template, request, url_for
#from flask_login import LoginManager
#from forms import LoginForm

app = Flask(__name__)
#login_manager = LoginManager(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/test')
def index():
    return render_template('test.html')

@app.route('/login', methods=['GET', 'POST'])
def loging():
    message = ''
    if request.method == 'GET':
        return render_template('base.html')
    else:
        return render_template('login.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

if __name__ == 'main':
    app.run(debug=True)
