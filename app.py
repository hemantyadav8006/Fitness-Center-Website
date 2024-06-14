from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
uri = "mongodb+srv://hemantyadav8006:wNqvrptyynTzSuky@cluster2.nnrkaax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2"

app = Flask(__name__)

client  = MongoClient(uri)

db = client.member_db


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/price')
def price():
    return render_template('prices.html')


@app.route('/blog')
def blog():
    return render_template('blogs.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/pricing-payment1')
def payment1():
    return render_template('payment1.html')


@app.route('/pricing-payment2')
def payment2():
    return render_template('payment2.html')


@app.route('/pricing-payment3')
def payment3():
    return render_template('payment3.html')



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/admin_data', methods=['GET'])
def show_payment():
    register = list(db.member_list.find({},{'_id':False}))
    return jsonify({'Register':register})



@app.route('/admin_data', methods=['POST'])
def payment():
    name = request.form['name']
    member_mail = request.form['member_mail']
    member_pin = request.form['member_pin']
    card_number = request.form['card_number']
    years = request.form['years']
    months = request.form['months']
    db.member_list.insert_one({
        'Name':name,
        'Email':member_mail,
        'Pin':member_pin,
        'Card_Number':card_number,
        'Years':years,
        'Months':months
    })
    return jsonify({'msg':'Order Completed !'})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)