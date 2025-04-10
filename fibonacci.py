array = [0,1]

def fibonacci(n):

    #while n > len(array):
    #   array.append(array[-1] + array[-2])
     
    # elif array[-1] + array == 2:
    #     array.append(2)
    #     return 2
    # elif n == 3:
    #     array.append(1)
    #     return 1
    # else:
    #     soma = array[-1] + fibonacci(n)
    #     array.append(soma)
    #     return soma
    if array[-1] + array[-2] == 1:
        array.append(1)
         #return array[-1]
        if array[-1] and array[-2] == 1:
            array.append(2)
            #return array[-1]
            if array[-1] != array[-2]:
                atual = array[-1] + array[-2]
                array.append(atual)
                fibonacci(n)
    atual = array[-1] + array[-2]
    array.append(atual)
    return atual


fibonacci(1321)
print(array)