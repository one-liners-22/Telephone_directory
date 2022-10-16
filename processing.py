import read
import view

def main_logic():
    value = 0
    data = read.get_data()
    while value != 4:
        value = view.user_command()
        if value == 1:
            pass
        elif value == 2:
            pass
        elif value == 3:
            view.print_all_contacts(data)
        elif value == 4:
            print('Bay_Bay')
            break
        print(value)
    # else:
    #     # view.bay_bay()
    #     print('Bay_Bay')


    
