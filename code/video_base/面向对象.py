'''
工资管理系统，工人（worker）、销售员（salesman）、经理（manager）、销售经理（salemanger）
所有员工都有工号，姓名，工资等属性，有设置姓名，获取姓名，获取工号，计算工资等方法
工人: 有工作小时数和时薪属性，工资=工作小时数*时薪
销售员: 有销售额和提成比例，工资=销售额*提成比例
经理: 固定月薪属性，工资=固定月薪
销售经理: 工资=销售额*提成比例+固定月薪
设计合理的类，完成
1.添加所有类型的员工
2.计算月薪
3.显示所有人工资情况
'''


class Person:
    def __init__(self, no, name, salary):
        self.no = no
        self.name = name
        self.salary = salary

    def __str__(self):
        msg = '工号:{}姓名:{}本月工资:{}'.format(self.no, self.name, self.salary)
        return msg

    def getSalary(self):
        return self.salary

# 工人: 有工作小时数和时薪属性，工资=工作小时数*时薪


class Worker(Person):
    def __init__(self, no, name, salary, hours, per_hour):
        super().__init__(no, name, salary)
        self.hours = hours
        self.per_hour = per_hour

    def getSalary(self):
        self.salary = self.hours*self.per_hour
        return self.salary

# 销售员: 有销售额和提成比例，工资=销售额*提成比例


class Salesman(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percent = percent

    def getSalary(self):
        self.salary = self.salemoney*self.percent
        return self.salary

# 经理: 固定月薪属性，工资=固定月薪


class Manager(Person):
    def __init__(self, no, name, salary, month_money):
        super().__init__(no, name, salary)
        self.month_money = month_money

    def getSalary(self):
        self.salary = self.month_money
        return self.salary


# 销售经理: 工资=销售额*提成比例+固定月薪
class Salemanger(Person):
    def __init__(self, no, name, salary, salemoney, percent):
        super().__init__(no, name, salary)
        self.salemoney = salemoney
        self.percent = percent

    def getSalary(self):
        self.salary += self.salemoney*self.percent
        return self.salary


# 创建对象
w = Worker('001', 'king', 0, 160, 50)
s = w.getSalary()
print('月薪:', s)
print(w)
sa = Salemanger('002', 'job', 2000, 50000, 0.03)
ss = sa.getSalary()
print('Salemanger月薪:', ss)
print(sa)
