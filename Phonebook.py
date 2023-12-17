phonebook = {}
import json
print("Телефонный справочник. Краткое руководство\n" #будут перечислены команды, которые повзовляют рабоать со справочником
     "1. show (вывести телефонный справочник);\n"
     "2. new (добавить новую запись в справочник);\n"
     "3. search (поиск по справочнику);\n"
     "4. export (выгрузить справочник во внешний файл);\n"
     "5. import (импортировать данные в телефонный справочник);\n"
     "6. exit (выход из справочника);\n"
     )
while True:
    command = input("Введите команду: ")
    if command =="show": 
        if len(phonebook) == 0:
            print("В телефонном справочнике не содержится записей.")
        else:
            for surname, values in phonebook.items():
                print(name, values)
    elif command =="new":
        name = input("Введите имя абонента: ")#имя
        patronymic = input("Введите отчество абонента: ")#отчество
        surname = input("Введите фамилию абонента: ")#фамилия  
        phonenum = input(f"Введите телефон {surname} {name}: ")#номер телефона
        person_info = {'surname': {surname}, 'name': {name}, 'patronymic': {patronymic}, 'phonenumber': {phonenum}}
        phonebook[surname] = person_info 
        print()
    elif command =="search":
        caller = input("Введите фамилию абонента: ") 
        if caller in phonebook:
            print(phonebook[caller])
        else:
            print(f"Абонент {caller} в справочнике не найден")
    elif command =="export":
        with open ("/Users/viktor/Desktop/Learn/GeekBrains/5. Python/PhoneBook/phonebook_Viktor.json", "w") as outfile:
            json.dump(phonebook, outfile, indent=4)
            print("Файл успешно экспортирован")
    elif command =="import": 
        with open ("/Users/viktor/Desktop/Learn/GeekBrains/5. Python/PhoneBook/phonebook_Viktor.json", "r") as inputfile:
            infjson = inputfile.read()
            phonebook = json.loads(infjson) 
            print("Файл успешно импортирован") 
    elif command =="exit":  
        exit()
else: print("Такой команды не существует. Введите команду из краткого руководства")