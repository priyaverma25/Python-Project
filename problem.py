# # fizzbuzz problem
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         result = []
#         for i in range(1, n + 1):
#             if i % 15 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))
#         return result
    
# # count odd Number in an interval range
# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#        return (high+1)//2 - low//2
   
   
# how many numbers are smaller than the current number
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        result = [] 
        for i in nums:
            c = 0
            for j in nums:
                if j < i:
                    c += 1
            result.append(c)
        return result
    
    
# #  Count the Digits With Even Number of Digits
# class Solution:
#     def findNumbers(self, nums: list[int]) -> int:
#         count = 0
        
        
        
        
# # Count the Digits that divide the number
# class Solution:
#     def countDigits(self, num: int) -> int:
#         temp = num
#         ans = 0
#         while temp>0:
#             r =temp%10
#             if num%r==0:
#                 ans+=1
#             temp //= 10
            
#         return ans
    
# # subtract the product and sum of digits of an integer
# class Solution:
#     def subtractProductAndSum(self, n: int) -> int:
#         temp = n
#         sum = 0
#         product = 1
#         while temp>0:
#             r = temp % 10
#             product *= r
#             sum += r
#             temp //= 10
            
#         return product - sum



# # Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         original = x
#         reverse = 0

#         while x > 0: 
#             digit = x % 10 
#             reverse = reverse * 10 + digit
#             x = x // 10

#         return original == reverse  


# # Kids with the Greatest Number of Conkies
# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         max_candies = max(candies)
#         result = []
#         for candy in candies:
#             if (candy+extraCandies) >= max_candies:
#                 result.append(True)
#             else:
#                 result.append(False)
#         return result
    
    