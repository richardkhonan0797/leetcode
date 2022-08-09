function targetIndices(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length - 1; i++) {
        for (let j = 0; j < nums.length - i - 1; j++) {
            if (nums[j] > nums[j + 1]) {
                let temp = nums[j]
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
    
    let left = 0;
    let right = nums.length - 1;
    let res = [];
    
    let index = binarySearch(nums, target);
    
    if (index === null) return res;
    
    left = index;
    right = index;
    
    while (nums[left - 1] === target) {
        left--;
    }
    
    while (nums[right + 1] === target) {
        right++;
    }
    
    for (let i = left; i <= right; i++) {
        res.push(i);
    }
    
    return res;
};

function binarySearch(nums: number[], target: number): number | null {
    let left = 0;
    let right = nums.length - 1;
    
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        
        if (nums[mid] === target) return mid;
        
        if (target > nums[mid]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return null;
}
