from Crypto.Util.number import long_to_bytes
from base64 import b64decode
import codecs
from pwn import *
import json
r=remote("socket.cryptohack.org",13377)
for i in range(101):
	input=r.recvline()
	print(input)
	input=json.loads(input)
	typo=input['type']
	input=input['encoded']
	if (typo == 'hex' or typo == 'bigint'):
		p=int(input,16)
		payload=str(long_to_bytes(p))[2:-1]
	elif (typo == 'base64') :
		payload=str(b64decode(input))[2:-1]
	elif typo == 'utf-8' :
		payload=''.join(chr(k) for k in input)
	elif typo == 'rot13' :
		payload= codecs.decode(input, 'rot_13')
	req= {"decoded" : payload}
	r.sendline(json.dumps(req))
####crypto{3nc0d3_d3c0d3_3nc0d3}####