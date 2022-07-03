function strStr(haystack: string, needle: string): number {
    let i = 0;
    let j = needle.length;
    
    while (j <= haystack.length) {
        let sub = haystack.substring(i, j);
        if (sub === needle) return i;
        i++;
        j++;
    }
    
    return -1;
};
