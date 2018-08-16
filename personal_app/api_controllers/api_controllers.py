from flask import Blueprint, request
from personal_app.email import emailing

ionic_app = Blueprint('personal_app', __name__)


@ionic_app.route('/email', methods=['POST'])
def sendContactEmail():

    data = request.get_json(silent=True, force=True)

    email_data = data['email']
    message = data['msg']

    emailing.sendemail(email_data, message)

    return
