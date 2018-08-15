from flask import Blueprint, render_template, request

ionic_app = Blueprint('personal-ionic-app', __name__)


@ionic_app.route('/email', methods=['GET', 'POST'])
def sendContactEmail():
    return "Hello, World!"