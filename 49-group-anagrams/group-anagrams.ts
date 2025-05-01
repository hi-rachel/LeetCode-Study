function groupAnagrams(strs: string[]): string[][] {
    const anagramMap = strs.reduce((map, word) => {
        const key = word.split('').sort().join('');
        if (!map.has(key)) {
            map.set(key, [])
        }
        map.get(key).push(word);
        return map;
    }, new Map<string, string[]>());

    return Array.from(anagramMap.values());
}