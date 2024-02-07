# первая задача 
fin=open('students.csv','r',encoding='utf-8')
#название файла,режим открывания файла, в какой кодировке открываем
title=fin.readline()#считали первую строку с заголовками
print(title)
#strip убирает спец символы в нач и конце строки
#split разделим элементы в списках
students=[x.strip().split(',') for x in fin]
fin.close()
#x[0] - порядковый номер 
#x[1] - ФИО
#x[2] - номер проекта
#x[3] - класс
#x[4] - оценка за проект
balsum={}#создали словарь
balcnt={}
#balsum{key - номер класса,value - сумма оценок}
#balcnt{key - номер класса,value - количество оценок}
for x in students:
    if x[4]!="None":#если оценка отсутствует,в алфавитно частотный словарь собираем сумму оценок и их количество
        if x[3] in balsum:
            balsum[x[3]]+=int(x[4])
            balcnt[x[3]]+=1
        else:
            balsum[x[3]]=int(x[4])
            balcnt[x[3]]=1
    
    fio=x[1].split()
    if fio[0]=='Хадаров' and fio[1]=='Владимир':
        print('Ты получил: ',x[4],',',' за проект - ',x[2],sep='')
#или: print(f'Ты получил: {x[4]}, за проект - {x[2]}')

for x in students:
    if x[4]=="None":
        x[4]=f'{balsum[x[3]]/balcnt[x[3]]:.3f}'
#.3f вывести 3 знака после запятой в числе

fout=open('students_new.csv','w',encoding='utf-8')
fout.write(title)
for x in students:
    s=','.join(x)+'\n'
    print(s)
    fout.write(s)
fout.close()
        
