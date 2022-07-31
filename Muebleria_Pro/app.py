from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/oferta')
def oferta():
    return render_template('oferta.html')

if __name__ == '__main__':
    app.run(debug=True)
