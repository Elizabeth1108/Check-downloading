# первая задача 
fin=open('students.csv','r',encoding='utf-8')
#название файла,режим открывания файла, в какой кодировке открываем
title=fin.readline()#считали первую строку с заголовками
print(title)
#strip убирает спец символы в нач и конце строки
#split разделим элементы в списках
students=[x.strip().split(',') for x in fin]
#x[0] - порядковый номер 
#x[1] - ФИО
#x[2] - номер проекта
#x[3] - класс
#x[4] - оценка за проект
fin.close()#закрыли файл
for i in range(1,len(students)):
    for j in range(i,0,-1):
        x=students[j]
        if students[j][4]<students[j-1][4]:
            students[j],students[j-1]=students[j-1],students[j]
        else:
            break
cnt=0
print('10 класс: ')
for x in students:
    if '10' in x[3]and x[4]=='5':
        cnt+=1
        fio=x[1].split()
        print(f'{cnt} место: {fio[1][0]}.{fio[0]}')
        if cnt==3:
            break
