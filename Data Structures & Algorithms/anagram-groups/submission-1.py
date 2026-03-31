class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_word = "".join(sorted(s))
            anagram_map[sorted_word].append(s)

        return list(anagram_map.values())
            



        



                


        