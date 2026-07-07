class Solution:
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        solutions: List[List[str]] = []
        pals = {}

        # simple palindrome check
        # cache results for faster runtime
        def isPal(word: str) -> bool:
            if word not in pals:
                p = word == word[::-1]
                pals[word] = p
            return pals[word]
         
        # build up first "word" to try and form palindromes.
        # if we find one run the recursive function passing in the current list of palindrome words used
        # update the index so we know the remaining substring we can process
        # if we hit the end of the sequence append to solution list
        def recurse(index:int, palWords:List[str]):
            
            # first check if we're at the end
            if index == length:
                # do we need to check if its unique? (nope)
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
                # if its not a palindrome its not part of a solution so we continue growing the word

        # initial entry point
        recurse(0, [])
        return solutions