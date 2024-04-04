from flask import Flask
import pyqrcode
import png
from pyqrcode import QRCode
from flask import render_template

app = Flask(__name__)


@app.route('/')

def QrCode():
    s   =  ("www.google.com")
    url = pyqrcode.create(s)
    url.png('myqr.png',scale=6)
    return render_template("index.html", QrCode=url)


if __name__=='__main__':
    app.run(debug=True)