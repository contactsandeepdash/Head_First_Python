class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i

    def increase(self) -> None:
        self.val += self.incr

    def __repr__(self) -> str:
        return str(self.val)
    
print("c")
c = CountFromBy()
print(c)
c.increase()
c.increase()
c.increase()
print(c)

print("d")
d = CountFromBy(100)
print(d)
d.increase()
d.increase()
d.increase()
print(d)

print("e")
e = CountFromBy(100, 10)
print(e)
e.increase()
e.increase()
e.increase()
print(e)

print("f")
f = CountFromBy(0, 15)
print(f)
for j in range(3):
    f.increase()
print(f)