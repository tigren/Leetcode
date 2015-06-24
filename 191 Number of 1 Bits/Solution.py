class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        result = 0
        binary = bin(n)
        for digit in binary:
            if digit is '1':
                result += 1
        return result
        