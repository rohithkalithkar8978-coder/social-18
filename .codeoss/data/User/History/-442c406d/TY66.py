from flask import Flask, render_template

app = Flask(__name__)

# Dictionary expected by templates/index.html
sports_data = {
    "cricket": "Cricket",
    "football": "Football",
    "badminton": "Badminton"
}

@app.route('/')
def home():
    return render_template('index.html', sports=sports_data)

if __name__ == '__main__':
    app.run(debug=True)