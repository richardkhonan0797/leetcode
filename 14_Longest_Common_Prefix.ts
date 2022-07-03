function longestCommonPrefix(strs: string[]): string {
    let res = "";
    
    let minLength = findMinLength(strs);
    
    for (let i = 0; i < minLength; i++) {
        let comp = strs[0][i];
        
        for (let j = 0; j < strs.length; j++) {
            if (strs[j][i] !== comp) return res;
        }
        
        res += strs[0][i];
    }
    
    return res;
};
    
function findMinLength(strs: string[]): number {
    let min = strs[0].length;
    
    for (let i = 1; i < strs.length; i++) {
        if (strs[i].length < min) {
            min = strs[i].length;
        }
    }
    
    return min;
};
