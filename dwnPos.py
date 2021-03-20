import requests
import os


results = []
root_path = "Z:\Film Bioskop & Film Seri\_Film Terbaru_\TAHUN 2021\FILM TERBARU BULAN FEBRUARI 2021"
file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]


for path, files in file_index:
    for file in files:
        if(file.lower().endswith(".mp4") or file.lower().endswith(".mkv")):
            result = path + "/" + file
            results.append(result)


for result in results:
    splited = os.path.split(result)
    splitedSecond = splited[1]
    splitedName = splitedSecond[:splitedSecond.index("(") - 1]

    title = splitedName
    URL = "http://www.omdbapi.com/?apikey=47bb3c38&t=" + title
    r = requests.get(url = URL) 
    data = r.json()
    
    check = data.get("Poster")
    
    if check:
        poster = data["Poster"]
    else:
        print(title)
        continue
    

    if(poster == "N/A"):
        print(title)
        continue
        
    response = requests.get(poster)

    posterName = splited[0] + "\\" + splitedName + ".png"
    

    if os.path.exists(posterName):
            continue
            
    file = open(posterName, "wb")
    file.write(response.content)
    file.close()
    