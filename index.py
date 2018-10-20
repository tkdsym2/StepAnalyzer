import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def route():
    return 'root dir'


@app.route('/uploads', methods=['GET', 'POST'])
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            result = {
                "result": {
                    "upload": 'success'
                }
            }
            return jsonify(ResultSet=result)


# app.run(host="127.0.0.1", port=5000, debug=True)
