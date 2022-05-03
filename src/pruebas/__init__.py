from flask import Flask, Config


def create_app(config_class=Config):
   app = Flask(__name__, template_folder="../templates", static_url_path='/static')
   app.config.from_object(config_class)
   return app


app = create_app()

from src.pruebas import basedatos
