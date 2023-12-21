from flask import Flask, render_template
from random import choice

app = Flask(__name__)

statement_type = ["question", "exclamation", "statement", "implication"]
basic_conjunctions = ["because", "but", "so"]


@app.route("/new")
def new_output():
    return home()


@app.route("/")
def home():
   output = f"""
  Statement type: {choice(statement_type)}
  Basic conjunction: {choice(basic_conjunctions)}
  """
   return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
