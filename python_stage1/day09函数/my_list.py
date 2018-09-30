empty = []
def count(list1):
    """
    统计数字列表中所有元素的和
    :param list1:
    :return:
    """
    num = 0
    for item in list1:
        num += item
    return num