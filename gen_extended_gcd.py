def gcdExt(a,b):
	if a== 0 :#base_Case
		return b , 0 , 1
	gcd, x1 ,y1=gcdExt(b%a,a)
	x= y1 - (b//a) * x1
	y= x1
	return gcd , x ,y
def main():
	a,b=26513,32321#put your values here
	g, x, y=gcdExt(a,b)
	print("gcd=",g," x=",x," y=",y)
#Driver Code
if __name__ == "__main__":
	main()



	
