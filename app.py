from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open("knowledge.json") as f:
    knowledge = json.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        query = request.form.get("query", "").lower()
        response = knowledge.get(query, "Sorry, I don't understand.")
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

