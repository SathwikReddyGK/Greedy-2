# Solution

# // Time Complexity :  O(N^2)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Sort acending the queue based on height and if height is same then sort acending on number of people
# ahead. Now just putting each in the respective indexs should work, since adding smaller heights elements infront of 
# larger heights elements.
# https://www.youtube.com/watch?v=7ly2mpKEVmo

from collections import deque
from functools import cmp_to_key

def compare(item1,item2):
        if item1[0] < item2[0]:
            return 1
        elif item1[0] == item2[0]:
            if item1[1] > item2[1]:
                return 1

        return -1

def reconstructQueue(people):
    peopleSort = sorted(people, key=cmp_to_key(compare))
    queue = deque()
    result = []

    for peeps in peopleSort:
        queue.insert(peeps[1],peeps)
    
    while queue:
        result.append(queue.popleft())
    
    return result

if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] 
    print(reconstructQueue(people))