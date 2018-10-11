//js中的循环分为：for循环和while循环
//1.for-in循环：（和Python的for循环一样）
/*
 for var 变量 in 序列{
 	循环体
 }
 
 执行过程:依次从序列中取元素对应的索引，取完为止，每取一个执行一次循环体
 */
var str='abcd'
for (var i in str){
	console.log(str[i])
}


for (var index in [1,'sd',true]){
	console.log(index)
}


//遍历对象，取的是属性名(key)
for (var x in {a:'scd',name:'咻咻'}){
	console.log(x)
}

//2.for循环：(和C语言的for循环一样)
/*
 for(语句1;表达式2;语句3){
 	循环体
 }
 
 执行过程:先执行表达式1，然后再判断表达式2的结果是否为true，如果为true就执行循环体，执行完循环体在执行表达式3，
 然后再判断表达式2的结果是否为true，如果为true又执行循环体，执行完循环体再执行表达式3，
 依次循环，直到表达式2的值为false为止
 
 */

var i = 1,count = 0
for(i;i<=100;i++){
	count += i
	
}
console.log(count)



//3.while循环:(和Python一样)
/*
 while(条件语句){
 	循环体
 }
 */
var sum=0
var i=1
while(i<=100){
	sum += i
	i++
}
console.log(sum)

//4.do-while:
/*
 do{
 	循环体
 	
 }while(条件语句)
 
 执行过程：先执行一次循环体，然后再判断条件语句是否为true,为true又执行循环体，依次类推，直到条件语句为false,循环就结束
 
 */
var sum1 = 0
i = 1
 do{
 	sum1 += i
 	i++
 }while(i<=100)
console.log(sum1)