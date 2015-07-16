import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SERVER = "smtp.qq.com"

COMMASPACE = ', '

# Create the container (outer) email message.
msg = MIMEMultipart()
msg['Subject'] = 'Our family reunion'
FROM = 'user@qq.com'
TO = ['user1@qq.com', 'uers2@qq.com']
msg['From'] = FROM
msg['To'] = COMMASPACE.join(TO)

text = 'hello,world!'
part1 = MIMEText(text, 'plain')
# part2 = MIMEText(html, 'html')
msg.attach(part1)
msg.preamble = 'Our family reunion'
server = smtplib.SMTP(SERVER)
server.login('user@qq.com', 'pwd')
server.sendmail(FROM, TO, msg.as_string())
server.quit()