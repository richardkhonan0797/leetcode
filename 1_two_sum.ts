function twoSum(nums: number[], target: number): number[] {
    let dict = {};
    dict[nums[0]] = 0;
    let sub = 0;
    
    for (let i = 1; i < nums.length; i++) {
        sub = target - nums[i];
        
        if (sub in dict) {
            return [dict[sub], i];
        } else {
            dict[nums[i]] = i;
        }
    }
}
