#This program generate qr code: 

import pyqrcode
from pyqrcode import QRCode

userLink = "https://www.jw.org/en/bible-teachings/questions/"
url = pyqrcode.create(userLink)
url.svg("myJw.org.png", scale=8)