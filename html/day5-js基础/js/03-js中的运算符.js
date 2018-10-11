//js中的运算符包含：数学运算符，比较，逻辑，赋值，三目运算符、（位运算）

//1.数学运算符：+、-、*、/、%、**（js7中才有的）、++、--

//+、-、*、/、%、**和Python中的功能一模一样
//注意：js中整除对应的运算符，但是多了++和--

//a.++(自加)：自加1
//语法：变量++,++变量----->让变量的值加1


//
var number = 10
number++   //相当于number += 1
console.log(number)

++number
console.log(number)

//b.--(自减1操作)
//语法：变量--，--变量------>让变量值减1  相当于变量-=1

var num=251
--num
console.log(num)
num--
console.log(num)

//c.赋值的时候，++写在变量的后面，是先赋值，然后再让变量的值加1.++写在变量的前面就是先加1再赋值
var a1=10,a2=10,b,c
b = a1++
c = ++a2
console.log(b,c,a1,a2)

//2.比较运算符：>,<,==,!=,>=,<=,===,!==,>==,<==
//结果都是布尔值
//==，===

//==(相等)：只判断值是否相等    ===（完全相等）：判断值和类型是否相等
console.log(10==10)   //true
console.log('2'=='2')  //true
console.log('10'==10)   //true

console.log(2===2)     //true
console.log('3'===3)   //false
console.log('3'==='3')   //true

console.log(3!=3)
console.log('3'!=3)
console.log(3!==3)
console.log('3'!==3)


//逻辑运算符：&&（与），||（或），！（非）
//js逻辑运算符除了形式其他和Python一样

console.log(!true)

//4.赋值运算符：=，+=，-=，*=，/=,%=,等  和Python一样

//三目运算符：?:
//语法：表达式1?值1：值2---->判断表达式1的值是否为真，为真，整个运算的结果就是值1，否则是值2
var value = 10>20?10:2
console.log(value)

var a = 100 ,b = 1000
var c=a>b?a:b
console.log(c)


//练习：求三个数中的最大数（用三目运算符）
var a = 10,b = 20,c = 15
var d,e
var d = a>b?a:b
var e = d>c?d:c
console.log(e)

//6.运算顺序：和Python基本一致（数学>比较>逻辑>赋值），也可以通过加括号来改变运算顺序

var re = 190>20?50:100>20
console.log(re)
