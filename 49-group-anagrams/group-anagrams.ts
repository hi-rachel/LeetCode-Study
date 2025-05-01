function groupAnagrams(strs: string[]): string[][] {
    const anagramMap = {};

    strs.forEach((word) => {
        const key = word.split('').sort().join('');
        (anagramMap[key] ||= []).push(word);
    });

    return Object.values(anagramMap);
}