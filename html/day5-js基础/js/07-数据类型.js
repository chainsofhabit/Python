//new 类型名(值)---->可以将其他类型的数据转换成相应类型的值
//

//数字类型(Number):所有的数字对应的类型
//不能转换的结果是NAN
console.log(typeof(90))

var num1 = 100
var num2 = new Number(false)
console.log(num2,num1)


//2.布尔:true和false
//数字->布尔：NAN和0是false,其他的都是true
//字符串->布尔：空串是false，其他的都是true
//所有为0为空的转换成布尔都是false
//NAN,null,undefined都是false
var bool = new Boolean(null)
console.log(bool)


//3.字符串(String):unicode编码
//a.获取单个字符：通过字符串[下标]
//注意:a.js里下标只能是0到长度-1 不支持负值
//	  b.js里不支持切片
var str1 = 'asdfs'
console.log(str1[1])

//c.长度:字符串.length
console.log(str1.length)


//d.运算符:支持比较和+
//比较和Python一样

//+:如果是其他的数据类型和字符串相加，都是先将其他数据类型转换成字符串，然后做字符串拼接操作
console.log('asw'+'123')    //'asw123'
console.log(123+'asw')      //'123asw'

//e.其他的方法
//String对象方法:字符串.方法()

console.log('asd'.charCodeAt(2))

//数组(相当于python中的列表)
//a.有序,可变的，元素的类型可以是任意类型的数据
var array = [1,'abc',true,[1,2,3]]
//查
console.log(array[1])
//增
array.push('asdg')
console.log(array)
//pop():删除最后一个元素
array.pop()
console.log(array)
//shift():删除第一个元素
array.shift()
console.log(array)
//splice(1,1)从下标1开始删除，删除一个元素
var array1 = [1,'abc',true,[1,2,3]]
array1.splice(1,1)
console.log(array1)

//splice(被删除的下标/添加的开始下标，添加个数，被添加的元素列表)
array1.splice(4,2,'aa','bb')
console.log(array1)

//d.改
var array1 = [1,'abc',true,[1,2,3]]
array1[0] = 100
console.log(array1)

