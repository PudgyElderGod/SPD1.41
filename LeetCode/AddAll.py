"""
Problem:
    Given a non-negative integer number, repeatedly add all of its digits until the result has only one digit.

Example:
    Input: 38
    Output: 2 
    Quickmaffs: 3 + 8 = 11, 1 + 1 = 2. 
                Since 2 has only one digit, it returns 2.
"""

class Calculator:
    def addDigits(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        print(num, " --> ", digits)
        size = len(digits)
        print("size", size, "output", num, "\n")
        if size == 1: return num
        else:
            out = 0
            for digit in digits:
                out += digit
            out + self.addDigits(out)



if __name__ == "__main__":
    solution = Calculator()
    result = solution.addDigits(38)
    print(result, "\n")