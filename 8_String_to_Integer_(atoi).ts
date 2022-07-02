function myAtoi(s: string): number {
    let res: number = 0;
    let mul: number = 1;
    let stop: boolean = false;
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ' && stop !== true) {
            continue;
        }
        
        if (['.', '-', '+'].includes(s[i]) && stop !== true) {
            if (s[i] === '-') {
                mul *= -1;
                stop = true;   
                continue;
            }
            
            if (s[i] === '+') {
                stop = true;
                continue;
            }
            
            if (s[i] === '.') break;
        }
        
        if (parseInt(s[i]) || parseInt(s[i]) === 0) {
            res = res * 10 + parseInt(s[i]);
            stop = true;
        } else {
            break;
        }
    }
    
    if (res * mul < (-2) ** 31) return (-2) ** 31;
    if (res * mul > 2 ** 31 - 1) return 2 ** 31 - 1;
    
    return res * mul;
};

console.log(myAtoi("42")); // 42
console.log(myAtoi("0000+123")); // 0
console.log(myAtoi("0+ 123")); // 0
console.log(myAtoi("hello world 987")); // 0
console.log(myAtoi("  -42")); // -42
