# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy  = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next =  list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    if list2:
        tail.next  = list2
    return dummy.next


# o(1) space and o(n+m) complexity
def mergeTwoListsAndPrintKitem(list1: Optional[ListNode], list2: Optional[ListNode],k:int) -> Optional[ListNode]:
    dummy  = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next =  list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    if list2:
        tail.next  = list2
    return dummy.next

# o(n+m) time complexity
# o(1) space complexity
def merge( nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # set p1 and p2 to point to the end of their respective arrys
        p1 = m -1 
        p2 = n-1
        last = m + n -1
        print(p1)
        print(p2)

     
        # and move p backward through the array1, each time writing the smallest value pointed at by p1 or p2/
        while p1 >= 0 and p2 >= 0:
            print(nums1)
            if nums1[p1] < nums2[p2]:
                nums1[last] = nums2[p2]
                p2-=1
            else:
                nums1[last] =  nums1[p1]
                p1 -=1
            last -=1
            print(nums1)

        while p2 >= 0:
            nums1[last] = nums2[p2]
            p2 ,last = p2-1,last-1
            print(nums1)


        
# o(n+m) space complexity
# o(n+m) time complexity
def mergeTwoSortedListsWithNoPlaceHolders(nums1, nums2):
    result = []
    i = j = 0
    nums1Len =  len(nums1)
    nums2Len =  len(nums2)


    
    while i < nums1Len and j < nums2Len:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i+=1
        else:
            result.append(nums2[j])
            j+=1
    
    while i < nums1Len:
        result.append(nums1[i])
        i+=1
    while j < nums2Len:
        result.append(nums2[j])
        j+=1
    
    return result


def mergeTwoSortedListsuntilKthElement(nums1, nums2,k):
    result = []
    i = j = 0
    nums1Len =  len(nums1)
    nums2Len =  len(nums2)


    
    while len(result)<k and i < nums1Len and j < nums2Len:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i+=1
        else:
            result.append(nums2[j])
            j+=1
    
    while len(result)<k and i < nums1Len:
        result.append(nums1[i])
        i+=1
    while len(result)<k and j < nums2Len:
        result.append(nums2[j])
        j+=1
    
    return result


def twosum(arr,target):
    seen = {}

    for i,n in enumerate(arr):
        complement = target - n
        if complement in seen:
            return [n,arr[complement]]
        seen[n] = i

def twosumWithAllPairs(arr,target):
    seen = set()
    pairs = set()

    for i,n in enumerate(arr):
        complement = target - n
        if complement in seen:
            pair = tuple(sorted[n,complement])
            pairs.add(pair)
        seen.add(n)

    return list(pairs)



def find_pairs_memory_optimal(arr, target_sum):
    """
    Find all distinct pairs that sum to target using minimal extra space
    Time: O(nlogn)
    Space: O(1) excluding output space
    """
    # Sort the array in-place to avoid extra space
    arr.sort()
    
    left = 0
    right = len(arr) - 1
    pairs = []
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        
        if curr_sum == target_sum:
            # Found a valid pair
            pairs.append((arr[left], arr[right]))
            
            # Skip duplicates for left pointer
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            # Skip duplicates for right pointer    
            while left < right and arr[right] == arr[right - 1]:
                right -= 1
                
            left += 1
            right -= 1
            
        elif curr_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return pairs


def find_most_frequent_substring(s, k):
    """
    Find the substring of length k with maximum occurrences
    
    Args:
        s: Input string
        k: Length of substring to find
        
    Returns:
        tuple: (most_frequent_substring, count)
    """
    # Edge cases
    if not s or k <= 0 or k > len(s):
        return None, 0
        
    # Store frequency of each substring
    substring_count = {}
    
    # Generate all substrings of length k
    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        substring_count[substring] = substring_count.get(substring, 0) + 1
    
    # Find substring with maximum frequency
    max_substring = max(substring_count.items(), key=lambda x: x[1])
    return max_substring



# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(4)

# list2 = ListNode(1)
# list2.next = ListNode(3)
# list2.next.next = ListNode(4)


# list3=mergeTwoLists(list1,list2)

# while list3:
#     print(list3.val)
#     list3=list3.next



# list1 = [0]
# list2 =  [2]
# merge(list1,0,list2,1)

# print(list1)


arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
k = 5

result = mergeTwoSortedListsuntilKthElement(arr1, arr2,300)
print(result)