import os
import pandas as pd
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd() + '/upload')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['table']
    file.filename = 'file.csv'
    savePath = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(savePath)
    return 'Upload feito com sucesso'


@app.route('/correlations-analysis', methods=['GET'])
def pearson_correlation():
    data = pd.read_csv(os.path.join(UPLOAD_FOLDER, 'file.csv'))
    corr = data.corr()
    return jsonify(corr.to_dict())


if __name__ == '__main__':
    app.run(debug=True)
