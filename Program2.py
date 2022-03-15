# Python program to display the Fibonacci sequence
def recur_fibo(n):

    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2)) 


nLoops = 10

# check if the number of terms is valid
if nLoops <= 0:
    print("Plese enter a positive integer")

else:
    print("Fibonacci sequence:") 

for i in range(nLoops):
    print(recur_fibo(i))