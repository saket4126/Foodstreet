from flask import Flask, render_template, request
from database.db import db, cursor
from database.restaurant_queries import add_restaurant_request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")
@app.route('/restaurant-enroll', methods=['GET', 'POST'])
def restaurant_enroll():

    if request.method == 'POST':

        data = (
            request.form['restaurant_name'],
            request.form['owner_name'],
            request.form['email'],
            request.form['phone'],
            request.form['address'],
            request.form['cuisine'],
            request.form['description']
        )

        add_restaurant_request(data)

        return "Data Saved Successfully"

    return render_template('restaurant_enrollment.html')
if __name__ == "__main__":
    app.run(debug=True)