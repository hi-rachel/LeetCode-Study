function longestConsecutive(nums: number[]): number {
    let numSet = new Set(nums);
    let longest = 0;

    while (numSet.size !== 0) {
        let num = numSet.values().next().value;
        numSet.delete(num);
        let [left, right] = [1, 1];

        while (numSet.has(num - left)) {
            numSet.delete(num - left);
            left += 1;
        }

        while (numSet.has(num + right)) {
            numSet.delete(num + right);
            right += 1;
        }
        longest = Math.max(left + right - 1, longest);
    }
    return longest;
};