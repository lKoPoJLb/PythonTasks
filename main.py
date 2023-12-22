import os

print("Команда для создания номера заданий. Писать через пробел./n<FolderName> <TaskName> <TaskCounts>")

arr = input("Введите запрос: ").split()
path = f"{os.getcwd()}/python"
Fname, Tname, Tcount = arr[0], arr[1], int(arr[2])+1

def CreatePath(path, name):
    return os.path.join(path, name)

if os.path.exists(path):
    for i in range(1, Tcount):
        NewPath = CreatePath(f"{path}/{Fname}", f"{Tname}-{i}.py")
        open(NewPath, "a")
else:
    NewPath = CreatePath(path, Fname)
    os.mkdir(NewPath)
    
    for i in range(1, Tcount):
        NewPath = CreatePath(f"{path}/{Fname}", f"{Tname}-{i}.py")
        open(NewPath, "a")