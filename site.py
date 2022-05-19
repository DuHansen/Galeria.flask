from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/sobriedade")
def sobriedade():
    return render_template("sobriedade.html")

if __name__ == "__main__":
  app.run(debug=True)

