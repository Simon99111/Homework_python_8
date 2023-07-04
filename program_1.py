data = 'telephone.txt'
columns = ['Фамилия' , 'Имя' , 'Телефон']

def ReadFile(data: str):
    newdata = []
    with open(data, 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(columns, line.strip().split(',')))
            newdata.append(record)
    return newdata

def SaveData(data, newdata):
     with open(data, 'w', encoding='utf-8')as f:
        for i in range(len(newdata)):
            s=''
            for v in newdata[i].values():
                s+= v + ','
            f.write(f'{s[:-1]}\n')

def PrintData():
    newdata = ReadFile(data)
    number = 0
    print('Данные справочника:')
    for i in newdata:
        number += 1
        print(f'{number}', end = '. ')
        print(*i.values())

def Search():
    while True:
        print('Меню поиска')
        for i in range(len(columns)):
            print(f'{i} - поиск по полю {columns[i]}')
        print(f'{len(columns)} - Главное меню')
        answer = int(input('Номер меню: '))
        if answer == len(columns): break
        if 0 <= answer <len(columns):
            searched = input('Поиск значения')
            SearchData(searched, answer)

def SearchData(searchedData, fieldNumber): 
    phoneDirectory = ReadFile(data)
    tick = 0
    print('Результаты: ')
    for line in phoneDirectory:
        i += 1
        if searchedData.lower() in line[columns[fieldNumber]].lower:
            find = True
            print(f'{i}', end=" ")
            print(*line.values())
    if find == False: print(f'{searchedData} не найдена')

def NewPerson():
    phoneDirectory = ReadFile(data)
    newRecord = dict()
    for i in range(len(columns)):
        newRecord[columns[i]]=(input(f'Введите данные по полю "{columns[i]}": '))
    phoneDirectory.append(newRecord)
    SaveData(data, phoneDirectory)

def Edit():
    PrintData()
    Index = int(input('Номер редактируемой записи: '))-1
    print(*enumerate(columns))
    fieldsIndex = int(input('Номер поля для редактирования: '))
    phoneDirectory = ReadFile(data)
    phoneDirectory[Index][columns[fieldsIndex]] = input('Новые данные: ')
    SaveData(data, phoneDirectory)

def Delete():
    PrintData()
    recIndex = int(input('Номер удаляемой записи: '))-1
    phoneDirectory = ReadFile(data)
    phoneDirectory.pop(recIndex)
    SaveData(data, phoneDirectory)


def main():
    while True:
        print('Меню:')
        print('0 - Все данные')
        print('1 - Меню поиска')
        print('2 - Новая запись')
        print('3 - Редактировать запись')
        print('4 - Удалить запись')
        print('5 - Выйти из программы')
        my_choice = int(input())
        if my_choice == 5:
            return
        elif my_choice == 0:
            PrintData()
        elif my_choice == 1:
            Search()
        elif my_choice == 2:
            NewPerson()
        elif my_choice == 3:
            Edit()
        elif my_choice == 4:
            Delete()
        
        


if __name__ == '__main__':
    main()