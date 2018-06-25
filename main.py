
import smtplib
import time, imaplib, email
import winsound


FROM_EMAIL = "email_address@gmail.com"
FROM_PWD = "password"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        prev_num = 0
        while True:
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL,FROM_PWD)
            mail.select('inbox')
            typ, data = mail.search(None, 'ALL')
            mail_ids = data[0]
            id_list = mail_ids.split()
            if (prev_num == 0):
                prev_num = len(id_list)
            if (prev_num != len(id_list)):
                prev_num = len(id_list)
                #play sound
                winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
                typ, data = mail.fetch(int(id_list[-1]), '(RFC822)' )
			
                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        email_from = msg['from']
                        print 'From : ' + email_from + '\n'
                        print 'Subject : ' + email_subject + '\n'


    except Exception, e:
        print str(e)
