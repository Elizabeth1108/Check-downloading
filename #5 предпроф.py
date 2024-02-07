#хэш любую числовую последовательность превращает в символьную
#p=67 - условие
#m=10**9+9 - условие
#enumerate(строка,c какого номера начать ид) - выдаёт индекс элемента и его значение

def hashstr(st):
    p=67
    m=10**9+9
    alfabet='ёйцукенгшщзхъфывапролджэячсмитьбю ЁЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ'
    d={}#создали словарь символов
    for ind, simbol in enumerate(alfabet,1):
        d[simbol]=ind
    hashname=0
    for i in range(len(st)):
        hashname+=d[st[i]]*p**i
    return hashname%m

fin=open('students.csv','r',encoding='utf-8')
title=fin.readline()

students=[x.strip().split(',') for x in fin]

fout=open('students_with_hash.csv','w',encoding='utf-8')
fout.write(title)
# x[0] - id
# x[1] - ФИО
# x[2] - № проекта
# x[3] - класс
# x[4] - оценка
for x in students:
    s=','.join((str(hashstr(x[1])),x[1],x[2],x[3],x[4]))+'\n'
    fout.write(s)
    print(s)
fout.close()
