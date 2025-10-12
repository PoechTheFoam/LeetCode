[Problem Link Here](https://leetcode.com/problems/longest-palindromic-substring)

**🚶‍➡️Approach🚶**:
- Approached the problem with 2 for loop cases for even-odd palindrome lengths
**⚠️Problems Encountered⚠️**:
- Had trouble understanding the length formula used (r-l-1)
- Initially used the string's length as an indicator for code direction (if s was even, use the code path for even-length palindromes)

**💡Lesson💡**:
- Odd-length palindromes can be in even-length strings and vice versa.
- r-l-1 is because the indices "overflowed" when while loop fails. (therefore, both r and l is larger than what the actual output is by one, r-l already includes -1 so we just do another -1)
- An alternative would be to update the maxLen inside while loop -> Uses r-l+1 instead (since indices starts at 0, when doing r-l, a "-1" is already included, hence to get actual length we do "+1"")

**📝Notes📝**:
- None
