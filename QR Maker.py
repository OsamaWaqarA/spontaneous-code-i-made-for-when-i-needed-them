import qrcode
text = input("Text here  ")
img = qrcode.make(text)
type(img)  # qrcode.image.pil.PilImage
file = input("What is the file name  ")
img.save(file+".png")
