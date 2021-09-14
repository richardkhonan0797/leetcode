"""
557. Reverse Words in a String III
Easy

1719

117

Add to List

Share
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""

def reverseWords(s: str) -> str:

    # 1st solution
    # s = s.split(" ")
    
    # for i in range(len(s)):
    #     string = list(s[i])
    #     string[:] = string[::-1]
    #     string = "".join(string)

    #     s[i] = string
    
    # s = " ".join(s)

    # return s

    # One liner
    return " ".join(string[::-1] for string in s.split())

print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))
