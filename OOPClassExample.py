class Customer:
    name_f = ""
    name_l = ""
    age = 0
    gender = ""

    def addCart(self):
        print("Added to %s's cart!" %(self.name_f))

customer1 = Customer()
customer1.name_f = "Thachin"
customer1.name_l = "Wisutimarkul"
customer1.age = 22
customer1.gender = "M"
customer1.addCart()

customer2 = Customer()
customer2.name_f = "Worraruthai"
customer2.name_l = "Ruangsuksriwong"
customer2.age = 24
customer2.gender = "F"
customer2.addCart()

customer3 = Customer()
customer3.name_f = "Anotherone"
customer3.name_l = "Bitetodust"
customer2.age = 40
customer3.gender = "M"
customer3.addCart()