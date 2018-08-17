from flask import Blueprint, request, jsonify
from personal_app.email import emailing

ionic_app = Blueprint('personal_app', __name__)


@ionic_app.route('/email', methods=['POST'])
def sendContactEmail():
    try:
        data = request.get_json(silent=True, force=True)

        email_data = data['email']
        message = data['msg']

        return emailing.sendemail(email_data, message)

    except Exception as e:
        print(e)
        return str(e)

