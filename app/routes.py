from flask import Blueprint, render_template, request

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html", title="Hackathon")

@bp.route("/details")
def details():
    # read title from query string and pass to template
    title = request.args.get("title", "")
    return render_template("details.html", title=title)
