def longest_substring_without_repeating_characters(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = current_length = longest_substring_length = 0
    for right in range(len(s)):
        current_length += 1
        while s[right] in s[left:right]:
            left += 1
            current_length -= 1
        longest_substring_length = max(longest_substring_length, current_length)
    return longest_substring_length


if __name__ == "__main__":
    s = input()
    res = longest_substring_without_repeating_characters(s)
    print(res)