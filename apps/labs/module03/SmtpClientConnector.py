'''
Created on 2018年9月15日
    
@author: heychris
'''
from labs.common import ConfigUtil

import smtplib
from email.mime.text import MIMEText


class SmtpClientConnector:
    host = None
    port = 465
    fromAddr = None
    toAddr = None 
    authToken = None
    enableAuth = True
    enableCrypt = True
    
#     use variable smtpConfigReader to get config's data by using ConfigUtil API
    smtpConfigReader = None

    def __init__(self, configFile):
        self.smtpConfigReader = ConfigUtil.ConfigUtil(configFile, "smtp.cloud")
        self.host = self.smtpConfigReader.getProperty("host")
        self.port = self.smtpConfigReader.getProperty("port")
        self.fromAddr = self.smtpConfigReader.getProperty("fromAddr")
        self.toAddr = self.smtpConfigReader.getProperty("toAddr")
        self.authToken = self.smtpConfigReader.getProperty("authToken")
#     send data API using name and msg(String from SensorData instance)
    def sendEmailMessage(self, topic, message):

            msg = MIMEText(str(message))
            msg["From"] = self.fromAddr
            msg["to"] = self.toAddr
            msg["Subject"] = topic
        
            try:
                mailServer = smtplib.SMTP_SSL(self.host, self.port)
                mailServer.ehlo()
                mailServer.login(self.fromAddr, self.authToken)
                mailServer.send_message(msg, self.fromAddr, self.toAddr)
                
                mailServer.close()
                print("Successful!! This address is: " + self.toAddr)
            except Exception as e:
                print("Failed to send information\n" + e)
                
# test code
# msg2=MIMEText("Hi leo\n\nThis is a test email from python script!!\n\nBest,\n\nMySelf")
# msg2["From"]="jiaoyi199507@gmail.com"
# msg2["to"]="jiaoyi199507@gmail.com"
# msg2["Subject"]="Temperature"
#  
# mailServer=smtplib.SMTP_SSL("smtp.gmail.com",465)
# mailServer.ehlo()
# mailServer.login("jiaoyi199507@gmail.com","jxjy2006")
# mailServer.sendmail()
# mailServer.send_message(msg2,"jiaoyi199507@gmail.com")
# mailServer.close()