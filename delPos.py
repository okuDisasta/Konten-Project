import requests
import os




results = []
root_path = "Z:\Film Bioskop & Film Seri\_Film Terbaru_\TAHUN 2021\FILM TERBARU BULAN JANUARI 2021"
file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]


for path, files in file_index:
    for file in files:
        if(".png" in file.lower()):
            result = path + "/" + file
            results.append(result)
print(results)

'''
for result in results:        
    os.remove(result)
'''
    