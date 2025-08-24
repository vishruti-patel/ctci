def longest_repeating_char(s, k):
    count = {}
    l = 0
    result = 0


    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] = count[s[l]] -1
            l = l + 1

        result = max(result, r - l + 1)
    return result
        
print(longest_repeating_char('ABAAAB', 2))

