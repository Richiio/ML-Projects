import imp
import ExercisesModule as trainer
import EmailingSystem as email_sys
import DatabaseSys as db_sys
import AudioCommSys as audio_sys

from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__, template_folder= 'template')

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/configure')
def configure():
    return render_template("/configure.html")

def gen_camera(camera):
    while(True):
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type:')