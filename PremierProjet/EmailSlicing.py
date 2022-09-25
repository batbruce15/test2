
email=""
while("@" not in email):
    email=input("enter your email : ")
    if("@" not in email):
        print("the email formate is not correcte")
username=email[:email.index("@")].capitalize().strip()
website=email[email.index("@")+1:].strip()
print(f"Your username is {username} and your website is {website}")