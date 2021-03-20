import os

#print(len("Z:\Film Bioskop & Film Seri\_Film Terbaru_\TAHUN 2021\FILM TERBARU BULAN JANUARI 2021\Crayon Shinchan Honeymoon Hurricane The Lost Hiroshi (JPN) (2019)\Crayon Shinchan (Animation, Action, Adventure, Family) (2019).mp4"))

results = []
root_path = "Z:\Film Bioskop & Film Seri\_Film Terbaru_"
file_index = [(root, files) for root, dirs, files in os.walk(root_path) if files]
num = 0

for path, files in file_index:
    for file in files:
        if(file.lower().endswith(".mp4") or file.lower().endswith(".mkv")):
            result = path + "/" + file
            length = len(result)
            if(length > 223):
                results.append(result)
                num += 1
        



with open('Note.txt', 'w') as file:
    for result in results:
        file.write(result + "\n")
        
print(num)