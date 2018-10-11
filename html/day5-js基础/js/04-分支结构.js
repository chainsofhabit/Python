//js中的分支结构：if语句，switch语句
//if语句
/*结构：
 a.if（条件语句）
  {
  	代码段
  }
  执行过程：先判断条件语句是否为true，为true就执行代码段
  
  
 b. if-else结构：
  if（条件语句）{
  	代码段1
  }
  else{
  	代码段2
  }
  
  
  c.if;else if;else:(这的else if相当于Python中的elif)
  if（条件语句）{
  	代码段1
  }
  else if{
  	代码段2
  }
  else{
  	代码段3
  }
  
  
  
 */

//var num = 11
//if(num%2 == 0){
//	console.log('偶数')
//}

//2.switch
/*
 a.结构：
 switch(表达式){
 	case 值1：{
 		代码段1
 		break
 	}
 	case 值2:{
 		代码段2
 		break
 	}
 	....
 	default:{
 		break
 	}
 }
 b.执行过程：先计算表达式的值，然后再用这个值去和后边case关键字后面的值一一对比，看是否相等
 		找到第一个和表达式的值相等的case，然后将这个case作为入口，一次执行后边所有的代码
 		直到遇到break或者switch结束，如果没有找到和表达式的值相等的case就执行finally后面的代码
 		
 c.注意：default可有可无。case可以有若干个		
 
 */

var num1=10
switch(num1){
	case 100:{
		console.log('A')
		break
	}
	case 10:{
		console.log('B')
		break
	}
	case 'abc':{
		console.log('C')
		break
	}
	default:{
		console.log('D')
		break
	}
	
}

//练习：根据数字对应的值不一样，打印不同的结果 0--->星期天 1--->星期一

var week = 10
switch(week){
	case 0:{
		console.log('Sunday')
		break
	}
	case 1:{
		console.log('Monday')
		break
	}
	case 2:{
		console.log('Tuesday')
		break
	}
	case 3:{
		console.log('Wednesday')
		break
	}
	case 4:{
		console.log('Thursday')
		break
	}
	case 5:{
		console.log('Friday')
		break
	}
	case 6:{
		console.log('Saturday')
		break
	}
	default:{
		console.log('告辞')
	}
}

var score = 11
switch(score){
	case 6:{
		console.log('及格')
		break
	}
	case 7:
	case 8:{
		console.log('良好')
		break
	}
	case 9:
	case 10:{
		console.log('优秀')
	}
	case 1:
	case 2:
	case 3:
	case 4:
	case 5:{
		console.log('不及格')
		break
	}
	default:{
		console.log('回家吧')
		break
	}
	
	
}
