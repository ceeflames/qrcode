import qrcode
import image

#input the url:

I= input("Type in url:")
print("QRcode stored:", I)

def generate(data, img_name='qrcode.png'):
    img = qrcode.make(data)
    img.save(img_name)
    print(img)

generate(I)
