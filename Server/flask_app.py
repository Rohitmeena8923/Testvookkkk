from flask import Flask, render_template, request
from bot import run_bot
import threading

app = Flask(__name__)

@app.route('/test')
def test():
    questions = [
        {"question": "What is 2+2?", "options": ["2", "3", "4", "5"]},
        {"question": "Capital of France?", "options": ["Berlin", "Paris", "Rome", "Madrid"]}
    ]
    return render_template("test_template.html", questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    answers = dict(request.form)
    return f"<h2>Analysis</h2><pre>{answers}</pre>"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
