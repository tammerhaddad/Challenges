# given a list of strings, 
# returns a list of lists of the groups of strings
# that are anagrams of each other

class mySolution(object):
    def groupAnagrams(self, strs):
        # loops through the strings
        # for each string, adds a list of all of its anagrams
        # but its in a set so the duplicates are removed
        return {tuple(s for s in strs if sorted(word) == sorted(s)) for word in strs}

class Solution(object):
    def groupAnagrams(self, strs):
        # makes a dict of the anagrams
        anagrams = {}
        for word in strs:
            # sorts each word the same way i do
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                # if the sorted word is a duplicate,
                # add the word to the dict IN THE ARRAY OF WORDS
                # connected to the sorted word
                anagrams[sorted_word].append(word)
            else:
                # otherwise, start a new list of words
                anagrams[sorted_word] = [word]
        # return the list of lists held in the values
        return list(anagrams.values())