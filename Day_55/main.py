from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

def make_bold(function):
    def bold_wrapper():
        text = function()
        final_text = f"<b>{text}</b>"
        return final_text
    return bold_wrapper

def make_emphasis(function):
    def emphasis_wrapper():
        text = function()
        final_text = f"<em>{text}</em>"
        return final_text
    return emphasis_wrapper

def make_underline(function):
    def underline_wrapper():
        text = function()
        final_text = f"<u>{text}</u>"
        return final_text
    return underline_wrapper

@app.route("/")
def hello_world():
    return open("Day_55/index.html")

@app.route("/<int:guessed_number>")
def guessed(guessed_number):
    if guessed_number > number:
        return open("Day_55/too_high.html")
    elif guessed_number < number:
        return open("Day_55/too_low.html")
    else:
        return open("Day_55/right.html")
if __name__ == "__main__":
    app.run(debug=True)