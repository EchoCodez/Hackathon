class Child():
    def __init__(self, name, age, wishlist, costs):
        self.name = name
        self.age = age
        self.wishlist = wishlist
        self.costs = costs

class Clout_Seeker():
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget


child_info = {"name": "HIJAKDSJN", 
"age": 2109831094804938501435, 
"wishlist": ["sadkfhgafjksfk", "dsjkahggfuyais8dyhbhf"],
"costs": ["$1309", "$2384"]}
childs = []
child = Child(child_info.get("name"), child_info.get("age"), child_info.get("wishlist"), child_info.get("costs"))
childs.append(Child)

print(child.name, child.age, child.wishlist, child.costs)




