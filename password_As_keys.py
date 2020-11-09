from Crypto.Cipher import AES
import hashlib
flag="c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"
flag1=bytes.fromhex(flag)
with open("./words.txt") as f:
    words=[w.strip() for w in f.readlines()]
for key in words:
    key1=hashlib.md5(key.encode()).digest()
    cipher=AES.new(key1, AES.MODE_ECB)
    try:
        df=cipher.decrypt(flag1)
        if('63727970' in df.hex()):
            print(df)
            break
    except :
        continue