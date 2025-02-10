from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    contact_info = {
        'email': 'contact@website.com',
        'phone': '123-456-7890',
        'address': '1234 Elm Street, Some City, Some Country'
    }

    additional_contacts = [
        {'name': 'John Doe', 'email': 'hotelganesha@example.com'},
        {'name': 'Jane Smith', 'email': 'sinergigemilang@example.com'}
    ]

    return render_template('contact.html', contact_info=contact_info, additional_contacts=additional_contacts)

if __name__ == '__main__':
    print("Flask app is starting...")
    app.run(debug=True)
