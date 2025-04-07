from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')  # You'll need an about.html template

@app.route('/contact')
def contact():
    return "Contact Us page goes here!" # Or render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)