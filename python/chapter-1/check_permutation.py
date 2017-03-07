# Given two strings, write a method to decide if one is a permutation of the other.

# O(NlogN), spaces are counted.
def solution1(A, B):
    lenA = len(A)
    lenB = len(B)
    if lenA != lenB:
        return False
    return sorted(A) == sorted(B)

if __name__ == '__main__':
    assert solution1("abcdef   ", " acbe d f") == True
