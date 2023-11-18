from flask import Flask, render_template, request, Response  # Mengimpor kelas Flask dan fungsi terkait dari pustaka Flask
from waitress import serve  # Mengimpor fungsi serve dari pustaka waitress
from PIL import Image  # Mengimpor kelas Image dari pustaka PIL (Pillow)
import json  # Mengimpor modul json untuk manipulasi JSON
from snap import detect_objects_on_image  # Import fungsi detect_objects_on_image dari snap.py
from ultralytics import YOLO  # Mengimpor kelas YOLO dari pustaka ultralytics

app = Flask(__name__)  # Membuat objek aplikasi Flask

@app.route("/")
def root():
    return render_template("upload.html")  # Merender template HTML "camera.html"

@app.route("/detect", methods=["POST"])
def detect():
    buf = request.files["image_file"]  # Mengambil file gambar dari permintaan POST
    boxes = detect_objects_on_image(Image.open(buf.stream))  # Mendeteksi objek pada gambar
    return Response(
        json.dumps(boxes),
        mimetype='application/json'
    )

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080, use_reloader=False)  # Menjalankan aplikasi menggunakan waitress pada localhost:8080
