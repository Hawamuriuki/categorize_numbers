
class CategorizeNumbers:
  '''
  Constructor
  '''
  def __init__(self):
    self.start = int(input("Enter the start of range:"))
    self.end = int(input("Enter the end of range:"))

  '''
  Function print Odd Numbers in given range

  An odd number is a number that is not divisible by 2.
  '''
  def get_odd_numbers(self):
    # iterating each number in list
    odd_numbers = []
    for num in range(self.start, self.end + 1):

        # checking condition
        if num % 2 != 0:
            odd_numbers.append(num)
    print("Odd numbers in given range",self.start,":",self.end,"are:")
    print(odd_numbers)

  '''
    Function print Even Numbers in given range

    An even number is a number that is divisible by 2.
  '''
  def get_even_numbers(self):
    # iterating each number in list
    even_numbers = []
    for num in range(self.start, self.end + 1):

        # checking condition
        if num % 2 == 0:
            even_numbers.append(num)
    print("Even numbers in given range",self.start,":",self.end,"are:")
    print(even_numbers)

  '''
      Function to print Prime Numbers in given range.

      A prime number is a natural number greater than 1 that
      has no positive divisors other than 1 and itself.

      Negative numbers, 0 and 1 are not primes
  '''
  def get_prime_numbers(self):
    # iterating each number in list
    prime_numbers = []
    for num in range(self.start, self.end + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    print("Prime numbers in given range",self.start,":",self.end,"are:")
    print(prime_numbers)

  '''
  Main Function
  '''
  def main(self):
    # Calling Each Function
    CategorizeNumbers.get_odd_numbers(self)
    CategorizeNumbers.get_even_numbers(self)
    CategorizeNumbers.get_prime_numbers(self)

# Initialize
cn = CategorizeNumbers()
# Calling main Function
cn.main()