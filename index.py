import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from Analyzer import AnalyzedDescription
from AudioToText import TranscriptNarration
from ExtractAudio import GetAudio
from Downloader import DownloadMovie
from UploadStorage import UploadGStorage

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def route():
    return 'root dir'


@app.route('/analyze', methods=['POST'])
def upload_url():
    url = request.form['url']
    filepath = DownloadMovie(url)
    filename = url.split('/')[-1].split('.')[0]
    convert_file = GetAudio(filepath, filename)
    gsutilpath = UploadGStorage(convert_file)
    _transcript = TranscriptNarration(gsutilpath)
    _result = AnalyzedDescription(_transcript)
    result = {
        'data': _result
    }
    return jsonify(result)


# app.run(host="127.0.0.1", port=5000, debug=True)
