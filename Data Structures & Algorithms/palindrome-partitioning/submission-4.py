class Solution:
    def partition(self, s: str) -> List[List[str]]:


        # splits the word at length 1, then 2, up to n and tries to make palindromes
        def attemptPSplit(word: str) -> List[List[str]]:
            pals = []
            if word in cached:
                #print(f"cached result! - {word}: {cached[word]}")
                return cached[word]
            if isPalindrome(word):
                pals.append([word])
            for splitIndex in range(1, len(word)):
                pre = word[:splitIndex]
                post = word[splitIndex:]
                # print(f"word: {word}")
                # print(f"{splitIndex}: {pre}-{post}")

                prePals = attemptPSplit(pre)
                postPals = attemptPSplit(post)

                # print(f"word: {pre}-{post}")
                # print(f"prePals: {pre} - {prePals}")
                # print(f"prePals: {post} - {postPals}")

                for i in prePals:
                    #print(f"prepal: {i}")
                    for j in postPals:
                        #print(f"postpal: {j}")
                        temp = i[:]
                        temp.extend(j)
                        #if temp not in pals:
                        pals.append(temp)
                        #print(f"added: {temp}")

            newPals = []
            for i in pals:
                if i not in newPals:
                    newPals.append(i)
            cached[word] = newPals
            return newPals
            #return pals
                

        def isPalindrome(word: str) -> bool:
            reverse = word[::-1]
            return reverse == word

        cached = {}
        palindromes: List[List[str]] = attemptPSplit(s)

        #print(f"pals: {palindromes}")
        return palindromes