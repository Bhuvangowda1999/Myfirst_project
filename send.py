from smtplib import SMTP


HOST= 'smtp.gmail.com'

PORT= 587

SENDER = 'unknowperson880@gmail.com'

PASSWORD='abcdefghI'

server = SMTP(host=HOST,port=PORT)

server.connect(host=HOST,port=PORT)

server.ehlo()

server.starttls()

server.ehlo()

server.login(user=SENDER ,password= PASSWORD)

RECIPIENT = "shailaja2594@gmail.com"

message = 'Hai you have won a gift voucher of rs 2500000'

server.sendmail( "unknowperson880@gmail.com ","shailaja2594@gmail.com",'hai you have won a gift voucher')

print('mail''sent')
