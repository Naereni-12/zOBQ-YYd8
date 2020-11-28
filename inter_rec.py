import speech_recognition as sr

print('''Приветсвую
    Для начала тебе нужно ввести имя файл, в который предстоит записывать данные 
    Используй те знаки, которые windows сможет прочитать. Пиши без расширений. 
    Например "Конфиренция от 28 сентября"
''')

name_file = str(input('Введи имя сюда: '))

print('''
    Программа очень чувтвительна к устройствам ввода(микрофонам),
    поэтому лучше выключить телевизор, говорить чётко, и не быстро.
''')


def recoder():
    try:
        time_of_rec = int(input('Сколько секунд идёт запись фрагмента (просто число):'))
    except ValueError:
        print('Непонятно время единичной записи\n'
              'Поэтому будет 1 секунда')
        time_of_rec = 1
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=1) as source:
            print("Запись началась")
            raw_audio = r.listen(source, phrase_time_limit=time_of_rec)
            print("Обработка записи")
            try:
                user_audio = r.recognize_google(raw_audio, language='ru')
            except sr.UnknownValueError:
                print('\nОшибка распознования: скорее всего слишком тихо\n')
                main()
            return user_audio
    except OSError:
        print("\nНе подключен микрофон\n")
        main()


def write_file(text):
    with open(f'D:/{name_file}.txt', 'a') as file:
        file.write(text)


def manage(text_func):
    print("\nВот что прога услышала:\n", text_func)
    print('\nЧтобы закончить с сохранением файла, введи " + " (плюс)\n'
          'Чтобы закончить без сохранения, введи " - " (минус)')
    write_mode = str(input('Режим записи: '))
    if write_mode == '+':
        write_file(text_func)
        main()
    elif write_mode == '-':
        main()
    else:
        print("Неверный режим записи")
        manage(text_func)


def main():
    work_mode = str(input("Для начала работы нажмите Enter "))
    if work_mode != 123:
        manage(recoder())


main()
