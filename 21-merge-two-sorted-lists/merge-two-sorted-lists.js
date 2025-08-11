/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    const dummy = new ListNode(); // 결과 리스트의 시작을 고정할 가짜 헤드
    let tail = dummy;             // 결과의 꼬리를 가리키는 포인터

    // 두 리스트가 모두 남아있는 동안, 더 작은 노드를 tail 뒤에 붙인다
    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            tail.next = list1
            list1 = list1.next
        } else {
            tail.next = list2
            list2 = list2.next
        }
        tail = tail.next
    }
    tail.next = (list1 !== null) ? list1 : list2;

    return dummy.next
};