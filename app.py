from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save_reason", methods=["POST"])
def save_reason():
    data = request.json
    reason = data.get("reason", "")

    with open("reasons.txt", "a", encoding="utf-8") as f:
        f.write(reason + "\n---\n")

    return "ok"