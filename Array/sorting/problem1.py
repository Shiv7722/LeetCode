"""Group Anagrams

Problem: Given a list of strings `strs`, group the anagrams together.
Anagrams are words made of the same letters in a different order.
Return a list of lists, where each sublist contains words that are anagrams of
each other.

Example:
    Input: ["eat","tea","tan","ate","nat","bat"]
    Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""

from typing import List, Dict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group a list of strings into anagram groups.

    Approach:
    - Use a dictionary (`groups`) mapping a normalized key -> list of words.
    - The normalization is: sort the characters of the word and join them.
      All anagrams produce the same sorted string (the key).
    - Append each word to the list for its key.

    Time complexity: O(N * L log L) where N is number of words and L is average
    length of a word (sorting each word costs L log L).
    Space complexity: O(N * L) to store the grouped words and keys.
    """

    groups: Dict[str, List[str]] = {}

    # Iterate through each word and group by the sorted-letter key
    for word in strs:
        # Normalize the word by sorting its characters
        key = "".join(sorted(word))

        # Add the word to the correct anagram bucket
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    # We only need the lists of grouped anagrams as the final result
    return list(groups.values())


if __name__ == "__main__":
    # Example usage for study / quick manual testing
    sample = ["eat", "tea", "tan", "ate", "nat", "bat"]

    # Call the function and print grouped anagrams
    result = group_anagrams(sample)
    print("Input:", sample)
    print("Grouped anagrams:", result)