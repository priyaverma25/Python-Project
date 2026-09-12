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
#         count = 0
#         for num in nums:
        
        
        

    
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



# Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
        #     return False

        # original = x
        # reverse = 0

        # while x > 0: 
        #     digit = x % 10 
        #     reverse = reverse * 10 + digit
        #     x = x // 10

        # return original == reverse  


# Kids with the Greatest Number of Conkies
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

# Recursion
# Power of Two
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         # while n%2==0:
#         #     n//2
#         # return n==1
        
# base case of recursive 
        # if n<=0:
        #     return False
        # if n==1:
        #     return True
        # if n%2!=0:
        #     return False
        # # recursive case 
        # return self.isPowerOfTwo(n//2)
    
    
# Power of Three
# class Solution: 
#     def isPowerofThree(self, n: int) -> bool:
#         if n<=0:
#             return False
#         if n==1:
#             return True
#         if n%3!=0:
#             return False
#         return self.isPowerofThree(n//3)
    
# # Power of four
# class Solution:
#      def isPowerofFour(self, n: int) -> bool:
#        if n<=0:
#           return False
#        if n==1:
#          return True
#        if n%4!=0:
#          return False
#        return self.isPowerofFour(n//4)

# # pow(x,n) 
# class Solution:
#   def findPow(self, x: float, n: int) -> float:
#     #   base case
#     if n==0:
#         return 1
#     # recursive case
#     a = self.findPow(x, n//2)
#     if n%2==0:
#         return a*a
#     else:
#         return a*a*x 
#   def myPow(self, x: float, n: int) -> float:
#         if n>=0:
#             return self.findPow(x, n)
#         else:
#             return 1/self.findPow(x, n*(-1))
  
# # fibonacci number
# class Solution:
#     def fib(self, n: int) -> int:
#         # base case
#         if n==0:
#             return 0
#         if n==1:
#             return 1
#         # recursive case
#         return self.fib(n-1)+self.fib(n-2) 

# # N-th tribonacci number
# class Solution:
#     def tribonacci(self, n: int) -> int:
#         # base case
#         if n==0:
#             return 0
#         if n==1 or n==2:
#             return 1
#         # recursive case
#         return self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
  
  
# Running Sum of 1d Array  
# class Solution:
#     def runningSum(self, nums: list[int]) -> list[int]:
#         n = len(nums) 
#         ans = []
#         ans.append(nums[0])
#         for i in range(1, n):
#             x = ans[i-1]+nums[i]
#             ans.append(x)
#         return ans    
                   
                   
# # # Remove Duplicates from Sorted Array (day11)
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         n = len(nums)
#         start = 0
#         for i in range(1, n):
#             # unique element found
#             if nums[i] != nums[start]:
#                 start+=1
#                 nums[start] = nums[i]
                
#         return start+1
 
# # Remove Duplicates from Sorted Array II  
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         n = len(nums)
        
#         if n<=2:
#             return n
        
#         start = 1
#         for i in range(2, n):
#             # unique element found
#             if nums[i] != nums[start-1]:
#                 start+=1
#                 nums[start] = nums[i]
                         
#         return start+1
    
# Sort Array By parity
# class Solution: 
#     def sortArrayByParity(self, nums: list[int]) -> list[int]:
#         n = len(nums)
        
#         start = 0
#         for i in range(n):
#             if nums[i]%2==0:
#                 temp = nums[i]
#                 nums[i] = nums[start]
#                 nums[start] = temp
#                 start+=1
#         return nums 
    
#  Sort Array by parity II
# class Solution:
#     def sortArrayByParityII(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         result = [0]*n
        
#         even = 0
#         odd = 1
        
#         for num in nums:
#             if num % 2 == 0:
#                 result[even] = num
#                 even += 2
#             else:
#                 result[odd] = num
#                 odd += 2
                    
#         return result

# Maximum Subarray (day13)
# class Solution:
#     def maxSubArray(self, nums: list[int]) -> int:
#         curr_sum = 0
#         max_sum = nums[0]
        
#         for i in range(len(nums)):
#             curr_sum += nums[i]
#             if curr_sum > max_sum:
#                 max_sum = curr_sum
#                 if curr_sum < 0:
#                     curr_sum = 0
#         return max_sum      
    
    
# #  Best time to buy and sell stock
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         min_price = prices[0]
#         profit = 0
       
#         for i in range(1, len(prices)):
#             curr_profit = prices[i] - min_price
#             if curr_profit > profit:
#                profit = curr_profit
#             min_price = min(min_price, prices[i])
            
#         return profit        
    
#  Best time to buy and sell stock II
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         profit = 0
#         n = len(prices)
        
#         for i in range(n-1):
#             if prices[i+1] > prices[i]:
#                 profit += prices[i+1] - prices[i]
#         return profit
  
  
# best time to buy and sell stock III(day16)
# class Solution:
#         def maxProfit(self, prices: list[int]) -> int:
                
#                 buy1  = float('-inf')
#                 sell1 = 0
                
#                 buy2 = float('-inf')
#                 sell2 = 0
                
#                 for price in prices:
#                         buy1 = max(buy1, -price)
#                         sell1 = max(sell1, buy1 + price)
#                         buy2 = max(buy2, sell1 - price)
#                         sell2 = max(sell2, buy2 + price)
#                 return sell2        
                

# # Richest customer wealth
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         ans = 0
#         for account in accounts:
#             ans = max(ans, sum(account))
#         return ans
    
    
    
