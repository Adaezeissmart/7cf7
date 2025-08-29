from flask import Flask
app = Flask(__name__)
@app.route('/logout')
def logout():
    name = ''
    id = ''
    msg = 'Logged out Successfully' 
    return render_template('login.html', msg=msg, name=name, id=id)