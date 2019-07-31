def eraseOverlapIntervals(intervals: list) -> int:
    if not intervals:
        return 0
    intervals.sort(key = lambda x: x[0])
    cur_end = intervals[0][1]
    ans = 0
    for start, end in intervals[1:]:
        if start < cur_end:
            cur_end = min(cur_end, end)
            ans += 1
        else:
            cur_end = end
    return ans