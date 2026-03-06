class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        s, t = s.lower(), t.lower() 
        from collections import Counter, defaultdict

        def is_smaller(w1, w2):  # is w1 smaller than w2
            return w1[1] - w1[0] < w2[1] - w2[0]

        t_counter = Counter(t)
        required_count = len(t_counter.keys()) 
        window_counter: defaultdict[str, int] = defaultdict(int)
        l = r = 0
        satisfied_count = 0
        min_window_length, current_length = (-len(s) - 1, 0), (0, 0)
        for r in range(len(s)):
            window_counter[s[r]] += 1
            if window_counter[s[r]] == t_counter[s[r]]:
                satisfied_count += 1
            while required_count == satisfied_count:
                current_length = (l, r + 1)
                if is_smaller(current_length, min_window_length):
                    min_window_length = current_length
                if s[l] in t_counter:  # delete only characters from t
                    window_counter[s[l]] -= 1
                # removing original[l] makes window dissatisfied
                if window_counter[s[l]] < t_counter[s[l]]:
                    satisfied_count -= 1
                l += 1
        return s[min_window_length[0] : min_window_length[1]]


