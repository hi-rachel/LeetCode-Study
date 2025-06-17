/**
 * 정수 배열 nums에서 2개의 요소를 더해 target이 되는 index 배열을 반환해라. 
 *
 * TC: O(N**2)
 * SC: O(1)
 */

function twoSum(nums: number[], target: number): number[] {
  const answer: number[] = [];
  for (let i = 0; i < nums.length; i++) {
    let cur = target - nums[i];
    let restIdx = nums.findIndex((val, idx) => val === cur && idx !== i);
    if (restIdx !== -1) {
        answer.push(i)
        answer.push(restIdx)
        break
    }
  }
  return answer;
};