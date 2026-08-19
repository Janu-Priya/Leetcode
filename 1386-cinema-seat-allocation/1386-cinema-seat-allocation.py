class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        occupied = defaultdict(set)
        for r, c in reservedSeats:
            if 2 <= c <= 9:
                occupied[r].add(c)
        ans = 2 * n
        
        for r, seats in occupied.items():
            left = not any(c in seats for c in (2, 3, 4, 5))
            right = not any(c in seats for c in (6, 7, 8, 9))
            middle = not any(c in seats for c in (4, 5, 6, 7))
            
            if left and right:
                continue
            elif left or right or middle:
                ans -= 1
            else:
                ans -= 2
                
        return ans
        