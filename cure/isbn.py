import random

class Isbn:
    def __init__(self):
        self.prefix = '978'
        self.body = self.generate_random_body()
        self.check_digit = self.calculate_check_digit(self.prefix + self.body)
        self.isbn = self.prefix + self.body + str(self.check_digit)

    def generate_random_body(self):
        return ''.join(str(random.randint(1,9)) for _ in range(9))

    def calculate_check_digit(self, base):
        total = 0
        for i , digit in enumerate(base):
            factor = 1 if i % 2 == 0 else 3
            total += int(digit) * factor
        remainder = total % 10
        return (10 - remainder) if remainder != 0 else 0
    def __str__(self):
        return f'{self.isbn}'

