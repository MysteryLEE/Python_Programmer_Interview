class Solution:
    def minMeetingRooms(self, intervals):
        if intervals is None or len(intervals) == 0:
            return 0

        tmp = []

        # mark starting points and ending points
        for inter in intervals:
            tmp.append((inter[0], True))
            tmp.append((inter[1], False))

        # sort
        tmp = sorted(tmp, key=lambda v: (v[0], v[1]))

        n = 0
        max_num = 0
        for arr in tmp:
            # meet starting points +1
            if arr[1]:
                n += 1
            # meet ending points -1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num

solve=Solution()
print(solve.minMeetingRooms([[0,30],[5,10],[15,20]]))
print(solve.minMeetingRooms([[7,10],[2,4]]))
