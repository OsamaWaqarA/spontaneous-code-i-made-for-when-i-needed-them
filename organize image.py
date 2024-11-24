import os, shutil
file = []

json = []
json_gif = []
json_jpg = []
json_mp4 = []
json_etc = []
json_screenshot = []

notjson = []
notjson_gif = []
notjson_jpg = []
notjson_mp4 = []
notjson_etc = []
notjson_screenshot = []

file = (os.listdir("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023"))
for i in range(0,len(file)):
    if "json" in file[i] :
        json.append(file[i])
    else:
        notjson.append(file[i])

for i in range(0,len(notjson)):
    if ".gif" in notjson[i]:
        notjson_gif.append(notjson[i])
    elif ".jpg" in notjson[i]:
        if "Screenshot" in notjson[i]:
            notjson_screenshot.append(notjson[i])
        else:
            notjson_jpg.append(notjson[i])
    elif ".mp4" in notjson[i]:
        notjson_mp4.append(notjson[i])
    else:
        notjson_etc.append(notjson[i])
        
for i in range(0,len(json)):
    if ".gif" in json[i]:
        json_gif.append(json[i])
    elif ".jpg" in json[i]:
        if "Screenshot" in json[i]:
            json_screenshot.append(json[i])
        else:
            json_jpg.append(json[i])
    elif ".mp4" in json[i]:
        json_mp4.append(json[i])
    else:
        json_etc.append(json[i])

os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\gif")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\jpg")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\screenshot")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\mp4")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\etc")

os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_gif")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_jpg")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_screenshot")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_mp4")
os.makedirs("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_etc")

for i in range(0,len(notjson_gif)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(notjson_gif[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\gif")

for i in range(0,len(notjson_jpg)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(notjson_jpg[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\jpg")

for i in range(0,len(notjson_screenshot)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(notjson_screenshot[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\screenshot")

for i in range(0,len(notjson_mp4)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(notjson_mp4[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\mp4")

for i in range(0,len(notjson_etc)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(notjson_etc[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\etc")

for i in range(0,len(json_gif)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(json_gif[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_gif")

for i in range(0,len(json_jpg)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(json_jpg[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_jpg")

for i in range(0,len(json_screenshot)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(json_screenshot[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_screenshot")
    
for i in range(0,len(json_mp4)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(json_mp4[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_mp4")

for i in range(0,len(json_etc)):
    shutil.move("C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\\"+str(json_etc[i]), "C:\\Users\wabal\Desktop\Dad\Takeout\Google Photos\Photos from 2023\json\json_etc")


print("All done")
    








