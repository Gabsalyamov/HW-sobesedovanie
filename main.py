BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALLANCED_LIST = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
UNBALLANCED_LIST = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]

class Stack(list):
    def isEmpty(self): #проверка на пустоту
        return len(self) == 0

    def push(self, _item): #новый элемент на вершину стека
        self.append(_item)

    def pop(self): #удаляет верхний элемент стека
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self): #возвращает верхний элемент стека, но не удаляет его
        if not self.isEmpty():
            return self[-1]

    def size(self): #возвращает количество элементов в стеке
        return len(self)

def check_ballance(seq_):
    stack = Stack()
    for item_ in seq_:
        if item_ in BAL_DICT:
            stack.push(item_)
        elif item_ == BAL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.isEmpty()

if __name__ == '__main__':
    for seq in BALLANCED_LIST + UNBALLANCED_LIST:
        print(f'{seq:<30}{check_ballance(seq)}')