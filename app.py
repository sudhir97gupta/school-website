from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admission')
def admission():
    return render_template('admission_form.html')



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
