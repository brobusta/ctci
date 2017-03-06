# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional datastructure?

# O(N^2)
def solution1(A):
    N = len(A)
    for i in range(0, N):
        for j in range(i+1, N):
            if A[i] == A[j]:
                return False
    return True

if __name__ == '__main__':
    assert solution1("abcDEFghi1234") == True
    assert solution1("") == True
    assert solution1("qwerty09876qBGTRFVe") == False
