function longestCommonPrefix(strs: string[]): string {
    let res = strs[0];
    
    for (let i = 1; i < strs.length; i++) {
        let temp = "";
        
        if (res.length === 0) break;
        
        if (res.length < strs[i].length) {
            for (let j = 0; j < res.length; j++) {
                if (res[j] === strs[i][j]) {
                    temp += res[j];   
                } else {
                    res = temp;
                    break;
                }
            }
            res = temp;
        } else {
            for (let j = 0; j < strs[i].length; j++) {
                if (res[j] === strs[i][j]) {
                    temp += res[j];
                } else {
                    res = temp;
                    break;
                }
            }
            res = temp;
        }
    }
    
    return res;
};
