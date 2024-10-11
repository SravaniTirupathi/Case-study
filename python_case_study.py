class Product:

    products={}

    def __init__(self,id,name,category,cost):

        self.id=id

        self.name=name

        self.category=category

        self.cost=cost

        self.products[self.id]={"name":self.name,"category":self.category,"cost":self.cost}

        print("Added successfully...")

    @classmethod

    def updateProduct(self,id,cost):

        self.products[id]["cost"]=cost

        print("Updated successfully...")

    @classmethod

    def deleteProduct(self,id):

        self.products.pop(id)

        print("Deleted successfully...")

    @classmethod

    def getProductByid(self,id):

        print(self.products[id])  

    @classmethod

    def getAllProduct(self):

        if(len(self.products)>=1):

            for i in list(self.products.items()):

                print(i)

        else:

            print("There are no products")

    @classmethod

    def getProductByCategory(self,category):

        values=list(self.products.values())

        for value in values:

            if(value["category"]==category):

               print(value)

    @classmethod

    def getProductBetweenPrices(self,min,max):

        for value in list(self.products.values()):

            if(value["cost"]>=min and value["cost"]<=max):

                print(value)

while(True):

   

    print('''1.Add product

    2.Update product

    3.Delete product

    4.Get product by id

    5.Get all products

    6.Get product by category

    7.Get product between prices

    8.Exit''')

    choice =int(input("What do you want to do?"))

    if(choice==1):

        id=int(input("enter id "))

        name=input("enter product name ")

        category=input("enter category ")

        cost=float(input("enter cost "))

        product=Product(id,name,category,cost)

    elif(choice==2):

        id=int(input("enter id "))

        cost=input("enter cost ")

        Product.updateProduct(id,cost)

    elif(choice==3):

        id=int(input("enter id "))

        Product.deleteProduct(id)

    elif(choice==4):

        id=int(input("enter id "))

        Product.getProductByid(id)

    elif(choice==5):

        Product.getAllProduct()

    elif(choice==6):

        category=input("enter category ")

        Product.getProductByCategory(category)

    elif(choice==7):

        c1=int(input("enter minimum cost "))

        c2=int(input("enter maximum cost "))

        Product.getProductBetweenPrices(c1,c2)

    else:

        print("Exit")

        break

   