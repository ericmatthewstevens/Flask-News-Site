from flask import Flask, Blueprint, render_template, request, redirect, url_for

views = Blueprint("views", __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/home')
def home():
    return render_template("home.html")