# Spiral matrix
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        
        total = n*m
        ans = []
        c = 0
        
        colstart = 0
        rowstart = 0
        colend = m-1
        rowend = n-1
        
        while c < total:
            # rowstart, colstart->colend
            for i in range(colstart, colend+1):
                ans.append(matrix[rowstart][i])
                c+=1
            rowstart+=1    
            
            if c==total:
                break
            
            # colend, rowstart->rowend
            for i in range(rowstart, rowend+1):
                ans.append(matrix[i][colend])
                c+=1
            colend-=1
            if c==total:
                break
            # rowend, colend->colstart
            for i in range(colend, colstart-1, -1):
                ans.append(matrix[rowend][i])
                c+=1
            rowend-=1
            if c==total:
                break
            # colstart, rowend->rowstart
            for i in range(rowend, rowstart-1, -1):
                ans.append(matrix[i][colstart])
                c+=1
            colstart+=1
        return ans         
    
    
# # Defanging an IP Address
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         ans = ""
#         for i in address:
#             if i!=".":
#                 ans+=i
#             else:
#                 ans+="[.]"
#         return ans            
    
#         # return address.replace(".", "[.]")
    
# # Valid palindrome
# class Solution:
#     def isAlphanumeric(s):
#         x = ord(s)
#         if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
#             return True
#         return False
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         i = 0
#         j = len(s)-1
#         while i<j:
#             if not self.isAlphanumeric(s[i]):
#                 i+=1
#             elif not self.isAlphanumeric(s[j]):
#                 j-=1    
#             elif s[i]==s[j]:
#                 i+=1
#                 j-=1
#             else:
#                 return False    
#         return True
    
# # Reverse String
# class Solution:
#     def reverseString(self, s: list[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         i = 0
#         j = len(s)-1
        
#         while i<j:
#             temp = s[i]
#             s[i] = s[j]
#             s[j] = temp
#             i+=1
#             j-=1
# # s.reverse()
        
# # Reverse Words in a String
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         s = s.strip()
#         s = s.split()
#         s.reverse()
#         return " ".join(s)
    
# # Length of last Word
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip()
#         n = len(s)
#         i = n-1
#         while i>=(-1*n) and s[i]!=" ":
#             i-=1
#         i+=1
#         i*=-1
#         return i  

# # two sum
# from email.headerregistry import Group
# from itertools import repeat
# import re


# class Soiution:
#         def twoSum(self, nums: list[int], target: int) -> list[int]:
#                 n = len(nums) 
#                 dict = {}
                
#                 for i in range(n):
#                         rem = target - nums[i]
#                         if rem in dict:
#                                 return [dict[rem], i]
#                         dict[nums[i]] = i
                        
# # Two Sum II - Inpu array is sorted
# class Solution:
#         def twoSum(self, nums: list[int], target: int) -> list[int]:
#             left = 0
#             right =  len(nums)-1
            
#             while left<right:
#                 sum1 = nums[left]+nums[right]
#                 if sum1==target:
#                     return [left+1, right+1]
#                 elif sum1<target:
#                     right-=1
#                 else:
#                     left+=1               
                
                
#                 # n = len(nums) 
#                 # dict = {}
                        
#                 # for i in range(n):
#                 #     rem = target - nums[i]
#                 #     if rem in dict:
#                 #         return [dict[rem]+1,i+1]
#                 #     dict[nums[i]] = i
                                
# # intersection of two arrays
# class Solution:
#         def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
#             set1 = set(nums1)
#             set2 = set(nums2)
            
#             return list(set1.intersection(set2))
        
# # return list(set(nums1) & set(nums2))
 
# # intersection of two arrays II
# class Solution:
#         def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
#                 dict = {}
#                 result = []
                 
#                 for num in nums1:
#                         dict[num] = dict.get(num, 0) + 1
                
#                 for num in nums2:
#                         if num in dict and dict[num] > 0:
#                           result.append(num)
#                           dict[num] -= 1
                
#                 return result


# # First Unique Character in a string
# class Solution:
#         def firstUniqChar(self, s: str) -> int:
#             dict = {}
#             for i in s:
#                 if i not in dict:
#                     dict[i] = 1
#                 else:
#                     dict[i] += 1
                               
#                 for i in range(len(s)):
#                     if dict[s[i]] == 1:
#                       return i                       
#                 return -1
        
# # valid anagram
# class Solution:
#      def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#              return False
         
#         dict = {}
#         for i in s:
#             dict[i] = dict.get(i, 0) + 1
         
#         for i in t:
#            if i not in dict:
#                 dict[i] = 1     
#            else:
#                 dict[i] += 1
                
#         for i in t:
#             if i not in dict:
#                 return False
#             else:
#                 dict[i] -= 1
                
#         for i in dict.values():  
#             if 1!=0:
#                 return False
        
#         return True

# # Group Anagrams
# class Solution:
#      def sortString(self,s): 
#         s1 = list(s)
#         s.sort()
#         return "".join(s)
#      def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
#         dict1 = {}
        
#         for s in strs:
#             key = self.sortString(s)
#             if key in dict1:
#                 dict1[key].append(s)
#             else:                
#                 dict1[key] = [s]
                
#         return (dict1.values())        
 
# # Substrings of size Three with distinct characters
# class Solution:
#      def countGoodSubstrings(self, s: str) -> int:
#         n = len(s)
#         ans = 0 
        
#         for i in range(n-2):
#             if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
#                 ans+=1
        
#         return ans

# # longest substring without repeating characters
# class Solution:
#      def lengthOflongestSubstring(self, s: str) -> int:
#         n = len(s)
#         if n==0: 
#              return 0                                 
 
#         ans = 1
#         set1 = set({})
#         set1.add(s[0])
        
#         i = 0
#         j = 1
        
#         while j<n:
#              while s[j] in set1:
#                 set.discard(s[i])
#                 i+=1
#              set.add(s[j])
#              j+=1
#              ans = max(ans,(j-i))
             
#         return ans  





              
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 