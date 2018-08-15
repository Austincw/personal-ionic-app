from flask import Blueprint, render_template, request,jsonify
from email import email

ionic_app = Blueprint('personal-ionic-app', __name__)


@ionic_app.route('/email', methods=['POST'])
def sendContactEmail():

    data = request.get_json(silent=True)

    email_data = data['email']
    message = data['msg']

    email.sendEmail(email_data, message)

    return
