from flask import Flask, render_template
from flask_cors import CORS
from src.controllers.telegram_controller import TelegramController
import os

def create_app() -> Flask:
    template_dir = os.path.dirname(os.path.realpath(__file__))
    template_dir = os.path.join(template_dir, '../templates')
    app = Flask(__name__, template_folder=template_dir)
    _ = CORS(app, resources={r"/": {"origins": ""}})

    app.add_url_rule("/telegram", methods=["POST"], view_func=TelegramController.send_message)
    app.add_url_rule("/", methods=["GET"], view_func=lambda: render_template("swaggerui.html"))
    return app