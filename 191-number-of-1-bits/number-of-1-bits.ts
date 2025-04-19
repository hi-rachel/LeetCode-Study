function hammingWeight(n: number): number {
    return n.toString(2).split('').filter(bit => bit === '1').length;
};