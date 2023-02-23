from flask import Flask,render_template
from main import tracks

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.jinja", tracks=tracks)

if __name__ == "__main__":
    app.run(debug=True)