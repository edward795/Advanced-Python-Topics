class Parrot:
    def fly(self):
        print("Parrot can fly.")

    def swim(self):
        print("Parrot can't swim.")


class Penguin:
    def fly(self):
        print("Penguin can't fly.")

    def swim(self):
        print("Penguin can swim.")

#common interface -- implements polymorpishm

def flying_test(bird):
    bird.fly()

p=Parrot()
pe=Penguin()

flying_test(p)
flying_test(pe)