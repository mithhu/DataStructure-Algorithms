def groupAnagrams(words):
    sortedWords = ["".join(sorted(w)) for w in words]
    return sortedWords


print(groupAnagrams(["yo", "act", "flop", "tac", "cat", 'oy', "olfp"]))
