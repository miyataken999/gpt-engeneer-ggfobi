from flask import render_template
from .models import Company

def home():
    company = Company(name="Web Development Company", description="We build amazing websites!")
    return render_template("home.html", company=company)