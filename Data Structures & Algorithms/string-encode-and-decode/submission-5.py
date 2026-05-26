class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            string = str(len(word)) + "#"
            string += word
            encoded += string
        return encoded


    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World
        words = []

        left = 0
        right = 0
        val = ""
        while left < len(s):
            if s[left] != "#":
                val += s[left]
            else:
                string = ""
                right = left+1

                for i in range(int(val)):
                    string += s[right+i]
                    left = right+i

                words.append(string)
                val = ""
            left += 1

        return words








