#!/usr/bin/python3
def input_arr()->list:
    '''
    Возвращает массив, запрашивая у пользователя
    '''
    arr = input('Введите элементы массива через пробел: ').split()
    try:
        arr = [float(elem) if '.' in elem else int(elem) for elem in arr]
    except ValueError:
        pass
    return arr

def main(arr: list)->list:
    '''
    Возвращает отсортрованный массив
    '''
    for number1 in range(1, len(arr), 1):
        for number2 in range(number1-1, -1, -1):
            if arr[number2+1]<arr[number2]:
                arr[number2+1], arr[number2] = arr[number2], arr[number2+1]
    return arr

def test()->None:
    '''
    Тесты для main функции
    '''
    test_dict ={
        'test1':[],
        'test2':[1, 2, 3],
        'test3':[3,2,1],
        'test4':[2,-3,5],
        'test5':[3.5,5,3.2],
        'test6':['moooore','a','ab'],
        'test7':[1,2,2,1,4,5,4]
        }
    answer_dict = {
        'test1':[],
        'test2':[1,2,3],
        'test3':[1,2,3],
        'test4':[-3,2,5],
        'test5':[3.2,3.5,5],
        'test6':['a','ab','moooore'],
        'test7':[1,1,2,2,4,4,5]
        }
    for name in test_dict:
        if main(test_dict[name])!=answer_dict[name]:
            print(f'{name} failed!')
        

if __name__ == '__main__':
    #array = input_arr()
    #print(main(array))
    test()