import math

class Fraction():
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator', numerator, 'must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('Denominator', denominator, 'must be an integer')
        self.numerator = numerator
        self.denominator = denominator


        # Use the math package to find the greatest common divisor
        greatest_common_divisor = math.gcd(self.numerator, self.denominator)
        if greatest_common_divisor > 1:
            self.numerator = self.numerator // greatest_common_divisor
            self.denominator = self.denominator // greatest_common_divisor
        self.value = self.numerator / self.denominator


        # Normalize the sign of the numerator and denominator
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def get_value(self):
        return self.value

    def __str__(self):
        """ Create a string reperesentation of the fraction """
        output = ' Fraction: ' + str(self.numerator) + '/' + \
            str(self.denominator) + '\n' + \
                ' Value: ' + str(self.value) + '\n'
        return output

    
    def __add__(self, oOtherFraction):
        """ Add Two fraction objects """
        if not isinstance(oOtherFraction, Fraction):
            raise TypeError('Second value in attempt to add is not a Fraction')
            # Use the math package to find the least common multiple
        new_denominator = math.lcm(self.denominator, oOtherFraction.denominator)

        multiplication_factor = new_denominator // self.denominator
        equivelant_numerator = self.numerator * multiplication_factor

        other_multiplaction_factor = new_denominator // oOtherFraction.denominator
        oOtherFraction_equivalant_numerator = oOtherFraction.numerator * other_multiplaction_factor

        new_numerator = equivelant_numerator + oOtherFraction_equivalant_numerator

        oAddedFraction = Fraction(new_numerator, new_denominator)
        return oAddedFraction

    def __eq__(self, oOtherFraction):
        """ Test for equality """
        if not isinstance(oOtherFraction, Fraction):
            return False #not comparing to a fraction
        if (self.numerator == oOtherFraction.numerator) and \
            (self.denominator == oOtherFraction.denominator):
            return True
        else:
            return False


Ofraction1 = Fraction(1,3) #create a Fraction object
Ofraction2 = Fraction(2,5)
print('Fraction1\n', Ofraction1)
print('Fraction2\n', Ofraction2)

oSumFraction = Ofraction1 + Ofraction2
print("Sum is \n", oSumFraction)

print("Are fractions 1 and 2 equal?", (Ofraction1 == Ofraction2))
print()

Ofraction3 = Fraction(-20, 80)
Ofraction4 = Fraction(4, -16)
print('Fraction3\n', Ofraction3)
print('Fraction4\n', Ofraction4)
print("Are fractions 3 and 4 equal?", (Ofraction3 == Ofraction4))
print()

Ofraction5 = Fraction(5, 2)
Ofraction6 = Fraction(500, 200)
print('Sum of 5/2 and 500/2\n', Ofraction5 + Ofraction6)