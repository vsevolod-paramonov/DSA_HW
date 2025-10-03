
def validate(pushed, popped):

    if len(pushed) == 0 and len(popped) == 0:
        return True
    
    stack = []
    j = 0
    
    for i in range(len(pushed)):
        ### Заполняем стек элементами из pushed
        stack.append(pushed[i])
        
        ### До тех пор, пока стек не пуст и верхний элемент стека равен
        ### следующему элементу из popped, достаем элементы из верха стека
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    
    return j == len(popped) and len(popped) > 0