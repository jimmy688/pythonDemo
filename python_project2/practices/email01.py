import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   #如果要添加附件，必须使用MIMEMultipart
from email.header import Header

#smtpserver,port,sender,receivers,sender_password
def sendEmail(smtpserver,port,sender,receivers,sender_password):
    message=MIMEMultipart()

    message.attach(MIMEText('发送邮件测试','plain','utf-8'))
    message['From']=Header("Jimmy",'utf-8')
    message['To']=Header('测试','utf-8')

    subject='python smtp 邮件测试'
    message['Subject']=Header(subject,'utf-8')

    #添加附件1：
    att1=MIMEText(open('../sources/runoob1.txt','rb').read(),'base64','utf-8')
    att1['Content-Type']='application/octet-stream'
    att1['Content-Disposition']='attachment; filename=runoob1.txt'
    message.attach(att1)

    #添加附件2：
    att1=MIMEText(open('../sources/runoob2.txt','rb').read(),'base64','utf-8')
    att1['Content-Type']='application/octet-stream'
    att1['Content-Disposition']='attachment;filename=runoob2.txt'
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
