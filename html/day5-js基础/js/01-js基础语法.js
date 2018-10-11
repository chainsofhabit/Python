//1.注释

//单行注释就是在前面加'//'

/* 这个是多行注释 
   这是注释第二行
 */


//2.标识符
//要求是由数字、字母、下划线和$符组成，数字不能开头
//var abc
//
//var 23sdf
//
//var $sfe

//3.js中大小写敏感



//4.基本数据类型

//Number(数字-包含所有的数字)、Boolean（布尔类型）、String（字符串）、Array(数组)、Object（对象）
//注意：js中没有元组和集合


//常用的特殊值：NaN（表示不存在的数字），null（空，一般用来清空变量中的内容），undefined（变量没有赋值的时候，默认是undefined）
//console.log(10*'abc')//相当于python中print函数，作用是在控制台打印（）中内容
// 
var name = null;
console.log(name)


//5.字面量
//Number字母量：所有的数字(支持科学计数法，不支持复数)

//19
//12.5
//-100
//+23.4

console.log(12e2)

//Boolean字面量：只有true和false

//true
//false

//String字面量：用单引号或者双引号引起来的字符集
//'abc'
//"wsd"
//console.log('sdw',"wed")
console.log('asd\nfd2','acv\sw234\\')
//Array字面量：js中数组就相当于python的列表

console.log([12,'acv',true])

//Object对象字面量：相当于python中的字典+对象
//注意:key相当于属性，value相当于属性的值
var dict = {a:100,name:200}

console.log(dict)

//typeof:查看数据类型

console.log(typeof(100),typeof('abc'))

//6.js中的语句：a.一条语句结束后可以写分号，也可以不写。如果一行写多条语句就必须写分号
//b.js中没有缩进语法的要求，需要使用代码的时候使用{}
