from typing import List

def isPalindrome(head) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    print(q)

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True

print(isPalindrome([1,2,2,1]))