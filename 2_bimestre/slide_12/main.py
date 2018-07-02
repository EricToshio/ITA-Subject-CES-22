from flask import Flask, render_template, request, make_response, session, redirect, url_for, escape, send_from_directory
from werkzeug import secure_filename
import os

app = Flask(__name__)
app.secret_key = '3sP5FXv4YKgt4RSe'

@app.route('/')
def index():
    last_user = request.cookies.get('last_user')
    if 'username' in session:
        username = session['username']
        list_files = os.listdir(os.path.join('./',username))
        return render_template('list_upload.html', name= username, files=list_files)
    return make_response(render_template('index.html', user = last_user))


@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/send_file', methods = ['GET', 'POST'])
def send_file():
    if request.method == 'POST':
        f = request.files['file']
        username = session['username']
        f.save(os.path.join(username, f.filename))

        return render_template('upload_success.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        #logar
        session['username'] = user
        #Cria uma pasta para aquele o novo usuario caso não exista
        if not os.path.exists(user):
            os.makedirs(user)
        #adiciona ultimo usuario logado aos cookies
        resp = make_response(render_template('login_success.html'))
        resp.set_cookie('last_user', user)
        return resp
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dowload/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    user = session['username']
    return send_from_directory(directory=user, filename=filename)


if __name__ == '__main__':
    app.run(debug=True)