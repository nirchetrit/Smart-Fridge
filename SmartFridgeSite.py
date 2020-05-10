from flask import Flask, render_template, url_for
app = Flask(__name__)

stocks = [
    {
        'id' : '1',
        'title' : 'Kotej',
        'brand':'Tnuva',
        'price' : '6.90',
        'description' : 'kotej 5%...',
        'etc':'milk / ...',
        'imgUrl':'10/5/2020'
    },
    {
        'id' : '2',
        'title' : 'milk',
        'brand':'tara',
        'price' : '4.90',
        'description' : 'normal milk',
        'etc':'milk / ...',
        'imgUrl':'10/5/2020'
    },
    {
        'id' : '3',
        'title' : 'Ketchup',
        'brand':'Osem',
        'price' : '10.90',
        'description' : '...',
        'etc':'sauce / ...',
        'imgUrl':'10/5/2020'
    }
]








@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', stocks = stocks, title = 'home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)