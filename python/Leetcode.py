
# # 1. Two Sum
# class Solution:
#     def twoSum(self, nums, target):   
#      for i in range(len(nums)):
#       for j in range(i + 1, len(nums)):
#          if nums[i] + nums[j] == target:
 
# # Palindrome Number
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         return str(x) == str(x)[::-1]

# #Roman to Integer
# class Solution:
#     def romanToInt(self, s: str) -> int:

#         roman = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }

#         total = 0

#         for i in range(len(s) - 1):
#             if roman[s[i]] < roman[s[i + 1]]:
#                 total -= roman[s[i]]
#             else:
#                 total += roman[s[i]]

#         total += roman[s[-1]]

#         return total

# #Valid Parentheses
# class Solution:
#     def isValid(self, s: str) -> bool:

#         prev = ""

#         while prev != s:
#             prev = s
#             s = s.replace("()", "")
#             s = s.replace("[]", "")
#             s = s.replace("{}", "")

#         return s == ""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# #Merge two sorted list
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         current = dummy
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
#         if list1:
#             current.next = list1
#         else:
#             current.next = list2
#         return dummy.next

# #Remove Duplicates from Sorted Array
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         if not nums:
#             return 0

#         i = 0
#         for j in range(1,len(nums)):
#             if nums[j] != nums[i]:
#                 i += 1
#                 nums[i] = nums[j]
#         return i + 1

        