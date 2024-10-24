from flask import Flask, send_from_directory

from config import Config, load_config
from pages.main import main_bp

app = Flask(__name__)


# Маршруты
def register_blueprints(app_obj: Flask) -> None:
    app_obj.register_blueprint(main_bp, url_prefix='/')


@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('pages/templates/assets', path)


if __name__ == '__main__':
    register_blueprints(app_obj=app)
    conf: Config = load_config()
    app.config['API_KEY'] = conf.api_key
    app.config['API_URL'] = conf.api_url
    app.run(host=conf.host, port=conf.port)
