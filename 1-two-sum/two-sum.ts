/**
 * 정수 배열 nums에서 2개의 요소를 더해 target이 되는 index 배열을 반환해라. 
 *
 * TC: O(N)
 * SC: O(N)
 */

function twoSum(nums: number[], target: number): number[] {
  const map = new Map<number, number>(); // num -> idx

  for (let i = 0; i < nums.length; i++) {
    const rest = target - nums[i];
    if (map.has(rest)) {
        return [map.get(rest), i];
    }
    map.set(nums[i], i)
  }
  return [];
};