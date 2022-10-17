def user_command():                                              ## Ф, которую запрашивает контроллер для цифры юзера
    num = int(input("Input \n 1. If You want to find a contact \n 2. If You want to create a new contact \n 3. If You want to see all contacts:   \n 4. If You want to close the programm: \n"))
    if 0 < num < 5:
        return num
    else:
        print("Incorrect number! The programm will be closed.")
        return 4

# # print(user_command())


def find_contact():
    find_me = input('Input contacts firstname: ')
    return find_me



def create_contact():
    new_contact = {'secondname': input('Input Secondname or press "enter" in case if you do not want to add it: ')}
    new_contact['name'] =  input('Input Firstname: ')
    while new_contact['name'] == '':
        new_contact['name'] =  input('Input Firstname: ')
    new_contact['lastname'] = input('Input Lastname or press "enter" in case if you do not want to add it: ')
    new_contact['phone_number'] =  input('Input phone number without + sign: ')
    print(new_contact.get('phone_number').isdigit() and new_contact.get('phone_number')[0] == "+")
    new_contact['comment'] = input('Leave a comment here or press "enter" in case if you do not need it: ')
    return new_contact

# print(create_contact())





from tabulate import tabulate                                       ## Таблица для вывода всех контактов

def print_all_contacts(data):
    data_to_print = []

    for i in range(len(data)):
        listik = list(data[i].values())
        listik.pop(0)
        data_to_print.append(listik)
        
       

    col_names = ["Firstname", "Lastname", "Middlename", "Phone number", "Comment"]
    print(data_to_print)
    print(tabulate(data_to_print, headers=col_names, tablefmt="fancy_grid", showindex="never"))

# #print_all_contacts(data)

