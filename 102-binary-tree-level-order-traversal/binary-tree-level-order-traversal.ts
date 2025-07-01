/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function levelOrder(root: TreeNode | null): number[][] {
    if (!root) return [];

    const queue: TreeNode[] = [root];
    const output: number[][] = [];

    while (queue.length > 0) {
        const level: number[] = [];
        for (let node of queue) {
            level.push(node.val)
        }
        output.push(level)
        const size = queue.length;

        for (let i = 0; i < size; i++) {
            const node = queue.shift();
            if (node.left) {
                queue.push(node.left)
            }
            if (node.right) {
                queue.push(node.right)
            }
        }
    }
    return output
};
