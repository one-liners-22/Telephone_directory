import read
import Record
import view

def main_logic():
    value = 0
    data = read.get_data()
    while value != 4:
        value = view.user_command()
        if value == 1:
            pass
        elif value == 2:
            contact = view.create_contact()
            Record.save_data(contact)
        elif value == 3:
            view.print_all_contacts(data)
        elif value == 4:
            print('Bay_Bay')
            break
        print(value)

# Поиск по всем контактам строчки введенной пользователем
# Желательно сделать универсальным для поиска дублей при вводе нового контакта
# def what_contact ():
#     str_for_search = view.find_contact() - тут лежит строка
#     str_for_double = view.create_contact() - тут лежит словарь

    
