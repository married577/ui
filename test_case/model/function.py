import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 截图路径
def insert_img(driver, filename):
    func_path = os.path.dirname(__file__)
    base_dir = os.path.dirname(func_path)

    # 将路径转化为字符串
    base_dir = str(base_dir)

    # 对路径的字符串进行替换
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)

    base = base_dir.split('/Website')[0]

    filepath = base+'/Website/data/screenshot/'+filename
    driver.get_screenshot_as_file(filepath)


# 测试报告发送到qq邮箱
# def send_mail(latest_report):
#     f = open(latest_report, 'rb')
#     mail_content = f.read()
#     f.close()
#
#     smtpserver = 'smtp.qq.com'
#
#     user = '935550503@qq.com'
#     password = 'wpsgsfobxrmybcgj'
#
#     sender = '935550503@qq.com'
#     receives = ['2581655885@qq.com']
#
#     subject = 'Web MFFQ 自动化测试报告'
#
#     msg = MIMEText(mail_content, 'html', 'utf-8')
#     msg['Subject'] = Header(subject, 'utf-8')
#     msg['From'] = sender
#     msg['To'] = ','.join(receives)
#
#     smtp = smtplib.SMTP_SSL(smtpserver, 465)
#     smtp.helo(smtpserver)
#     smtp.ehlo(smtpserver)
#     smtp.login(user, password)
#
#     smtp.sendmail(sender, receives, msg.as_string())
#     smtp.quit()
#     print("发送成功")


# 测试报告路径和最新报告名的打印
def latest_report(report_dir):
    lists = os.listdir(report_dir)

    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))

    file = os.path.join(report_dir, lists[-1])
    print(lists[-1])
    return file


