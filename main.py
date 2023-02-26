from types import LambdaType
from multipledispatch import dispatch

class TestClass(object):

    @dispatch(object)
    def test_method(self, arg, verbose=False):
        if verbose:
             print("Let me just say,", end=" ")
        
        print(arg)
    
    @dispatch(int, float)
    def test_method(self, arg, arg2):
        print("Strength in numbers, eh?", end=" ")
        print(arg + arg2)

    @dispatch((list, tuple), LambdaType, type)
    def test_method(self, arg, arg2, arg3):
        print("Enumerate this:")

        for i, elem in enumerate(arg):
            print(i, arg3(arg2(elem)))


if __name__ == '__main__':

    test = TestClass()
    test.test_method('Choo choo train', verbose=True)
    test.test_method(55555, 9.5)
    test.test_method([33, 22, 11], lambda x: x*2, float)