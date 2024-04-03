from flask import Flask
import pyqrcode
import png
from pyqrcode import QRCode

app = Flask(__name__)


@app.route('/')

def QrCode():
    s   =  input()
    url = pyqrcode.create(s)
    url.png('myqr.png',scale=6)
    return "<img src='myqr.png'/>"


if __name__=='__main__':
    app.run(debug=True)