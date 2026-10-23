from flask import Flask, render_template, request
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # Reads from .env file

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv(
    'SECRET_KEY') or 'make-a-new-secret-key-plz'


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


@app.route('/profile', methods=["GET", "POST"])
def profilePage():

    minGuests = 1
    maxGuests = 10

    # Check to see if the request method is POST
    if request.method == "POST":

        # Capture data from the form
        name = request.form.get("name", "").strip()  # name
        email = request.form.get('email', '').strip()  # email
        quan = request.form.get('quan', '').strip()
        rel = request.form.get('rel', '').strip()
        comments = request.form.get('comments', '').strip()
        accommodations = (request.form.get(
            'accommodations', '').strip() == "yes")

        errorList = []

        # Try converting quan to int
        try:
            quan = int(quan)
        except ValueError:
            errorList.append("Please enter an integer between 1 and 10")

        # Confirm required fields are present
        if not name or not email or not quan or not rel:
            errorList.append("Please fill out all required fields.")

        # Confirm quan is within min and max
        if quan > maxGuests or quan < minGuests:
            errorList.append("Please select a quantity between 1 and 10")

        if errorList:
            return render_template('profileForm.html', error=errorList)

        # Show the success page with submitted data
        return render_template('profileSuccess.html', name=name, email=email, quan=quan, rel=rel, comments=comments, accommodations=accommodations)

    # Show the blank form to fill out
    return render_template('profileForm.html')


if __name__ == "__main__":
    app.run(debug=True)
