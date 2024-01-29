from flask import Flask, render_template, redirect, url_for

app= Flask(__name__)


@app.route('/')
def home():
    return render_template('indexx.html')





#planning to possibly add more features (switch to Django??)
# @app.route('/generic')
# def generic():
#     return render_template('generic.html')

# @app.route('/elements')
# def elements():
#     return render_template('elements.html')

if __name__ == '__main__':
    app.run(debug=True)