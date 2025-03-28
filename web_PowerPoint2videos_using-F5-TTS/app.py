from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for
import uuid
import os

app = Flask(__name__, static_folder="static", static_url_path="/static", template_folder="templates")

# set path
UPLOAD_FOLDER = 'uploads'
AUDIO_FOLDER = os.path.join(UPLOAD_FOLDER, 'audio')
PPT_FOLDER = os.path.join(UPLOAD_FOLDER, 'ppt')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)
os.makedirs(PPT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    audio_file = request.files.get("audio")
    if not audio_file:
        return jsonify({"error": "No audio file provided"})
    
    ext = os.path.splitext(audio_file.filename)[1]
    filename = str(uuid.uuid4()) + ext
    save_path = os.path.join(AUDIO_FOLDER, filename)
    audio_file.save(save_path)

    return jsonify({
        'message': 'Audio uploaded successfully',
        'filename': filename
    })

@app.route('/upload_PPT', methods=['POST'])
def upload_ppt():
    ppt_file = request.files.get("ppt")
    if not ppt_file:
        return jsonify({"error": "No ppt file provided"})
    
    ext = os.path.splitext(ppt_file.filename)[1]
    filename = str(uuid.uuid4()) + ext
    save_path = os.path.join(PPT_FOLDER, filename)
    ppt_file.save(save_path)

    return jsonify({
        'message': 'PPT uploaded successfully',
        'filename': filename
    })

# # 访问http://127.0.0.1:5000/index                       GET请求
# @app.route('/index', methods=["POST", "GET"])
# def index():
#     # get请求: 传输到URL中
#     # http://127.0.0.1:5000/index?age=18&pwd=123 GET请求
#     age = request.args.get("age")
#     pwd = request.args.get("pwd")
#     print(age, pwd)
    
#     # post请求: 传输到请求体中
#     # 请求体: xx=123 yy=999
#     xx = request.form.get("xx")
#     yy = request.form.get("yy")
#     print(xx, yy)

#     # json请求: 传输到请求体中
#     # json：  {"xx":123,"yy":999}
#     data = request.json
#     # data = request.get_json()
#     print(data)

#     # 返回json
#     # import json
#     # return json.dumps({"status":True, "msg":"ok"})
#     return jsonify({"status":True, "msg":"ok"})

# # 访问http://127.0.0.1:5000/home
# @app.route('/home')
# def home():
#     return "here"

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)