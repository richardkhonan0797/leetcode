function plusOne(digits: number[]): number[] {
    let index = digits.length - 1;
    
    digits[index] += 1;
    
    while (digits[index] == 10 ) {
        digits[index] = 0;
        index -= 1;
        if (index < 0) {
            digits.unshift(1);
        } else {
            digits[index] += 1;   
        }
    }
    
    return digits;
};
