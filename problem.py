# fizzbuzz problem
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
    
# count odd Number in an interval range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
       return (high+1)//2 - low//2
   
   
# # how many numbers are smaller than the current number
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
#         result = [] 
#         for i in nums:
#             c = 0
#             for j in nums:
#                 if j < i:
#                     c += 1
#             result.append(c)
#         return result
    
    
# #  Count the Digits With Even Number of Digits
# class Solution:
#     def findNumbers(self, nums: list[int]) -> int:
        