from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sports Database Dictionary
SPORTS_DATA = {
    "boxing": {
        "title": "Boxing",
        "importance": "Crucial for explosive cardiovascular endurance, lightning reflexes, and mental resilience under pressure.",
        "benefits": [
            "Enhanced hand-eye coordination & reaction speed",
            "Core stability, balance, and upper body power",
            "Agility, footwork, and defensive reflexes"
        ],
        "arrangements": "Weekly sparring sessions at central arenas, certified coaching, and weight-class brackets."
    },
    "running": {
        "title": "Running",
        "importance": "Builds ultimate aerobic capacity, improves joint stability, and releases endorphins for mental clarity.",
        "benefits": [
            "Superior cardiovascular stamina & lung strength",
            "Lower-body power, calf strength, and knee stability",
            "High caloric burn and weight management"
        ],
        "arrangements": "Weekend group trail runs, sprint pacing clinics, and seasonal 5K/10K track events."
    },
    "cycling": {
        "title": "Cycling",
        "importance": "Low-impact, high-intensity endurance training that builds quadriceps power and spatial awareness.",
        "benefits": [
            "Joint-friendly endurance & leg hypertrophy",
            "Improves core posture and balance",
            "Great for long-distance athletic recovery"
        ],
        "arrangements": "Group road rides, peloton speed trials, and indoor spin masterclasses."
    },
    "cricket": {
        "title": "Cricket",
        "importance": "Demands tactical focus, fast-twitch reflexes, rotational power, and strategic teamwork.",
        "benefits": [
            "Explosive rotational power for batting & bowling",
            "Precision fielding reflexes and tracking speed",
            "Strategic communication and team coordination"
        ],
        "arrangements": "Net practice sessions, turf grounds booking, and weekend amateur league tournaments."
    },
    "powerlifting": {
        "title": "Powerlifting",
        "importance": "Focuses on raw strength development through compound movements: Squat, Bench Press, and Deadlift.",
        "benefits": [
            "Maximum bone density & muscle strength",
            "Improved biomechanics and postural alignment",
            "High nervous system adaptability"
        ],
        "arrangements": "Rack reservation, form technique coaching, and mock meet competitions."
    },
    "badminton": {
        "title": "Badminton",
        "importance": "Fastest racket sport requiring fast footwork, sharp wrist control, and rapid deceleration.",
        "benefits": [
            "High agility, multi-directional lunging, and speed",
            "Quick visual tracking and wrist flex power",
            "Excellent interval cardio workout"
        ],
        "arrangements": "Indoor synthetic court reservations, shuttlecock supply, and singles/doubles ladders."
    },
    "tennis": {
        "title": "Tennis",
        "importance": "Combines aerobic endurance with anaerobic sprint bursts, precision, and strategic court placement.",
        "benefits": [
            "Full-body strength & core rotatory force",
            "Dynamic lateral footwork and stamina",
            "Sharp mental focus during long rallies"
        ],
        "arrangements": "Clay/hard court bookings, stringing services, and round-robin ladder tournaments."
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sport/<name>")
def get_sport(name):
    sport = SPORTS_DATA.get(name.lower())
    if sport:
        return jsonify(sport)
    return jsonify({"error": "Sport not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)