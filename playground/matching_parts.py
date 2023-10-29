import difflib

string1 = "abcdefg"
string2 = "abxyzefg"

matcher = difflib.SequenceMatcher(None, string1, string2)
matching_blocks = matcher.get_matching_blocks()

print(matching_blocks)
for item in matching_blocks:
    print(string1[item.a:item.a + item.size])

# Find the longest matching block
longest_block = max(matching_blocks, key=lambda block: block.size)

common_part = string1[longest_block.a:longest_block.a + longest_block.size]
print(common_part)  # Output: "efg"


def findCommons(word, q):
    # first find from the start
    parts = []
    s = ""
    for i in word:
        s += i
        if s in q and len(s) >= 3:
            parts.append(s)

    for i in range(1, len(word)):
        if word[i:] in q and len(word[i:]) >= 3:
            parts.append(word[i:])

    return parts


print("commons: ")
print(findCommons("spoooon", "spoon"))
