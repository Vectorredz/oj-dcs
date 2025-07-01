def funct(n):
  
    if (n==1):
       return
    for i in range(1, n+1):
        for j in range(i, n + 1):
            print("*", end = "")
            # break
        print()
    
# The code is contributed by Nidhi goel. 
funct(5)