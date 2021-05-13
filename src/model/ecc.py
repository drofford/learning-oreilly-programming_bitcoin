class FieldElement:

    def __init__(self, num, prime):
        if prime < 1:
            raise ValueError("Prime {} must be greater than 0".format(prime))
        if num >= prime:
            raise ValueError("Num {} not in field range 0 to {}".format(num, prime-1))
        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.num, self.prime)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __add__(self, other):
        if other is None:
            raise ValueError("Cannot add a null object")
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different fields")
        num = (self.num + other.num) % self.prime
        return self.__class__(num, self.prime)
        
