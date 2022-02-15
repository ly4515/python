class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__score = 50

    # 给私有属性赋值
    def setName(self, name):
        if len(name) == 6:
            self.__name = name
        else:
            print('名字必须是6位')

    # 获取私有属性
    def getName(self, name):
        return self.__name

    # 先有getxxx
    @property
    def age(self):
        return self.__age

    # 再有set，因为set依赖get

    @age.setter
    def age(self, age):
        if age < 0:
            print('年龄不合理')
        else:
            self.__age = age

    def __str__(self):
        return '姓名:{},年龄:{}'.format(self.__name, self.__age)


s = Student('lili', -8)
print(s)
s.name = 'kokoko'
print(s.name)
# 私有化赋值
s.setName('kkk')
s.age = -3
