from flask import Flask

from api_controllers.api_controllers import ionic_app

app = Flask(__name__)


def register_blueprints(my_app):

    my_app.register_blueprint(ionic_app)


register_blueprints(app)

