import smtplib, ssl


def send_email(email_to, message):
    port = 465  
    email_from = "nurtugang17@gmail.com"
    password = "iaolbcsbmbbqrsmj"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email_from, password)
        server.sendmail('nurtugang17@gmail.com', email_to, message)

