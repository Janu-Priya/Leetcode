class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree_max = [0] * (4 * self.n)
        self.tree_pref = [0] * (4 * self.n)
        self.tree_suff = [0] * (4 * self.n)
        self.tree_left = [''] * (4 * self.n)
        self.tree_right = [''] * (4 * self.n)
        self.build(s, 0, 0, self.n - 1)

    def merge(self, node, left_node, right_node, l_len, r_len):
        self.tree_left[node] = self.tree_left[left_node]
        self.tree_right[node] = self.tree_right[right_node]
        
        self.tree_max[node] = max(self.tree_max[left_node], self.tree_max[right_node])
        self.tree_pref[node] = self.tree_pref[left_node]
        self.tree_suff[node] = self.tree_suff[right_node]

        if self.tree_right[left_node] == self.tree_left[right_node]:
            self.tree_max[node] = max(
                self.tree_max[node], 
                self.tree_suff[left_node] + self.tree_pref[right_node]
            )
            if self.tree_pref[left_node] == l_len:
                self.tree_pref[node] = l_len + self.tree_pref[right_node]
            if self.tree_suff[right_node] == r_len:
                self.tree_suff[node] = r_len + self.tree_suff[left_node]

    def build(self, s, node, l, r):
        if l == r:
            self.tree_max[node] = 1
            self.tree_pref[node] = 1
            self.tree_suff[node] = 1
            self.tree_left[node] = s[l]
            self.tree_right[node] = s[l]
            return
        
        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2
        self.build(s, left_node, l, mid)
        self.build(s, right_node, mid + 1, r)
        self.merge(node, left_node, right_node, mid - l + 1, r - mid)

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.tree_left[node] = ch
            self.tree_right[node] = ch
            return
        
        mid = (l + r) // 2
        left_node, right_node = 2 * node + 1, 2 * node + 2
        if idx <= mid:
            self.update(left_node, l, mid, idx, ch)
        else:
            self.update(right_node, mid + 1, r, idx, ch)
            
        self.merge(node, left_node, right_node, mid - l + 1, r - mid)


class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        st = SegmentTree(s)
        ans = []
        n = len(s)
        
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(0, 0, n - 1, idx, ch)
            ans.append(st.tree_max[0])
            
        return ans