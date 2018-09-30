#浅拷贝：只是单纯的将值拷贝（如果是对象就直接拷贝对象的地址）
#深拷贝：只会拷贝对象地址对应的值，产生一个新的地址，然后将新的地址进行赋值
import copy
number1 = [1,2]
numbers = [number1,3,4,'asd']
#浅拷贝
new_numbers = numbers.copy()
new_numbers2 = copy.deepcopy()