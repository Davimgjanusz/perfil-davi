from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

@app.route('/EditarPerfil')
def editarperfil():
    return render_template('EditarPerfil.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)