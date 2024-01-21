class ListLINQ:
    def __init__(self, _arr=[]):
        self.arr = _arr

    def Add(self, v):
        self.arr.append(v)
        return self

    def First(self):
        return self.arr[0]
    
    def Where(self, fun):
        return ListLINQ(list(filter(fun, self.arr)))
    
    def Select(self, fun):
        return ListLINQ(list(map(fun, self.arr)))

    def __str__(self) -> str:
        return '[' + ', '.join([str(n) for n in self.arr]) + ']'

    def toString(self):
        return list(self.arr)

class Tuple:
    def __init__(self, a: any, b: any):
        self.lVal = a
        self.rVal = b
    
    def __str__(self) -> str:
        return '({}, {})'.format(self.lVal, self.rVal)
    
    def __eq__(self, __value: object) -> bool:
        return (self.lVal == __value.lVal) and (self.rVal == __value.rVal)