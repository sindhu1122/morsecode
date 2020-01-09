import encrypt
import decrypt
print("do you want to envrypt(0) or decrypt(1)")
d=int(input())
print("enter text")
s=input()
encrypt.enc(s)
print("enter decrypt msg")
s=input()
decrypt.dec(s)
