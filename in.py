v,p=input().split()
v,p=int(v),int(p)
count=0
for i in range(v+1,p):
	if(i%2!=0):
		if i<p-2:
			k=" "
		else:k=""
		print(i,end=k)
