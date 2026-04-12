import imaplib
import email

def check_inbox():
    mail = imaplib.IMAP4_SSL("imap.seuprovedor.com")
    mail.login("usuario", "senha")
    mail.select("inbox")

    status, data = mail.search(None, "UNSEEN")
    for num in data[0].split():
        status, msg_data = mail.fetch(num, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        print("Assunto:", msg["subject"])
