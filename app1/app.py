from flask import Flask
from flask import url_for, render_template, request, session, redirect
#from flask_peewee.db import Database

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', data = {'name': 'Jesse', 'age': 'Almost 29'})

@app.route('/user/<name>')
def user(name):
    return 'User was {0}'.format(name)

@app.route('/story/<int:id>')
def story(id):
    return 'The story id is: {0}'.format(id)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "POST":
        return "The user posted!"
    else:
        return "The user did a get!"

@app.route('/move')
def move():
    return redirect(url_for('index'))

# 404 Error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# The startup command
if __name__ == '__main__':
    app.run()