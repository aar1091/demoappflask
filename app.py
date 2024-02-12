from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Teletubies123'  # Esta clave secreta se utiliza para firmar las sesiones

# Datos de usuario de ejemplo (deberías almacenarlos de manera más segura en un sistema real)
users = {'username': 'password', 'user2': 'password2'}  

@app.route('/')
def home():
    if 'username' in session:
        return f'¡Hola, {session["username"]}! <a href="/logout">Cerrar sesión</a>'
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Credenciales inválidas. Inténtalo de nuevo.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
