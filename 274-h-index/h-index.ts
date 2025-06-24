function hIndex(citations: number[]): number {
    citations.sort((a, b) => b - a)
    let cnt = 0

    for (let i = 0; i < citations.length; i++) {
        if (citations[i] >= i + 1) cnt++
    }

    return cnt
};