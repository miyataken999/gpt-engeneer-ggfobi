from flask import render_template
from .models import Project

def projects():
    projects = [
        Project("Project 1", "This is project 1", "project1.jpg"),
        Project("Project 2", "This is project 2", "project2.jpg"),
        Project("Project 3", "This is project 3", "project3.jpg"),
    ]
    return render_template("projects.html", projects=projects)