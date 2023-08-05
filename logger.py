import csv
from note_create import id_note, title_note, body_note, timestamp_note
from datetime import datetime

# Добавить новую заметку
def input_new_note(): 
    id = id_note("fff")
    title = title_note()
    body = body_note()
    timestamp = timestamp_note()
    with open('data_note.csv', 'a', encoding='utf-8') as file:
        file.write(f'\n{id};{title};{body};{timestamp}')
    print("Заметка успешно сохранена")
    data_notes = print_notes()    

# Вывести все заметки
def print_notes(): 
    print('Вывожу данные из файла\n')
    with open('data_note.csv', 'r', encoding='utf-8') as file:
        data_notes = list(file.readlines())
        data_file = []
        for i in range(len(data_notes)):
            id = data_notes[i].split(";")[0]
            title = data_notes[i].split(";")[1]
            body = data_notes[i].split(";")[2]
            timestamp = data_notes[i].split(";")[3]
            id = i + 1
            data_file += [f"{id};{title};{body};{timestamp}"]
        with open('data_note.csv', 'w', encoding='utf-8') as file:
            file.write(''.join(data_file))
    with open('data_note.csv', 'r', encoding='utf-8') as file:
        data_notes = list(file.readlines())
        print(*data_notes)              
    return data_notes

# Вывести конкретную заметку
def print_one_note(): 
    data_notes = print_notes()
    print("Какую именно запись по идентификатору Вы хотите вывести: ?")
    number_journal = int(input("Введите номер записи: "))
    print(f"Выбранная вами запись\n{data_notes[number_journal - 1]}")

# Вывести заметки, отфильтрованные по дате
def filter_notes_date(): 
    data_notes = print_notes()
    date_filter = datetime.strptime(input("Введите дату для фильтрации заметок (в формате yyyy-mm-dd) в консоль: "), "%Y-%m-%d").date()
    data_file = []
    for i in range(len(data_notes)):
        id = data_notes[i].split(";")[0]
        title = data_notes[i].split(";")[1]
        body = data_notes[i].split(";")[2]
        timestamp = data_notes[i].split(";")[3].rstrip() # убрать пробел в конце
        timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()        
        if timestamp == date_filter:
            data_file += [f"{id};{title};{body};{timestamp}\n"]            
    if len(data_file) != 0:
        print(*data_file)
    else:
        print("Заметки по выбранной дате отсутствуют")
    return data_file

# Редактировать заметку
def edit_note():
    data_notes = print_notes()
    print("Какую именно запись по счету Вы хотите изменить?")
    number_journal = int(input("Введите номер записи: "))
    print(f"Удалить данную запись\n{data_notes[number_journal - 1]}")
    change_line(data_notes, number_journal)

def change_line(dataFile, numberRow):
    answer = input(f"Изменить данную запись\n{dataFile[numberRow - 1]}?\nВведите ответ: да/нет")
    if answer == "да":
        numberRow -= 1
    while answer != "да":
        numberRow = int(input('Введите номер записи: '))
        answer = input(f"Изменить данную запись\n{dataFile[numberRow - 1]}?\nВведите ответ: да/нет")
        numberRow -= 1    
    print(f"Меняем данную запись\n{dataFile[numberRow]}\n")
    
    id = dataFile[numberRow].split(";")[0]
    title = dataFile[numberRow].split(";")[1]
    body = dataFile[numberRow].split(";")[2]
    timestamp = dataFile[numberRow].split(";")[3]

    answer = int(input("Какие данные Вы хотите поменять?\n"
                       "1. Заголовок заметки\n"
                       "2. Тело заметки\n"))
    while answer < 1 or answer > 2:
        print("Вы ошиблись!\nВведите корректный номер от 1 до 2")
        answer = int(input("Какие данные Вы хотите поменять?\n"
                       "1. Заголовок заметки\n"
                       "2. Тело заметки\n"))

    if answer == 1:
        title = title_note()
        timestamp = timestamp_note()
    elif answer == 2:
        body = body_note()
        timestamp = timestamp_note()
    
    data_notes = dataFile[:numberRow] + [f"{id};{title};{body};{timestamp}\n"] + \
                  dataFile[numberRow + 1:]
    with open('data_note.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_notes))
    print('Изменения успешно сохранены!')
    data_notes = print_notes()

# Удалить заметку
def delete_note():
    data_notes = print_notes()
    print("Какую именно запись по счету Вы хотите удалить?")
    number_journal = int(input("Введите номер записи: "))
    print(f"Удалить данную запись\n{data_notes[number_journal - 1]}")
    data_notes = data_notes[:number_journal - 1] + data_notes[number_journal:]    
    with open('data_note.csv', 'w', encoding='utf-8') as file:
        file.write(''.join(data_notes))
    print('Изменения успешно сохранены!')
    data_notes = print_notes()