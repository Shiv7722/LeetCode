"""
Anagram Gouping

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Complexity:
    Time: O(N * L log L) where N=len(strs) and L is the average word length
    (sorting each word dominates).
    Space: O(N * L) for the output and keys."""

strs = ["eat","tea","tan","ate","nat","bat"]    

def groupAnagrams(strs):
        # Dictionary to collect groups: key (sorted letters) -> list of words
        groups={}

        # Process each word and place it into the appropriate anagram bucket
        for word in strs:
            # Create the canonical key by sorting the letters of the word
            x = "".join(sorted(word))

            # If the key already exists, append the original word to that list
            if x in groups:
                groups[x].append(word)
            else:
                # Otherwise, start a new list for this key
                groups[x]=[word]

        # Return only the grouped anagram lists (values of the dictionary)
        return list(groups.values())

print(groupAnagrams(strs))