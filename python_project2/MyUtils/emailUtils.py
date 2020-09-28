import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   #如果要添加附件，必须使用MIMEMultipart
from email.header import Header

def sendEmail(smtpserver,port,sender,receivers,sender_password,attPath,attFilename):
    """

    :param smtpserver: smtp.qq.com或者smtp.163.com
    :param port: 465
    :param sender: 发送者邮箱
    :param receivers: 接受者邮箱
    :param sender_password: smtp授权码
    :param reportPath:   html报告路径
    """
    message=MIMEMultipart()

    message.attach(MIMEText('发送邮件测试','plain','utf-8'))
    message['From']=Header("Jimmy",'utf-8')
    message['To']=Header('测试','utf-8')

    subject='python smtp 邮件测试'
    message['Subject']=Header(subject,'utf-8')

    #添加多个附件：
    for i in range(len(attPath)):
        # 一般如果数据是二进制的数据格式，在指定第二个参数的时候，都使用base64，一种数据传输格式。
        # att1 = MIMEText(open(attPath[i], 'rb').read(), 'base64', 'utf-8')

        att1=MIMEText(open(attPath[i],'rb').read(),'base64','utf-8')
        att1['Content-Type']='application/octet-stream'
        att1['Content-Disposition']='attachment; filename={}'.format(attFilename[i])
        message.attach(att1)


    try:
        smtpObj=smtplib.SMTP_SSL(smtpserver,port)
        smtpObj.login(sender,sender_password)
        smtpObj.sendmail(sender,receivers,message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error:无法发送邮件")


if __name__=='__main__':
    sender='974643517@qq.com'
    receivers=['974643517@qq.com']
    sendEmail("smtp.qq.com",465,sender,receivers,"gofyiuzkjzlzbdic")


