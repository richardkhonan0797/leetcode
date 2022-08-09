function countNegatives(grid: number[][]): number {
    let count = 0;
    
    for (let nums of grid) {
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] < 0) {
                count += nums.length - i;
                break;
            }
        }
    }
    
    return count;
};
