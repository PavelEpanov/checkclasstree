def classTree(cls, indent):
    print("." * indent + cls.__name__) # Вывести здесь имя класса
    for supercls in cls.__bases__: # Вызвать рекурсивно для всех суперклассов
        classTree(supercls, indent+3) # Может посетить суперкласс более одного раза

def instanceTree(inst):
    print("Tree of %s" %inst) # Показать экземпляр
    classTree(inst.__class__, 3) # Подняться к его классу


def selftest():
    class A:
        pass
    class В(A):
        pass
    class C(A):
        pass
    class D (В, C) :
        pass
    class E:
        pass
    class F(D,E) : pass
    instanceTree(F())

if __name__ == "__main__":
    selftest()



