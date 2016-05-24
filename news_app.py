# coding: utf-8
from flask import Flask
from flask_bootstrap import Bootstrap
from blueprints.videos import videos_blueprint

app = Flask("samba")
app.config.from_object('settings')
app.register_blueprint(videos_blueprint)
Bootstrap(app)