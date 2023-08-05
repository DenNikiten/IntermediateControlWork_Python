import datetime

def id_note(notes):
    id = len(notes)
    return id

def title_note():
    title = input("Введите заголовок: ")
    return title

def body_note():
    body = input("Введите тело заметки: ")
    return body

def timestamp_note():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp