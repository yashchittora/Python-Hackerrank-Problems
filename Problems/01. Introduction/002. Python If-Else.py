# Problem Link : https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

n = int(input().strip())

if n%2!=0 and 1<= n <=100 :
	print("Weird")
	
if n%2==0 and 2<= n <=5 :
	print("Not Weird")
	
if n%2==0 and 6<= n <= 20:
	print("Weird")
	
if n%2==0 and n>20: 
	print("Not Weird")