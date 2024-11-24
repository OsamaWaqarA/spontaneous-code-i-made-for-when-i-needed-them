from pyzbar import pyzbar
import cv2
import subprocess
import pygame
chrome = "C:\Program Files\Google\Chrome\Application\chrome.exe"
barcode_info = ""
file = open("barcode_result.txt","w")
file.close()

def read_barcodes(frame, dec):
    barcode_info = ""
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        
        with open("barcode_result.txt", mode ='w') as file:
            file.write(barcode_info)
    return frame,dec

def main():
    
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    dec = False
    ans = "" 
    read = []
    
    while ret:
        ret, frame = camera.read()
        frame, dec = read_barcodes(frame ,dec)
        cv2.imshow('Barcode/QR code reader', frame)
        code = ""
        file = open("barcode_result.txt","r")
        code = str(file.readline())
        file.close()
        file = open("barcode_DataBase.txt","r")
        cek = False
        if dec == False:
            print(ans)
            while cek == False:
                get = file.readline()
                if "EOF" in get:
                    #print("error: No histroy")
                    cek = True
                else:
                    mark1 = int(get.find("#"))
                    mark2 = int(get.find("*"))
                    mark3 = int(get.find("%"))
                    check = str(get[0:mark1])
                    if code == check:
                        code = ""
                        dec = True
                        cek = True
                        code = ""
                        ans = (get[mark1:mark2], " price of ", get[mark2:mark3])
        file.close()
        if dec == True:
            print(ans)
            dec = False
        if "OPENPY:" in code:
            command = str(code[7:(len(code))])
            
            subprocess.run(["python.exe",command])
            code = ""
            file = open("barcode_result.txt","w")
            file.close()
                    
        if cv2.waitKey(1) & 0xFF == 27:
            camera.release()
            cv2.destroyAllWindows()
            break
                
                

if __name__ == '__main__':
    main()
    #file = open("barcode_result.txt","r")
    #code = file.readline()
    #print(code)
    #file.close()
    #subprocess.Popen([chrome,"https://www.google.com/search?q="+code])
    
