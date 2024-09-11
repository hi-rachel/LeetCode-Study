from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams_dict[sorted_word].append(word)

        return list(anagrams_dict.values())