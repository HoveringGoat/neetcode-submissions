class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return None
        s = ""
        for i in strs:
            s+=i
            s+="%&!"
        return s[:-3]

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        elif s == None:
            return []
        
        return s.split("%&!")
