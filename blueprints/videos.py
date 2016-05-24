# coding: utf-8
import os
from werkzeug import secure_filename
from flask import (
    Blueprint, request, current_app, send_from_directory, render_template
)
from db import videos

videos_blueprint = Blueprint('videos', __name__)


@videos_blueprint.route("/videos/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        video = request.files.get('video')

        if video:
            filename = secure_filename(video.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            video.save(path)
            dados_do_formulario['video'] = filename

        id_novo_video = videos.insert(dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                               id_novo_video=id_novo_video)

    return render_template('cadastro.html', title=u"Inserir novo video")


@videos_blueprint.route("/")
def index():
    todos_os_videos = videos.all()
    return render_template('index.html',
                           videos=todos_os_videos,
                           title=u"Todos os vídeos")


@videos_blueprint.route("/video/<int:video_id>")
def video(video_id):
    video = videos.find_one(id=video_id)
    return render_template('video.html', video=video)


@videos_blueprint.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)
