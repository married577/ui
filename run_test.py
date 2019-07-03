import unittest
from test_case.model.function import *
# from BSTestRunner import BSTestRunner
from HTMLTestRunner import HTMLTestRunner
import time

report_dir = './test_report'
test_dir = './test_case'

print("用例正在执行中...")
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test_login.py")

now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir+'/'+now+'result.html'

print("正在发送报告...")
with open(report_name, 'wb') as f:
    runner = HTMLTestRunner(stream=f, title="分期测试报告", description="测试脚本")
    runner.run(discover)
    f.close()

print("最近的一条测试报告是：")
latest_report = latest_report(report_dir)

# print("测试报告正在发送中，请稍后...")
# send_mail(latest_report)

print("测试结束")