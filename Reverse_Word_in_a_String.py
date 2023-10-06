class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.findall(r'\S+', s)
        rev_words=words[::-1]
        
        return (' '.join(rev_words))
