/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permute = function(nums) {
    const permutations = [];
    
    const dfs = (picked, unpicked) => {
        if (!unpicked.length) return permutations.push(picked);

        unpicked.forEach((num, i) => 
            dfs(
                [...picked, num],
                [...unpicked.slice(0, i), ...unpicked.slice(i + 1)],
            ),
        );
    };

    dfs([], nums);

    return permutations;
};