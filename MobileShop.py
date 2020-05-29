print('Clix Mobile Shop')
n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit'))

SNO=['SNO',1,2,3,4,5]
Product=['Product','SmartPhone','HeadPhones','ScreenGaurd','Chargers','MemoryCards']
In_Stock=['   InStock',20,100,200,100,120]
Price=['Price',200,30,5,10,50]
while(1):
    
    if n==1:
        for i in range(len(Product)):
            print(SNO[i],Product[i],In_Stock[i],Price[i],sep='\t')
        n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit'))
    elif n==2:
        m,q=int(input('Which item',)),int(input('Quantity'))
        if q>In_Stock[m]:
            print('not enough qty')
        print(q*Price[m])
        In_Stock[m]=In_Stock[m]-q
        n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit'))
    elif n==3:
        p,i,pr=input('Enter name'),int(input('In_Stock')),int(input('Price'))
        Product.append(p)
        In_Stock.append(i)
        Price.append(pr)
        w=len(SNO)
        SNO.append(w)
        n= int(input('1.Show All Products\n2.Buy Product\n3.Add Product\n4.Exit'))
    elif n==4:
        break
