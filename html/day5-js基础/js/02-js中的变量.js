//1.js中变量的声明
/*语法:var 变量名 或者  var 变量名=初值
 * 说明：
 * a.var:是js中声明变量的关键字
 * b.变量名：标识符，不能是js中的关键字；驼峰式命名（第一个单词的首字母小写 后面每个单词首字母大写）
 * 见名知意
 * c.初值:声明的时候可有可无
 */

var age

var age = 20

console.log(age)
//变量名不能是关键字

var studentCount = 100

//a.同时声明多个变量
var age,name,studyId
var age1=20,name1,studyId1


//b.
var name='张飒'    //声明变量（就是在内存中开辟空间存储数据）
name = 100       //修改变量的值
name = [1,'aaa']
console.log(name)


var userName
userName = '张飒'
