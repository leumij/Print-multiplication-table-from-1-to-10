for i in range(1,11):
    for j in range(1,11):
        n = i*j
        if n // 10 == 0:
            print(n,end=' '*2)         
        else: 
            print(n,end=' ')
        
    print()