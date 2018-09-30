import json

def write_json_file(file_name,content):
    """
    将内容写入json文件中
    :param file_name: 文件名
    :param content: 要写的内容
    :return: 是否写入成功
    """
    try:
        with open("./files/"+file_name,"w",encoding="utf-8") as f:
            json.dump(content,f,ensure_ascii=False,indent=2)
            return True
    except:
        return False

def read_json_file(file_name):
    """
    读取json文件的内容
    :param file_name: 文件名
    :return: 文件内容
    """
    try:
        with open("./files/"+file_name,encoding="utf-8") as f:
            return json.load(f)
    except:
        return None
def read_text_file(file_name):
    """
    获取文本文件内容
    :param file_name: 文件名
    :return: 文件内容
    """
    try:
        with open("./files/"+file_name,encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("文件不存在")
        return None
# print(read_text_file('login.txt'))


