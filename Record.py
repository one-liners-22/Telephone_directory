
def save_data(data):
    print(type(data))
    src = "dataBase.txt"
    with open(src, "w", encoding="utf-8") as file:
        for i in data:
            file.writelines("::".join( i.values())) 
       
