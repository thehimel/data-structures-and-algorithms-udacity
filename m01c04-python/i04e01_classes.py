class Person:
    def __init__(self, name, age, married):
        # Public members
        self.name = name
        self.age = age

        # Private member
        self.__married = married

    # Mutator
    def birthday(self):
        self.age += 1

    # Accessor
    def getName(self):
        return self.name

    # Accessor
    def isMarried(self):
        return self.__married


bob = Person('Bob', 32, True)
print(bob.getName())
# prints Bob

bob.birthday()
print(bob.age)
# prints 33

print(bob.isMarried())
