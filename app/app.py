from flask import Flask
from .views import home, about, contact, projects

app = Flask(__name__)

@app.route("/")
def index():
    return home()

@app.route("/about")
def about_page():
    return about()

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    return contact()

@app.route("/projects")
def projects_page():
    return projects()

if __name__ == "__main__":
    app.run(debug=True)