def show(product,selling):
    if(product>selling):
        print("it is a profit of",product-selling)
    elif(selling>product):
        print("it is a loss of",selling-product)
x=int(input("enter a product price"))
y=int(input("enter a selling price"))
show(x,y)
