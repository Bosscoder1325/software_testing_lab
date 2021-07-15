lockprice = 45.0
stockprice = 30.0
barrelprice = 25.0

totallocks = totalstocks = totalbarrels = 0

print("Enter the number of locks and to exit press -1")
locks = int(input())

while locks != -1:
    c1 = locks<=0 or locks>70
    print("Enter the number of stocks and barrels")
    stocks = int(input())
    barrels = int(input())
    
    c2 = stocks<=0 or stocks>80
    c3 = barrels<=0 or barrels>90
    
    if c1:
        print("Value of locks are not in range of 1...70")
    else:
        temp = totallocks + locks
        if temp>70:
            print(f"new totallocks = {temp} not in the range of 1...70")
        else:
            totallocks = temp
    print(f"Total locks = {totallocks}")

    if c2:
        print("Value of stocks not in the range of 1...80")
    else:
        temp = totalstocks + stocks
        if temp>80:
            print(f"New total stocks {temp} not in the range of 1...80")
        else:
            totalstocks = temp
    print(f"Total stocks = {totalstocks}")

    if c3:
        print("Value of barrels not in the range of 1...90")
    else:
        temp = totalbarrels + barrels
        if temp>90:
            print(f"New total barrels = {temp} not in the range of 1...90")
        else:
            totalbarrels = temp
    print(f"Total barrels = {totalbarrels}")
    print("Enter the number of locks and to exit press -1")
    locks = int(input())

print(f"Total locks = {totallocks}")
print(f"Total stocks = {totalstocks}")
print(f"Total barrels = {totalbarrels}")

locksales = totallocks * lockprice
stocksales = totalstocks * stockprice
barrelsales = totalbarrels * barrelprice

sales = locksales + stocksales + barrelsales

print(f"Total sales = {sales}")
comm = 0
if sales>1800:
    comm = 0.10 * 1000
    comm = comm + (0.15 * 800)
    comm = comm + 0.20 * (sales - 1800)
elif sales>1000:
    comm = 0.10 * 1000
    comm = comm + 0.15 * (sales - 1000)
else:
    comm = 0.10 * sales

print(f"Commission = {comm}")




    
