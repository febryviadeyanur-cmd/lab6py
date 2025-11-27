import math

# Mengubah fungsi menjadi lambda
a = lambda x: x**2
b = lambda x, y: math.sqrt(x**2 + y**2)
c = lambda *args: sum(args) / len(args) if args else 0
d = lambda s: "".join(set(s))

# Contohnya
print(a(7))          # Output: 49
print(a(-3))         # Output: 9
print(a(2.5))        # Output: 6.25
print("hello python")