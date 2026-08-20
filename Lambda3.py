1.#An online store stores product prices in a list. Write a program using map() to apply a 10% tax
# to each product price and display the updated prices.
prices = [100,200,250,370]
def addtax(x):
    return x + x * 0.1
final_prices =list(map(lambda x : x + x * 0.1, prices))
print(final_prices)

2.#A list of usernames is stored in lowercase. Use map() to format them so that the first letter is uppercase.
usernames=["hemu","khadri","syam","teja"]
f= list(map(lambda x : len(x), usernames))
print(f)

7.#Use filter() with a lambda function to select numbers that are multiples of 4.
l=[10,20,30,40,50]
l1=list(map(lambda x : x**2, l))
l2=list(filter(lambda x : x%4==0,list(map(lambda x : x**2, l))))
print(l1)
print(l2)
print(l)

