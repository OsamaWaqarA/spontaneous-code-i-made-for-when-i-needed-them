from barcode import EAN13
number = ""
from barcode.writer import ImageWriter
print("create your custom 13 dight barcode.")
number = str(input("Type a 13 dight barcode here  "))
my_code = EAN13(number, writer=ImageWriter())
my_code.save("Peanut butter")
import os
import tempfile
filename = tempfile.mktemp(".PNG")
os.startfile("peanut butter.PNG", "print")
