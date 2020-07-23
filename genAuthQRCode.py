import pyqrcode
import sqlite3
conn = sqlite3.connect('/home/user/databases')
c = conn.cursor()

for idx, (email, secret, issuer) in enumerate(c.execute("SELECT email,secret,issuer FROM accounts").fetchall()):

if issuer==None:

    if len(email.split(" "))>0:
        issuer=email.split(" ")[0]
    else:
        issuer=email

    if len(issuer.split(":"))>0:
        issuer=issuer.split(":")[0]

    #print ("If the following issuer looks wrong, enter a new value. If it's OK, just press ENTER.")
    #newIssuer=input(issuer)
    #if len(newIssuer)>0:
    #    issuer=newIssuer

url = 'otpauth://totp/{}?secret={}&issuer={}'.format(email, secret, issuer)
im = pyqrcode.create(url)
#print (url)
#print(im.terminal(quiet_zone=1))

big_code = pyqrcode.create(url, error='L', version=27, mode='binary')
big_code.png(issuer+'.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()