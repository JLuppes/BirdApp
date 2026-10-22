from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/birds')
def birdPage():
    return render_template('bird.html')


@app.route("/seasons")
def seasonsPage():

    now = datetime.now()

    current_month = now.strftime('%B')
    current_year = now.year

    return render_template("seasons.html", month=current_month, year=current_year)



@app.route("/randomNumber")
def randomNumberPage():
    import random
    random_number = random.randint(1, 100)

    return render_template("randomNumberPage.html", random_number=random_number)


if __name__ == "__main__":
    app.run(debug=True)