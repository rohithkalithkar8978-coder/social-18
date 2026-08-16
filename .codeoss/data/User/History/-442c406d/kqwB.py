from flask import Flask, render_template, abort, jsonify

app = Flask(__name__)

SPORTS_DATA = {
    "boxing": {
        "title": "Boxing",
        "bg_image": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Explosive Power & High-Speed Reflexes",
        "importance": "Crucial for explosive cardiovascular endurance, lightning reflexes, and mental resilience under high pressure.",
        "benefits": ["Enhanced hand-eye coordination & reaction speed", "Core stability, balance, and upper body power", "Agility, footwork, and defensive reflexes"],
        "arrangements": "Weekly sparring sessions at central arenas, certified coaching, and weight-class brackets for ages 14–18."
    },
    "running": {
        "title": "Running",
        "bg_image": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Peak Endurance & Kinetic Motion",
        "importance": "Increases lung capacity, strengthens bone density, and lowers resting heart rate for long-term stamina.",
        "benefits": ["Stamina improvement & lung strength", "Dopamine boost & mental clarity", "Leg strength and joint vitality"],
        "arrangements": "Bi-weekly 5K sprint trials and 10K endurance runs timed with digital RFID chips."
    },
    "cycling": {
        "title": "Cycling",
        "bg_image": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Low-Impact High-Velocity Power",
        "importance": "Low-impact endurance training that maximizes leg power without damaging developing joint structures.",
        "benefits": ["Quadriceps and calf power", "Spatial awareness & high speed", "Vascular health and core stability"],
        "arrangements": "Weekend velodrome races, highway sprint circuits, and safety-escorted group rides."
    },
    "cricket": {
        "title": "Cricket",
        "bg_image": "https://images.unsplash.com/photo-1531415074968-036ba1b575da?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Tactical Precision & Team Strategy",
        "importance": "Fosters high-pressure teamwork, tactical thinking, dynamic movement, and upper-body rotational power.",
        "benefits": ["Strategic intelligence", "Sprinting & throwing power", "Team collaboration under pressure"],
        "arrangements": "T20 dynamic leagues, net practice sessions, and professional turf pitch matches."
    },
    "powerlifting": {
        "title": "Powerlifting",
        "bg_image": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Raw Muscle & Skeletal Alignment",
        "importance": "Builds skeletal mass, foundational raw power, and proper kinetic chain biomechanics.",
        "benefits": ["Maximum strength output", "Bone density enhancement", "Posterior chain activation"],
        "arrangements": "Supervised Squat/Bench/Deadlift max tests with certified strength coaches and safety spotters."
    },
    "badminton": {
        "title": "Badminton",
        "bg_image": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Rapid Aerobics & Wrist Reflexes",
        "importance": "Fastest racquet sport demanding high anaerobic capacity, rapid spatial reflexes, and kinetic power.",
        "benefits": ["Reflex speed and footwork agility", "Calf and core explosion", "High calorie-burn rate"],
        "arrangements": "Indoor synthetic court tournaments, singles & doubles leagues, and footwork clinics."
    },
    "tennis": {
        "title": "Tennis",
        "bg_image": "https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?auto=format&fit=crop&w=1920&q=80",
        "tagline": "Total Body Motion & Precision Control",
        "importance": "Builds whole-body muscular endurance, lateral footwork agility, and tactical point play resilience.",
        "benefits": ["Aerobic & anaerobic fitness", "Rotational core strength", "Precision hand-eye control"],
        "arrangements": "Hard-court rankings matches, weekend grand-slam format tournaments, and ball-machine sessions."
    }
}

@app.route('/')
def home():
    return render_template('index.html', sports=SPORTS_DATA)

@app.route('/sport/<name>')
def sport_detail(name):
    sport = SPORTS_DATA.get(name.lower())
    if sport:
        return render_template('sport.html', sport=sport)
    abort(404)

@app.route('/api/sport/<name>')
def api_sport(name):
    sport = SPORTS_DATA.get(name.lower())
    if sport:
        return jsonify(sport)
    return jsonify({"error": "Sport not found"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)