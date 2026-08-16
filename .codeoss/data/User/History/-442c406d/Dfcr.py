from flask import Flask, jsonify, render_template

app = Flask(__name__)

# SporSPORTS_DATA = {
    "boxing": {
        "title": "Boxing",
        "bg_image": "https://images.unsplash.com/photo-1549719386-74dfcbf7dbed?auto=format&fit=crop&w=1600&q=80",
        "importance": "Crucial for explosive cardiovascular endurance, reflexes, and mental resilience.",
        "benefits": ["Enhanced hand-eye coordination", "Core stability & power", "Agility and defensive reflexes"],
        "arrangements": "Weekly sparring sessions at central arenas, certified coaching, and weight-class brackets."
    },
    "running": {
        "title": "Running",
        "bg_image": "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=1600&q=80",
        "importance": "Increases lung capacity, strengthens bone density, and lowers resting heart rate.",
        "benefits": ["Stamina improvement", "Dopamine & mental clarity", "Leg strength and joint vitality"],
        "arrangements": "Bi-weekly 5K sprint trials and 10K endurance runs timed with digital RFID chips."
    },
    "cycling": {
        "title": "Cycling",
        "bg_image": "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=1600&q=80",
        "importance": "Low-impact endurance training that maximizes leg power without damaging joints.",
        "benefits": ["Quadriceps and calf power", "Spatial awareness & speed", "Vascular health"],
        "arrangements": "Weekend velodrome races, highway sprint circuits, and safety-escorted group rides."
    },
    "cricket": {
        "title": "Cricket",
        "bg_image": "https://images.unsplash.com/photo-1531415074968-036ba1b575da?auto=format&fit=crop&w=1600&q=80",
        "importance": "Fosters high-pressure teamwork, tactical thinking, dynamic movement, and upper-body power.",
        "benefits": ["Strategic intelligence", "Sprinting & throwing power", "Team collaboration under pressure"],
        "arrangements": "T20 dynamic leagues, net practice sessions, and professional turf pitch matches."
    },
    "powerlifting": {
        "title": "Powerlifting",
        "bg_image": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=1600&q=80",
        "importance": "Builds skeletal mass, foundational raw power, and proper kinetic chain biomechanics.",
        "benefits": ["Maximum strength output", "Bone density enhancement", "Posterior chain activation"],
        "arrangements": "Supervised Squat/Bench/Deadlift max tests with certified strength coaches and safety spotters."
    },
    "badminton": {
        "title": "Badminton",
        "bg_image": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=1600&q=80",
        "importance": "One of the fastest racquet sports demanding high anaerobic capacity, rapid spatial reflexes, and kinetic power.",
        "benefits": ["Reflex speed and agility", "Calf and core explosion", "High calorie-burn rate"],
        "arrangements": "Indoor synthetic court tournaments, singles & doubles leagues, and professional footwork clinics."
    },
    "tennis": {
        "title": "Tennis",
        "bg_image": "https://images.unsplash.com/photo-1595435934249-5df7ed86e1c0?auto=format&fit=crop&w=1600&q=80",
        "importance": "Builds whole-body muscular endurance, lateral footwork agility, and tactical point play resilience.",
        "benefits": ["Aerobic & anaerobic fitness", "Rotational core strength", "Precision hand-eye control"],
        "arrangements": "Hard-court rankings matches, weekend grand-slam format tournaments, and ball-machine training sessions."
    }
}ts Database with 3D Rendered Visual References
