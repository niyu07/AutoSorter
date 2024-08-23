from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# デスクトップのパスを取得
DESKTOP_DIR = os.path.join(os.path.expanduser("~"), "Desktop")
MOVE_TO = os.path.join(DESKTOP_DIR, "sorted_files")

# フォルダが存在しない場合は作成
os.makedirs(MOVE_TO, exist_ok=True)

# 許可する拡張子をセットで定義
ALLOWED_EXTENSIONS = {"txt", "zip", "html", "css", "jpg", "png", "pdf", "mp3", "mp4", "js", "docx", "xlsx", "pptx", "java", "csv", "cpp", "cs"}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort-files', methods=['POST'])
def sort_files():
    if 'files[]' not in request.files:
        return jsonify({'error': 'ファイルが提供されていません'}), 400

    files = request.files.getlist('files[]')
    classified_files = {}

    for file in files:
        if file.filename == '':
            continue

        if not allowed_file(file.filename):
            continue

        filename = secure_filename(file.filename)
        file_extension = filename.rsplit('.', 1)[1].lower()
        folder_name = file_extension if file_extension in ALLOWED_EXTENSIONS else 'others'
        folder_path = os.path.join(MOVE_TO, folder_name)

        # ファイル名の処理
        if '_' in filename:
            filename = filename.split('_', 1)[1]
    

        os.makedirs(folder_path, exist_ok=True)

        destination_path = os.path.join(folder_path, filename)

        try:
            file.save(destination_path)
        except Exception as e:
            return jsonify({'error': f'ファイルのコピー中にエラーが発生しました: {str(e)}'}), 500

        if folder_name not in classified_files:
            classified_files[folder_name] = []
        classified_files[folder_name].append(filename)

    return jsonify({
        'message': 'ファイルが正常に分類され、コピーされました！',
        'classified_files': classified_files
    })

if __name__ == '__main__':
    app.run(debug=True)