from flask import Flask
from exts import db
from lib.models import AnimeList
from flask_migrate import Migrate
from blueprints.index import bp as index_bp
from blueprints.anime import bp as anime_bp
import config

app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(index_bp)
app.register_blueprint(anime_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)