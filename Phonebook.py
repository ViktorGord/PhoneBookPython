phonebook = {}
import json
print("Телефонный справочник. Краткое руководство\n" #будут перечислены команды, которые повзовляют рабоать со справочником
     "1. show (вывести телефонный справочник);\n"
     "2. new (добавить новую запись в справочник);\n"
     "3. search (поиск по справочнику);\n"
     "4. change (скорректировать запись в справочнике);\n"
     "5. del (удалить запись из справочника);\n"
     "6. export (выгрузить справочник во внешний файл).\n")
while True:
    command = input("Введите команду: ")
    if command =="show": 
        if len(phonebook) == 0:
            print("В телефонном справочнике не содержится записей.")
        else:
            for surname, values in phonebook.items():
                print(name, values)
    elif command =="new":
        name = input("Введите имя абонента: ")
        surname = input("Введите фамилию абонента: ")
        phonenum = input(f"Введите телефон {surname} {name}: ")
        person_info = {'surname': {surname}, 'name': {name}, 'phonenumber': {phonenum}}
        phonebook[surname] = person_info 
        print()
    elif command =="search":
        caller = input("Введите фамилию абонента: ") 
        if caller in phonebook:
                print(phonebook[caller])
        else:
             print(f"Абонент {caller} в справочнике не найден")
else: print("Такой команды не существует. Введите команду из краткого руководства")