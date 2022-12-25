import qrcode
qr=qrcode.make("Please subscribe the Sathish Swag channel")
#data="https://youtube.com/@SathishSwag"
#qr=qrcode.make(data)
qr.save("docpy.png")
qr.show()