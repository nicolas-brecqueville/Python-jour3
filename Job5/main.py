for i in range(2, 1001): 
    for n in range(2, int(i**n)+1):
        if i % n == 0:
            break
    else:
        print(i)