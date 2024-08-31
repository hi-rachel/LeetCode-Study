class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        num = 0
        magazine_book = list(magazine)
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine_book:
                num += 1
                magazine_book.remove(ransomNote[i])
                    
        return num == len(ransomNote)
        