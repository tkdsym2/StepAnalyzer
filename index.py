# coding: utf-8

import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from Analyzer import AnalyzedDescription
from AudioToText import TranscriptNarration
from ExtractAudio import GetAudio
from Downloader import DownloadMovie, DownloadThumb
from UploadStorage import UploadGStorage
from ExtractImage import MovieToFrame
from SanitizeResult import SanitizeYOLOResult, CombineResults
from BackgroundSubstraction import GetDiffPoint
from ImagePlotter import DrawingDetectonRect
# from darknet import detectionImage

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def route():
    return 'root dir'


@app.route('/analyze', methods=['POST'])
def upload_url():
    movie_url = request.form['movie_url']
    print(movie_url)
    movie_filepath = DownloadMovie(movie_url)
    movie_filename = movie_url.split('/')[-1].split('.')[0]
    convert_file = GetAudio(movie_filepath, movie_filename)
    gsutilpath = UploadGStorage(convert_file)
    _transcript = TranscriptNarration(gsutilpath)
    transcript_result = AnalyzedDescription(_transcript)
    # -------
    thumb_url = request.form['thumb_url']
    thumb_filepath = DownloadThumb(thumb_url)
    thumb_filename = thumb_url.split('/')[-1].split('.')[0]
    detection_result = detectionImage(thumb_filepath)
    # ------
    result = {
        'transcription': transcript_result,
        'detection': detection_result
    }
    return jsonify(result)


@app.route('/analyze/narration', methods=['POST'])
def upload_movie_url():
    movie_url = request.form['movie_url']
    movie_filepath = DownloadMovie(movie_url)
    movie_filename = movie_url.split('/')[-1].split('.')[0]
    convert_file = GetAudio(movie_filepath, movie_filename)
    gsutilpath = UploadGStorage(convert_file)
    _transcript = TranscriptNarration(gsutilpath)
    transcript_result = AnalyzedDescription(_transcript)
    result = {
        'transcript_result': transcript_result
    }
    return jsonify(result)


@app.route('/analyze/detection', methods=['POST'])
def upload_thumb_url():
    # thumb_url = request.form['thumb_url']
    # thumb_filepath = DownloadThumb(thumb_url)
    # thumb_filename = thumb_url.split('/')[-1].split('.')[0]
    # detection_result = detectionImage(thumb_filepath)
    movie_url = request.form['movie_url']
    movie_filepath = DownloadMovie(movie_url)
    movie_filename = movie_url.split('/')[-1].split('.')[0]
    frame_name = MovieToFrame(movie_filepath, movie_filename)
    diff_list = GetDiffPoint(frame_name)
    yolo_detected_list = []
    combined_result = CombineResults(diff_list, yolo_detected_list)
    DrawingDetectonRect(frame_name, movie_filename, diff_list)
    result = {
        'detection': combined_result
    }
    return jsonify(result)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000, debug=True)
