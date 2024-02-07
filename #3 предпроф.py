fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()
students=[x.strip().split(',')for x in fin]
#x[0] - порядковый номер 
#x[1] - ФИО
#x[2] - номер проекта
#x[3] - класс
#x[4] - оценка за проект
fin.close()#закрыли файл
while True:
    n=input('Введите номер проекта(или СТОП):')
    if n.upper()=='СТОП':
        break
    for x in students:
        if x[2]==n:
            fio=x[1].split()
            print(f'Проект № {x[2]} делал: {fio[1][0]}.{fio[0]} он(а) получил(а) оценку - {x[4]}.')
            break
    else:
        print('Ничего не найдено.')

    
