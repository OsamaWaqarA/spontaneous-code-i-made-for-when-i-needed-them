from pyzbar import pyzbar
import cv2
barcode_info = ""

def read_barcodes(frame, dec):
    barcode_info = ""
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        if barcode_info != "":
            dec = True
        else:
            barcode_info = ""

        print(barcode_info)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        
        with open("barcode_result.txt", mode ='w') as file:
            file.write(barcode_info)
    return frame,dec

def main():
    
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    dec = False
    read = []
    
    while ret:
        ret, frame = camera.read()
        frame, dec = read_barcodes(frame ,dec)
        cv2.imshow('Barcode/QR code reader', frame)
        code = 0
        file = open("barcode_result.txt","r")
        code = file.readline()
        file.close()
        file = open("barcode_DataBase.txt","r")
        if dec == True:
            while dec == True:
                get = file.readline()
                print(get)
                if "EOF" in get:
                    dec = False
                    file.close()
                    read = [""]
                    count = 0
                    camera.release()
                    cv2.destroyAllWindows()
                    pname = str(input("What is the Product Name with Detail "))
                    price = str(input("what is the price "))
                    detail = str(code)+"#"+str(pname)+"*"+str(price)+"%"+'\n'
                    file = open("barcode_DataBase.txt","r")
                    while True:
                        read.append(file.readline())
                        count += 1
                        if "EOF" in read[count]:
                            read[count] = detail
                            read.append("EOF")
                            file.close()
                            file = open("barcode_DataBase.txt","w")
                            for i in range(0,count+2):
                                print(read[i])
                                file.write(read[i])
                            file.close()
                            break
                #if dec == True:
                    #mark1 = int(get.find("#"))
                    #mark2 = int(get.find("*"))
                    ##mark3 = int(get.find("%"))
                    #check = int(get[0:mark1])
                    #if check == code:
                        #print("What i wron with you????")
                    #if get == "EOF":
                        #file.close()
                    
        if cv2.waitKey(1) & 0xFF == 27:
            camera.release()
            cv2.destroyAllWindows()
            break
                
                

if __name__ == '__main__':
    main()
