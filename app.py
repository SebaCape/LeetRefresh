from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

import os

# Port definition for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_question", methods=["POST"])
def get_question():
    try:
        data = request.get_json()
        mode = data.get("mode")  # "review" or "new"
        difficulty = (data.get("difficulty") or "").lower()
        all_problems = data.get("problems", [])

        completed_problems = [p for p in all_problems if p.get("status") == "ac"]
        unsolved_problems = [p for p in all_problems if p.get("status") != "ac"]

        if mode == "review":
            pool = completed_problems
        else:
            pool = unsolved_problems

        # Filter by difficulty if provided
        if difficulty in ["easy", "medium", "hard"]:
            level_map = {"easy": 1, "medium": 2, "hard": 3}
            pool = [p for p in pool if p["difficulty"]["level"] == level_map[difficulty]]

        if not pool:
            return jsonify({"error": "No questions available for the selected options."})

        question = random.choice(pool)
        return jsonify({
            "title": question["stat"]["question__title"],
            "link": f"https://leetcode.com/problems/{question['stat']['question__title_slug']}/",
            "difficulty": {1: "easy", 2: "medium", 3: "hard"}[question["difficulty"]["level"]]
        })
    except Exception as e:
        return jsonify({"error": str(e)})
    
if __name__ == "__main__":
    app.run(debug=True)
