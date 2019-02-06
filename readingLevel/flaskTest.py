from flask import Flask, render_template
import gradeLevel

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", gradeLevel = gradeLevel.finalCalc, readingLevel = gradeLevel.finalGrade)

if __name__ == "__main__":
    app.run()
