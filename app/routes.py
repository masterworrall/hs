from flask import Blueprint, render_template, request, current_app
import os
import json

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html", title="Hackathon")

@bp.route("/details")
def details():
    # read title from query string
    title = request.args.get("title", "").strip()

    # build path to data/registries.json (data folder at project root)
    data_file = os.path.abspath(os.path.join(current_app.root_path, "..", "data", "registries.json"))

    restrictions = []
    try:
        with open(data_file, "r", encoding="utf-8") as f:
            registries = json.load(f)
        # find matching registry
        match = next((r for r in registries if r.get("Title_Register_Number") == title), None)
        if match:
            # Extract only the text and actions we need
            restrictions = [{
                "text": r.get("text", ""),
                "actions": r.get("actions", [])  # Now we can use the actions from JSON if needed
            } for r in match.get("Restrictions", [])]
    except FileNotFoundError:
        restrictions = []
    except Exception as e:
        print(f"Error processing restrictions: {e}")  # Added logging
        restrictions = []

    return render_template("details.html", title=title, restrictions=restrictions)
