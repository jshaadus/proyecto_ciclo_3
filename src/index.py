from flask import Flask, render_template

app = Flask(__name__)


'''
# Creating simple Routes 
@app.route('/')
def test():
    return "Home Page"


@app.route('/test/about/')
def about_test():
    return "About Page"

'''

# rutas para renderizar


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/administrador', strict_slashes=False)
def administrador():
    return render_template("administrador.html")


@app.route('/docentes', strict_slashes=False)
def docentes():
    return render_template("docentes.html")


@app.route('/estudiantes', strict_slashes=False)
def estudiantes():
    return render_template("estudiantes.html")


# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
