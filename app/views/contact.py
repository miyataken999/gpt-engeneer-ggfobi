from flask import render_template, request
from .models import Contact

def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        contact = Contact(name, email, message)
        # Save the contact message to a database or send an email
        return "Thank you for contacting us!"
    return render_template("contact.html")