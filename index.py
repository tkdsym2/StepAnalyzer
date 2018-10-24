import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from Analyzer import AnalyzedDescription
from AudioToText import TranscriptNarration
from ExtractAudio import GetAudio

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'raw', 'flac'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['JSON_AS_ASCII'] = False


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def route():
    return 'root dir'


@app.route('/analyze', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)  # mp4
            convert_file = GetAudio(filepath, filename)
            _transcript = TranscriptNarration(audiofile=convert_file)
            _result = AnalyzedDescription(_transcript)
            result = {
                'data': _result
            }
            return jsonify(result)


# app.run(host="127.0.0.1", port=5000, debug=True)
