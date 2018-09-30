# import json
# data1 = []
# with open("./files/data.json","r",encoding="utf-8") as f:
#     content = json.load(f)
#
# for item in content["data"][:]:
#     data2 = {}
#     data2["name"] = item["name"]
#     data2["text"] = item["text"]
#     data2["love"] = item["love"]
#     data2["comment"] = item["comment"]
#     data1.append(data2)
# with open("./files/new_data.json","w",encoding="utf-8") as f1:
#     json.dump(data1,f1)
#     print(data1)
# count = 0
# for item in data1:
#     if int(item["comment"])>1000:
#         count += 1
# print(count)
# 3. 将data.json文件中所有点赞数(love)对应的值超出1000的用k来表示，
# 例如1000修改为1k, 1345修改为1.3k

# with open("./files/data.json","r",encoding="utf-8") as f2:
#     content = json.load(f2)
# count = 0
# for item in content["data"][:]:
#     if int(item["love"]) >= 1000:
#         item["love"] = str(int(item["love"])//100/10) + "k"
#         # print(item)
# with open("./files/data1.json","w",encoding="utf-8") as f3:
#     json.dump(content,f3,ensure_ascii=False,indent=2)
#
# print(content)
import random
number = random.randint(0,50)
while True:
    try:
        number1 = int(input("输入一个整数："))
        if number1 == number:
            print("猜对了！！")
        elif number1 < number:
            print("小了，往大的猜")
        else:
            print("大了，往小的猜")
    except ValueError:
        print("输入有误，请重新输入")


