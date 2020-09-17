from PIL import Image
lemur = Image.open("lemur.png")
flag = Image.open("flag.png")

pixels_lemur=lemur.load()
pixels_flag= flag.load()

for i in range(lemur.size[0]):
	for j in range(lemur.size[1]):
		l=pixels_lemur[i,j]
		f=pixels_flag[i,j]
		r=l[0]^f[0]
		g=l[1]^f[1]
		b=l[2]^f[2]
		pixels_flag[i,j]=(r , g , b)
flag.save('final_flag.png')
######crypto{X0Rly_n0t!}######
