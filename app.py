# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# Flask Setup
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# Route that renders the form and receives form data
# Query the database and send the jsonified results if route hit via a post method
@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        print(request.form)
        return redirect("/", code=302)

    return render_template("form.html")

if __name__ == "__main__":
    app.run()