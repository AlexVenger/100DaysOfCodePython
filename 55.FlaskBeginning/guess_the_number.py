from flask import Flask
import random

MIN_BORDER = 0
MAX_BORDER = 9

app = Flask(__name__)

number_to_guess = random.randint(MIN_BORDER, MAX_BORDER)


@app.route("/")
def main_page():
    return f'''
    <h1>Guess the number from {MIN_BORDER} to {MAX_BORDER}!</h1>
    <img src="https://media3.giphy.com/media/4GKjAS16BrjApOC6rl/giphy.gif?
    cid=ecf05e47obr0qan3973x97xxppfcwqp1xmq1fwot7a31808k&ep=v1_gifs_search&rid=giphy.gif&ct=g"/>
    '''


@app.route("/<int:number>")
def number_page(number):
    if number < number_to_guess:
        return '''
        <h1>Too low! Try again!</h1>
        <img src="https://media1.giphy.com/media/36Alf6u5zdL4En4jRO/giphy.gif?
        cid=ecf05e47yl109r2189z687yv3znr4tjcjzd41elasghzg5bo&ep=v1_gifs_related&rid=giphy.gif&ct=g"/>
        '''
    elif number > number_to_guess:
        return '''
        <h1>Too high! Try again!</h1>
        <img src="https://media2.giphy.com/media/zNOnHRdaG0ANFa38UQ/giphy.gif?
        cid=ecf05e47zugkg9glcukdzyhmjxxgoky3ux5wog9l1h2b04za&ep=v1_gifs_related&rid=giphy.gif&ct=g"/>
        '''
    else:
        return '''
        <h1>Congratulations! You got it!</h1>
        <img src="https://media4.giphy.com/media/US7sKLbHAovvPgPN3Y/giphy.gif?
        cid=ecf05e47zugkg9glcukdzyhmjxxgoky3ux5wog9l1h2b04za&ep=v1_gifs_related&rid=giphy.gif&ct=g"/>
        '''


if __name__ == "__main__":
    app.run(debug=True)
