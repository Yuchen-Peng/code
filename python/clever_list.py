# using list comprehension
a = list(range(100))
a_square = [e**2 for e in a]
a_odd_ind = [0 if e%2 else 1 for e in a]
