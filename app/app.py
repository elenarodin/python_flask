from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')


app.run(debug=True, host='0.0.0.0')
