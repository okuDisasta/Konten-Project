import requests
import os 

#titles = ["sound of metal", "rage", "armageddon tales", "body brokers", "enforcement", "i'll meet you there", "love in the forecast", "narco soldiers", "shock wave 2", "the donkey king"]
titles = ["love, lost & found", "raya and the last", "coming 2 america", "miss juneteenth", "land", "dragon rider", "moxie", "the mauritanian", "anastasia", "biggie", "cosmic sin", "adverse", "the girl on the train", "crazy about her", "forever love", "last call", "black beach", "tom and jerry", "strip down, rise up", "the speed cubers"]

parent_dir = "D:/Konten Ridwan/film"
path = ""


try:
    for title in titles:
        URL = "http://www.omdbapi.com/?apikey=47bb3c38&t=" + title
        r = requests.get(url = URL) 
        data = r.json()
        print(data["Title"])
        country = ""
        if data["Country"] == "N/A":
            country = ""
        elif data["Country"] != "USA":
            country = " (" + data["Country"] + ")"
        
        
        dir_title = data["Title"].replace(":", "").replace("-","") + " (" + data["Genre"] + ")" + country + " (" + data["Year"] + ")"
        #print(dir_title)
        
        path = os.path.join(parent_dir, dir_title)
        if os.path.exists(path):
            continue
            
        os.mkdir(path) 
        
except Exception as e:
    print(e)
    
 

if os.listdir(path) == []: 
    print("No files found in the directory.") 
else: 
    results = []
    root_path = "D:/Konten Ridwan/film"
    file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]


    for path, files in file_index:
        for file in files:
            result = path + "/" + file
            results.append(result)
            

    for result in results:        
        splited = os.path.split(result)
        splitedDir = os.path.split(splited[0])

        old_name = result
        new_name = splited[0] + "/" + splitedDir[1] + ".mp4"
        os.rename(old_name, new_name)



    for path, files in file_index:
        year = " " + path.split(" ")[-1]
        pathFolder = path[:path.index("(") - 1]
        folderName = os.path.split(pathFolder)
        title = folderName[1]
        
        URL = "http://www.omdbapi.com/?apikey=47bb3c38&t=" + title
        r = requests.get(url = URL) 
        data = r.json()
        print(data["Title"])
        country = ""
        if data["Country"] == "N/A":
            country = ""
        elif data["Country"] != "USA":
            country = " (" + data["Country"] + ")"
            
        old_name = path
        new_name = pathFolder + country + year
        
        os.rename(old_name, new_name)