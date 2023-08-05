from logger import input_new_note, print_notes, print_one_note, filter_notes_date, delete_note, edit_note

def interface():
    file_name = "data_note.csv"    

    command = -1
    while command != 7:
        print("Выберите действие: \n"
              "1 - Добавить новую заметку\n"
              "2 - Вывести все заметки\n"              
              "3 - Вывести конкретную заметку\n"
              "4 - Вывести заметки, отфильтрованные по дате\n"              
              "5 - Редактировать заметку\n"
              "6 - Удалить заметку\n"
              "7 - Выход\n")
        command = int(input("Введите номер команды: "))

        while command < 1 or command > 7:
            print("Введите команду от 1 до 7")
            command = int(input("Введите номер команды: "))
        
        if command == 1:
            input_new_note()
        elif command == 2:
            print_notes()
        elif command == 3:
            print_one_note()
        elif command == 4:
            filter_notes_date()
        elif command == 5:
            edit_note()        
        elif command == 6:
            delete_note()               
        elif command == 7:
            print("Выход")
            


