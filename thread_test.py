import threading
from time import ctime,sleep

num = 9

def music(func):
    for i in range(2):
        print("I was listening to %s. %s" %(func,ctime()))
        sleep(1)

def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

class Person(object):


    def __init__(self,name,tag):
        self.__a__ = name
        self.__b__ = tag

    # call调用
    def print_test(self):
        print('a:%s b:%s',self.__a__,self.__b__)

    def __call__(self):
        print('%s:  a = %s, b = %s',self.__a__,self.__b__)


    # 作用域
    def f2(self):
        print(num)
    def f1(self):
        num = 20
        print(num)

    # 默认方法
    def mydefault(self,*args):
        print('default:' + str(args[0]))

    def __getattr__(self, item):
        return self.mydefault


# and_or
@classmethod
def choose(bool,a,b):
    return (bool and [a] or [b])[0]

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

li = [3,3,1,2,3]
def main():
     mid = len(li)/2
     for l in li:
         count = 0
         i = 0
         mark = 0
         while True:
             if l == li[i]:
                 count += 1
                 temp = i
             i += 1
             if count > mid:
                 mark = temp
                 return (mark,li[mark])
             if i > len(li) - 1:
                 break


class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

if __name__ == '__main__':
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()
    # print("all over %s"%ctime())
    # g = lambda x:x*2
    # g(2)
    #
    # print(main())

    p = Person('hello','word')
    p()
    p.f2(),p.f1(),p.f2(),p.f3(10)
