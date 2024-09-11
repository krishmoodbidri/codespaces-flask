from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
    return render_template("index.html", title="Hello", user_input=user_input)