//函数的声明
/*
 function 函数名(参数列表){
 	函数体
 }
 
 说明：
 a.function:是js中声明函数的关键字
 b.函数名：标识符，不能是关键字；见名知意；驼峰式命名
 c.参数列表：参数名1，参数名2....;形参;将数据从函数的外面传到函数中
 d.函数体:实现函数的功能
 
 
 注意事项：函数体只有在函数调用的时候才执行
 */
function sum(num1,num2){
	console.log(num1+num2)
}

function sum2(num3=10,num4){
	console.log(num3+num4)
}
sum2(10,89)

//2.函数的调用：和Python一样

/*
 函数调用的时候要保证每个参数都有值
 支持位置参数，关键字参数，参数设置默认值(js6)
 js不支持不定长参数
 */
sum(20,30)
sum(num1=10,num2=34)

//3.函数的返回值
//js中函数如果没有遇到return，函数的返回值是undefined
//注意:js中不能同时返回多个值(有元组语法的语言才支持多个返回值)
function func1(){
	console.log('func1')
//	return 100,'asd'
	return 100
}
console.log(func1())

//4.js中函数也可以作为变量
//var a = func2
//a()

//5.另外一种声明方式
/*
 var 变量 = function(参数列表){
 	函数体
 }
 */
var func2 = function(num){
	console.log('这是一个函数类型的数据',num)
}
func2('axx')

var funcs = [
	function(){
		console.log('aaa')
	},100
]
funcs[0]()
