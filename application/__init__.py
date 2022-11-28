from flask import Flask, render_template
from flaskwebgui import FlaskUI
from application.db_controller import create_db


app = Flask(__name__)
ui = FlaskUI(app=app,
             server="flask",
             port=5000,
             fullscreen=True,
             browser_path="chromium")

# Create de database if not exists
create_db()


@app.errorhandler(404)
def not_found(error):
    title = "404 Page not found"
    return render_template('404.html', title=title), 404


@app.errorhandler(500)
def server_error(error):
    title = "500 Server Error"
    return render_template('500.html', title=title), 500


import application.manager
