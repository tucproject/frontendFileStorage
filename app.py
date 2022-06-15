from flask import Flask, render_template, url_for, request, redirect
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        user_n = request.form['user']
        psw = request.form['psw']
        data = {"user": user_n, "psw": psw}
        try:
            r = requests.post('http://host1720124.hostland.pro/api/register', json=data)
            print(r.text)
            return render_template('index.html', msg=r.text)
        except:
            return "fehler"
    else:
        return render_template('registration.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return 'user page ' + name + ' - ' + str(id)


@app.route('/upload', methods=['GET', 'POST'])
def uploading():
    if request.method == 'POST' and "file" in request.files:
        print('alles gut')
    else:
        return redirect('/')
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

#MYTODO hash for password