from collections import Counter, defaultdict

def get_minimum_window(original: str, check: str) -> str:
    original_length, check_length = len(original), len(check)
    if original_length < check_length:
        return ""

    def is_smaller(w1, w2):  # is w1 smaller than w2
        if w1[1] - w1[0] == w2[1] - w2[0]:
            for i in range(w1[1] - w1[0]):
                if original[w1[0] + i] != original[w2[0] + i]:
                    return original[w1[0] + i] < original[w2[0] + i]
            return False
        else:
            return w1[1] - w1[0] < w2[1] - w2[0]

    check_counter = Counter(check)
    required = len(check_counter.keys())
    window_counter: defaultdict[str, int] = defaultdict(int)
    # initialize "empty" window of size (m+1)
    window = (-original_length - 1, 0)
    satisfied = 0
    l = 0

    for r in range(original_length):
        # keep track only characters that appear in check
        if original[r] in check_counter:
            window_counter[original[r]] += 1
            if window_counter[original[r]] == check_counter[original[r]]:
                satisfied += 1
        while satisfied == required:  # valid window
            if is_smaller((l, r + 1), window):  # new window is smaller than window
                window = (l, r + 1)
            if original[l] in check_counter:  # delete only characters from check
                window_counter[original[l]] -= 1
                # removing original[l] makes window dissatisfied
                if window_counter[original[l]] < check_counter[original[l]]:
                    satisfied -= 1
            l += 1

    return original[window[0] : window[1]]

if __name__ == "__main__":
    original = input()
    check = input()
    res = get_minimum_window(original, check)
    print(res)