import xlwt


def study_xlwt():
    """
    使用xlwt模块来操作excel
    :return:
    """

    file_path = "/Users/tongziyu/Desktop/未命名.et"
    workBook = xlwt.Workbook(encoding="UTF-8")

    # 使用add_sheet()方法添加一个工作簿
    ceshi_sheet: xlwt.Worksheet = workBook.add_sheet("测试sheet")


    head = ['姓名', '年龄', '性别']
    data = [['zhangsan', 18, '男'], ['lisi', 20, '女']]

    # 循环写入表头
    for item in head:
        ceshi_sheet.write(0, head.index(item), item)

    # 循环写入内容
    for i in range(len(data)):
        for j in range(len(data[i])):
            ceshi_sheet.write(i + 1, j, data[i][j])

    workBook.save(file_path)


if __name__ == '__main__':
    """
    使用python操作excel
    
    使用第三方模块 xlwt
    
    """
    study_xlwt()



    pass


