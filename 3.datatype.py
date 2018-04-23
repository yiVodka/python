counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
 
print (counter)
print (miles)
print (name)

'''
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Sets（集合）
Dictionary（字典）
'''

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

res = isinstance(d, complex)
print(res)

class A:
    pass

class B(A):
    pass

_a = isinstance(A(), A)  # returns True
_b = type(A()) == A      # returns True
_c = isinstance(B(), A)    # returns True
_d = type(B()) == A        # returns False
print(_a, _b, _c, _d)
'''
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型
'''

var1 = 'a'
print(var1)

print(5 + 4)  # 加法
print(4.3 - 2) # 减法
print(3 * 7)  # 乘法
print(2 / 4)  # 除法，得到一个浮点数
print(5 // 4) # 除法，得到一个整数
print(17 % 3) # 取余 
print(2 ** 5) # 乘方

lista = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
listb = [123, 'runoob']
print (lista)            # 输出完整列表
print (lista[0])         # 输出列表第一个元素
print (lista[1:3])       # 从第二个开始输出到第三个元素
print (lista[2:])        # 输出从第三个元素开始的所有元素
print (lista * 2)    # 输出两次列表
print (lista + listb) # 连接列表

a = [1, 2, 3, 4, 5, 6]
print (a[1:3])
a[2:5] = [1]
print(a)

tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2 )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

tuplea = ('x',25)
print(tuplea)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉

# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

a = set('abracadabra')
b = set('alacazam')

print(a - b)     # a和b的差集
print(b - a)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
print(dict)