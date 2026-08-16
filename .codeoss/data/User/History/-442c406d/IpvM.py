from flask import Flask, render_template, abort

app = Flask(__name__)

sports_data = {
    "cricket": {
        "title": "Cricket",
        "tagline": "Master the pitch with elite coaching.",
        "description": "Join our comprehensive cricket program covering batting, bowling, and field tactics."
    },
    "football": {
        "title": "Football",
        "tagline": "Elevate your game on the field.",
        "description": "Develop agility, teamwork, and ball control in our structured football drills."
    },
    "badminton": {
        "title": "Badminton",
        "tagline": "Precision and speed on the court.",
        "description": "Improve your footwork, smash power, and reaction times with practical court training."
    }
}

@app.route('/')
def home():
    return render_template('index.html', sports=sports_data)

@app.route('/sport/<sport_name>')
def sport_detail(sport_name):
    sport = sports_data.get(sport_name.lower())
    if not sport:
        abort(404)
    return render_template('sport.html', sport=sport, key=sport_name)

if __name__ == '__main__':
    app.run(debug=True)