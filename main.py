import os

v = int(input("Количество файлов."))

for i in range(1, v+1):
    path = f"{os.getcwd()}/python"
    NewPath = os.path.join(path, f"{i}.py")
    open(NewPath, "a")
