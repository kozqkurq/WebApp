from flask import Flask, request, render_template

app = Flask(__name__)

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