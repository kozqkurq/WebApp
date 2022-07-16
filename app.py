from flask import Flask, request, render_template, jsonify
import sqlite3

from flask_sqlalchemy import SQLAlchemy
from pyparsing import col
from mysql_model import Person

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:p%40ssword1@mysqldb/test_mysql?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Response Data"

@app.route("/another")
def another():
    return "Another Response"



@app.route("/test_request")
def test_request():
    return f"test_request:{request.args.get('dummy')}"

@app.route("/exercise_request/<dummy>")
def exercise_request(dummy):
    return f"exercise_request:{dummy}"



@app.route("/show_html")
def show_html():
    return render_template("test_html.html")

@app.route("/show_exercise_html")
def show_exercise_html():
    return render_template("exercise.html")

@app.route("/exercise")
def exercise():
    return render_template("answer.html", name=request.args.get("my_name"))



@app.route("/try_rest", methods=["POST"])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)



@app.route("/sqlite")
def sqlite():
    con = sqlite3.connect('./test_db')
    cur = con.cursor()
    response = ""

    for row in cur.execute("SELECT * FROM person"):
        response += "{"
        for column in row:
            response += str(column) + ", "
        response += "}"

    return response

@app.route("/person_search")
def person_search():
    return render_template('./person_search.html')

@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size >= search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)
