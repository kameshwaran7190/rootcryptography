from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('text.key', 'wb') as file:
    file.write(key)

f = Fernet(key)

with open('hi.csv', 'rb') as og:
    cipher1 = og.read()

encrpted = f.encrypt(cipher1)

with open('encrypt.csv', 'wb') as sec:
    sec.write(encrpted)

with open('encrypt.csv', 'rb') as decfile:
    last = decfile.read()
dec =f.decrypt(last)

with open ('decrypt.csv', 'wb') as newdecfile:
    newdecfile.write(dec)


