import  itertools
nu=itertools.count(1)  #注意count会创建一个无线迭代器
nu=itertools.cycle('ABC') #cycle()会把ABC无线循环下去
nu=itertools.repeat('AB',11) #repeat()会把第一个参数重复下去,传入第二个参数可以控制重复次数
for n in nu:
        print(n)
print('#############################')
for c in itertools.chain('ABC','DEF'):      #chain()可以将多个对象串联起来形成一个更大的迭代器
        print(c)
print('##############################')
for key,group in itertools.groupby('AAAAAAAAaaaaaaaaaCCCCCCCCBBBBBBBBBEEE'):
    print(key,list(group))      #groupby()把迭代器相邻的重复元素挑出来放在一起