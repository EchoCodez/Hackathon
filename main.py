class Child():
    def __init__(self, name, age, wishlist, cost):
        self.name = name
        self.age = age
        self.wishlist = wishlist
        self.cost = cost

child_info = {}
database = []
child = Child(child_info.get("name"), child_info.get("age"), child_info.get("wishlist"), child_info.get("cost"))
database.append(child)

print(child.name, child.age, child.wishlist, child.cost)


class Clout_Seeker():
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

cloutseeker_info = {"name": "Clout",
"budget": "$102103932104923840291348091234803219840319248103948093218440923184092318409" }

def connect():
    possible = []
    cloutseeker = Clout_Seeker(cloutseeker_info.get("name"), cloutseeker_info.get("budget"))
    for object in database:
        print(object.cost)
        if child.cost <= cloutseeker.budget:
            possible.append(child)

connect()





