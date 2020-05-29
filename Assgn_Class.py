class Fruit:
    prop1="sweet"
    prop2="sour"
    prop3="red"
    def juice(self,fruit):
        print(Fruit.prop1+fruit +'juice is ready')
    def jam(self,fruit):
        print(Fruit.prop2+ fruit+' jam is ready')
    def salad(self,fruit):
        print(Fruit.prop3+fruit+' salad is ready')

ob = Fruit()
ob.juice('papaya')
ob.jam('papaya')
ob.salad('papaya')
