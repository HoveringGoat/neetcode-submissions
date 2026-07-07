import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = json.dumps(strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = json.loads(s)
        return decoded
