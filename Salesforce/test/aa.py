import random
import time
import xlwt as ExcelWrite

from Salesforce.config import env_key
from Salesforce.pages.LoginPage import LoginPage
from Salesforce.pages.ToolPage import ToolPage


def get_tabs():
    login = LoginPage('PingChina')
    login.openWebSite()
    tool_page = ToolPage()
    all_rows = tool_page.all_rows
    tool_page.wait_loading_disappear()

    first_list = [["监测点", "解析IP", "HTTP状态", "总耗时", "解析时间", "连接时间", "下载时间", "文件大小", "下载速度", "操作", "赞助商"]]
    for row in all_rows:
        first_list.append(row.text.split('\n'))

    print("first_list : ")
    print(first_list)
    writeXLS(first_list , "./test_write_{0}{1}.xls".format(env_key,str(random.randint(1,100))))

def writeXLS(value, file_name):
    # value = [["name", "jim", "hmm", "lilei"], ["sex", "man", "woman", "man"]]

    xls = ExcelWrite.Workbook()
    sheet = xls.add_sheet("Sheet1")

    for row in range(0, len(value)):
        for col in range(0, len(value[row])):
            sheet.write(row, col, value[row][col])

    xls.save(file_name)


if __name__ == "__main__":
    get_tabs()
    # writeXLS("./test_write3.xls");
