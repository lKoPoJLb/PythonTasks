import os, json
Data = open('python/main.json', 'r', encoding='utf-8')
txt = json.load(Data)

print(txt['entry'])

arr = input("Введите запрос: ").split()
path = os.path.dirname(os.path.abspath(__file__))
Fname, Tname, Tcount = arr[0], arr[1], int(arr[2])+1

def CreatePath(Directory, File_Foler_Name):
    if not os.path.exists(Directory):
        NewPath = os.path.join(path, Fname)
        os.mkdir(NewPath)
        print(txt['files']['foldercreated'])
    return os.path.join(Directory, File_Foler_Name)

for i in range(1, Tcount):
    NewPath = CreatePath(f"{path}/{Fname}", f"{Tname}-{i}.py")
    file = open(NewPath, 'a')
    file.close()

print(txt['files']['filecreated'])

Data.close()