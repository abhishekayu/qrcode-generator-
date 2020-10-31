import qrcode
#for data

data = "https://github.com/imdarkcoder"
#for output

output = "qr.png"

#convert data in to qr

img = qrcode.make(data)

#save output

img.save(output)

#show output

img.show(output)


