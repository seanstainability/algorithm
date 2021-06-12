import re

def isPalindrome(s: str) -> bool:
    # 정규표현식 + 슬라이싱 조합
    s = s.lower()
    print(s)
    s = re.sub('[^a-z0-9]', '', s)
    print(s)
    return s == s[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))