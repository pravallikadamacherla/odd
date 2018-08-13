d,p=input().split()
d,p=int(d),int(p)
count=0
for i in range(d+1,p):
	if(i%2==0):
		if i<p-2:
			k=" "
		else:k=""
		print(i,end=k)
