class Comedian:
    def __init__(self, joke):
        self.__joke = joke

    def change_joke(self, joke):
        self.__joke = joke

    def get_joke(self):
        return self.__joke

def process(c):
    # line A
    c[1] = Comedian("joke3")
    c.append(Comedian("joke4"))
    c = c + [Comedian("joke5")]
    c[0].change_joke("joke6")
    
c1 = Comedian("joke1")
c2 = Comedian("joke2")
com = [c1,c2]
process(com)
c1 = Comedian("joke7")
for c in com:
    print(c.get_joke())
