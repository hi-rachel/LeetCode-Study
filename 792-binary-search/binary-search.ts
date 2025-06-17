/*
* 정수 배열 오름차순 정렬 nums가 주어졌을때,
* target이 존재하면 찾아 target의 index를 반환, 없으면 -1 반환
* O(log n) 시간 복잡도로 작성해라.
* 
* 문제 풀이
* 이분 탐색 -> O(log n), 매 탐색마다 탐색 범위를 절반으로 줄이기 때문
*/

function search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
};