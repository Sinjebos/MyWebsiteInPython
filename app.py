import gspread
from flask import Flask, render_template, request as r
app = Flask(__name__)

gc = gspread.service_account(filename='minhemsidasdatabas.json')
sh = gc.open('flask-website')

shProfile = sh.get_worksheet(0)
shContact = sh.get_worksheet(1)


@app.route('/', methods=['POST', 'GET'])
def home():
    if r.method == 'POST':
        shContact.append_row(
            [r.form['name'], r.form['email'], r.form['message']])
    profile = {
        'About': shProfile.acell('B1').value,
        'Intrests': shProfile.acell('B2').value,
        'Experience': shProfile.acell('B3').value,
        'Education': shProfile.acell('B4').value
    }
    return render_template("index.html", profile=profile)


@app.route('/contact')
def contact():
    return render_template('contact.html')
