class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # build up first "word" to try and form palindromes.
        # if we find one run the recursive function passing in the current list of palindrome words used
        
        length = len(s)
        solutions: List[List[str]] = []

        # simple palindrome check
        def isPal(word: str) -> bool:
            return word == word[::-1]
         
        # recursive function. we need: the index to which we've processed and the current formed words
        # doesn't return anything. if we find a new palindrome word in the sequence we recursively call it
        # otherwise we build up the current "word"
        # if we hit the end of the sequence append to solution list
        def recurse(index:int, palWords:List[str]):
            
            # first check if we're at the end
            if index == length:
                # do we need to check if its unique?
                solutions.append(palWords)
            
            # form a word and check if its a palindrome
            currentWord = ""
            for i in range(index, length):
                currentWord += s[i]

                if isPal(currentWord):
                    # dup the list and add current word
                    words = palWords[:]
                    words.append(currentWord)
                    recurse(i+1, words)

        # initial entry point
        recurse(0, [])
        return solutions

