from flask import Flask, render_template, request
import pyqrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", url="")

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        site = request.form['site']
        if site:
            url = pyqrcode.create(site)
            # Save the QR code as a temporary file (or in memory) to serve to the frontend
            # For simplicity, we'll encode the QR code image as a data URI directly in HTML
            qr_as_base64 = url.png_as_base64_str(scale=6)
            return qr_as_base64
    return ''

