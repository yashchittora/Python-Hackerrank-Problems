# **Python-Hackerrank-Problems**
Solutions to all the Python Preparation Problems of HackerRank

*Feel free to contribute and give suggestions*
<br></br>
# Support 😄
<a href="https://www.buymeacoffee.com/yashchittora" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="width: 150px !important;" ></a>
<br></br>
# Introduction
### [1. Say "Hello,World!" With Python](https://github.com/yashchittora/Python-Hackerrank-Problems/blob/main/Problems/01.%20Introduction/001.%20Say%20Hello%2CWorld!%20With%20Python.py)

```python
my_string = "Hello,World!"
print(my_string)
```

**Required Output**
```zsh
Hello,World!
```

<br></br>

### [2. Python If-Else](https://github.com/yashchittora/Python-Hackerrank-Problems/blob/main/Problems/01.%20Introduction/002.%20Python%20If-Else.py)

```python
n = int(input().strip())

if n%2!=0 and 1<= n <=100 :
	print("Weird")
	
elif n%2==0 and 2<= n <=5 :
	print("Not Weird")
	
elif n%2==0 and 6<= n <= 20:
	print("Weird")
	
elif n%2==0 and n>20: 
	print("Not Weird")
```

Example :
**If input is given `5` , Then : 
Required Output**

```
Weird
```
