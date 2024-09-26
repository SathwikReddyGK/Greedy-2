# Solution

# // Time Complexity :  O(N)
# // Space Complexity : O(N)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

# // Your code here along with comments explaining your approach
# Greedy Solution - Find the last index of all characters so that when we run on the string again we will know the end index
# once, before going to end if we find any other character whose end index is greater then that becomes end index
# https://www.youtube.com/watch?v=7ly2mpKEVmo

def partitionLabels(s):
    minMaxDict = {}
    result = []

    for i in range(len(s)):
        if s[i] in minMaxDict:
            minMaxDict[s[i]][1] = i
        else:
            minMaxDict[s[i]] = [i,i]
    
    start = 0
    end = None
    for i in range(len(s)):
        if i == end:
            result.append(end - start + 1)
            end = None
            start = i+1
            continue

        if end == None:
            end = minMaxDict[s[i]][1]
            if start == end:
                result.append(1)
                end = None
                start = i+1
                continue
        elif end < minMaxDict[s[i]][1]:
            end = minMaxDict[s[i]][1]
    
    return result

if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(partitionLabels(s))