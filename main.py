'''
1. Выполнить задание уровня light
2. Придумайте 2 теста к грязной функции. Примером грязной функции является функция F из дз 4;
3. Пришлите ответ по инструкции 4.
'''

import random

def f( lstName, n ):
    if n <= len( lstName ):
        lst = random.sample( lstName, n  )
    else:
        lst = []
        if len(lstName) <= 2:
            step=1
        elif len(lstName) <= 6:
            step = 3
        else:
            step = 5

        for i in range( 0, n//step ):
            lst += random.sample(lstName, step )
            #print( len(lst) )
        if n%step > 0:
            lst += random.sample( lstName, n%len(lstName)  )
            #print(len(lst))
    return lst

def fMax( lst ):
    # уникальные слова
    lstUnique = list( set(lst) )
    #print('всего слов=', len(lst), 'Уникальных слов=', len(lstUnique))

    # словарь частотности слов
    dic = {}
    for word in lstUnique:
        n = lst.count( word )
        dic[word] = n
    #print('словарь частотности слов\n', dic)

    # Сортировка по частоте
    ds = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    #print( 'Сортировка:\n', ds )

    # самые часто встречающиеся слова
    rez = list( filter( lambda x: x[1] == ds[0][1], ds ) )

    print('Самые частые имена (повторяемость={}):'.format(rez[0][1]))
    for v in rez:
        print( v [0],end=' ' )
    print()

def rareType( inLst ):
    lst = list( map( lambda x: x[0], inLst ) )
    #print(inLst)
    #print(lst)

    # уникальные начальные буквы
    lstUnique = list( set(lst) )
    #print('всего букв=', len(lst), 'Уникальных букв=', len(lstUnique))

    # словарь частотности слов
    dic = {}
    for word in lstUnique:
        n = lst.count( word )
        dic[word] = n
    #print('словарь частотности\n', dic)

    # Сортировка по частоте
    ds = sorted(dic.items(), key=lambda x: x[1], reverse=False)
    #print( 'Сортировка:\n', ds )

    # самые редко встречающиеся буквы
    rez = list( filter( lambda x: x[1] == ds[0][1], ds ) )

    print('Самые редкие буквы (повторяемость={}):'.format(rez[0][1]))
    for v in rez:
        print( v [0],end=' ' )
    print()
# -----------------------------------------------------------------------------------------

lst = ['Ия','Аполлинарий','Ян','Алексей','Валентина','Мирослава','Екатерина','Микеланджело','Александрина','Лидия','Полина','Габриэль','Гарри','Шарик','Валерий','Александр','Мурзик','Терминатор','Паша','Маша']

# список из случайных заданных имен
lst100 = f( lst, 100 )

#print(    lst   )
#print(    lst100   )

fMax( lst100 )

rareType( lst100 )