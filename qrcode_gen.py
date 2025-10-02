import qrcode
print("Link To Qr Code Generator!")
data=input("Enter the link you want to convert into QR code: ")
img=qrcode.make(data) #lmao i named the code qrcode.py and shit imported itself and not the actual qrcode library
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")