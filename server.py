from flask import Flask
import random

random_num= random.randint(0,9)
print(random_num)
app = Flask(__name__)

@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media0.giphy.com/media/3o7TKRVBGOSdSODGJa/giphy.webp?cid=ecf05e47tztjla5al03bmj06e81lpjckarcag0jzjev7ay7w&ep=v1_gifs_search&rid=giphy.webp&ct=g'>")

@app.route("/<int:num>")
def check_num(num):
    if num==random_num:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"
    elif num<random_num:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif num>random_num:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

if __name__ == "__main__":
    #run the app in debug mode i.e, auto-reloaded
    app.run(debug= True)