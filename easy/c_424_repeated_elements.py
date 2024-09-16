"""
Given an array of integers in which two elements 
appear exactly once and all other elements appear exactly twice, 
find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], 
return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""
from abc import ABC, abstractmethod

# Solved using the strategy pattern
class ExtractElementsStrategy(ABC):
    """Abstract class for extracting elements"""

    @abstractmethod
    def extract_elements(self, array: list):
        """Abstract method for extracting elements"""
        raise NotImplementedError

class RegularStrategy(ExtractElementsStrategy):
    """Regular strategy class for extracting elements"""
    def extract_elements(self, array: list):
        unique_numbers = set(array)
        non_repeated_numbers = []
        for number in unique_numbers:
            count = 0
            for element in array:
                if number == element:
                    count += 1

            if count == 1:
                non_repeated_numbers.append(number)

        return non_repeated_numbers

class LinearStrategy(ExtractElementsStrategy):
    """Linear time and constant space extracting elements strategy"""
    def extract_elements(self, array: list):
        # XOR all elements. The result will be the XOR of the two unique numbers.
        xor_result = 0
        for num in array:
            xor_result ^= num

        # Find any set bit (1-bit) in xor_result.
        rightmost_set_bit = xor_result & -xor_result  # isolates the rightmost set bit

        # Divide numbers into two groups based on the rightmost set bit and XOR the groups
        num1, num2 = 0, 0
        for num in array:
            if num & rightmost_set_bit:  # If the bit is set, XOR in the first group
                num1 ^= num
            else:  # If the bit is not set, XOR in the second group
                num2 ^= num

        # num1 and num2 are the two unique numbers
        return [num1, num2]


class Context:
    """Context of the strategies"""
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        """Set strategy"""
        self._strategy = strategy

    def extract_elements(self, array: list):
        """Execute strategy"""
        return self._strategy.extract_elements(array)

if __name__ == "__main__":
    # data
    data = [2, 4, 6, 8, 10, 2, 6, 10]

    # two ways to solve the problem
    regular_approach = RegularStrategy()
    linear_approach = LinearStrategy()

    # regular execution
    context = Context(regular_approach)
    print("Extract elements O(n^2)")
    result = context.extract_elements(data)
    print(result)

    # linear time execution
    context.set_strategy(linear_approach)
    print("Extract elements O(n)")
    result = context.extract_elements(data)
    print(result)
