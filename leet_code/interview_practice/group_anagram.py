from collections import defaultdict

def group_anagram(strs):
    result = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1
        result[tuple(count)]

    
    print(result.values())





print(group_anagram(["eat", "ate", "tea", "bat", "nat"]))
