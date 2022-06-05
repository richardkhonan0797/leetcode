function isAnagram(s: string, t: string): boolean {
    let unicode = Array(26).fill(0);
    
    if (s.length !== t.length) return false;
    
    for (let i = 0; i < s.length; i++) {
        unicode[s.charCodeAt(i) - 97] += 1;
    }
    
    for (let i = 0; i < t.length; i ++) {
        unicode[t.charCodeAt(i) - 97] -= 1;
        if (unicode[t.charCodeAt(i) - 97] < 0) return false; 
    }
    
    return true;
};
