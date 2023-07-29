class IntegerToRoman:
    def __init__(self):
        self.numeral_map = (('M', 1000),
                            ('CM', 900),
                            ('D', 500),
                            ('CD', 400),
                            ('C', 100),
                            ('XC', 90),
                            ('L', 50),
                            ('XL', 40),
                            ('X', 10),
                            ('IX', 9),
                            ('V', 5),
                            ('IV', 4),
                            ('I', 1))

    def to_roman(self, num):
        """Converts an integer to a Roman numeral."""
        result = ''
        for numeral, integer in self.numeral_map:
            while num >= integer:
                result += numeral
                num -= integer
        return result
converter = IntegerToRoman()
print(converter.to_roman(int(input("Enter a num to convert: "))))  
