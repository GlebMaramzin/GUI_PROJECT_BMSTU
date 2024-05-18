from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def loging():
    message = ''
    if request.method == 'GET':
        return render_template('base.html')
    else:
        return render_template('login.html')


@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/about')
def about_us():
    return render_template('about.html')

if __name__ == 'main':
    app.run(debug=True)
