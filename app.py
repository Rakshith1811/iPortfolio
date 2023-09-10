from flask import Flask, render_template, request
from flask_mysqldb import MySQL



app = Flask(__name__, template_folder='templates')
#mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("index.html")



app.run(debug=True)
