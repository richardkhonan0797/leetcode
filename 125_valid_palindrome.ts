/*
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
*/

function isPalindrome(s: string): boolean {
    if (s.length === 1) return true;
    
    let charsOnly = "";
    
    for (let i = 0; i < s.length; i++) {
        let ascii = s.charCodeAt(i);
        if (
            ascii >= 48 && ascii <= 57 ||
            ascii >= 65 && ascii <= 90 || 
            ascii >= 97 && ascii <= 122
        ) {
            charsOnly += s[i].toLowerCase();
        }
    }
    
    let i = 0;
    let j = charsOnly.length - 1;
    
    while (i < j) {
        if (charsOnly[i] !== charsOnly[j]) return false;
        i++;
        j--;
    }
    
    return true;
};
