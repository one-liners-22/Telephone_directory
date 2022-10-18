# Актуальный код

def save_data (for_rec):
    src = 'dataBase.txt'
    convert_data = []
    for i in for_rec:
        convert_data.append(i)
        save_convert_data_str = '::'.join(convert_data)
        with open(src, 'a', encoding = 'utf-8') as file:
              file.writeline(save_convert_data_str)
        print(f'Контакт {save_convert_data_str} сохранен в {src}')
    return save_convert_data_str



# пример

# src = "dataBase.txt"
# def save_data(for_rec):
    
#     conver_data = " " 

#     # with open(src, "a",encoding="utf-8") as file:
#     #     file.writeline(conver_data)
#     print(f"Контакт {conver_data}, сохранен в {src}")

# Образец for_rec {'id': '0000007', 'secondname': 'Ли', 'name': 'Борис', 'lastname': '-1', 'Phone number': '-1', 'comment': 'Обработка, controller\n'}
# Образец conver_data = "0000010::Яковлев::Александр::Михайлович::+79507355238::-1" +"\n"
