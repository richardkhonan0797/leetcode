function intersect(nums1: number[], nums2: number[]): number[] {
    let dict = {};
    let res = [];
    
    for (let num of nums1) {
        if (num in dict) {
            dict[num] += 1;
        } else {
            dict[num] = 1;
        }
    }
    
    for (let num of nums2) {
        if (num in dict) {
            if (dict[num] > 0) {
                res.push(num);
                dict[num] -= 1;
            }
        }
    }
    
    return res;
};
