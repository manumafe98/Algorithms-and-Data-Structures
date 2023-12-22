"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order 
by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result_array = []
        # We loop over the inervals in the array
        for i in range(len(intervals)):
          # We first check the edge cases
          # if our new interval is smaller than a interval in the array
          if newInterval[1] < intervals[i][0]:
            result_array.append(newInterval)
            return result_array + intervals[i:]
          # Then if they do not overlap and the first part of new interval is greater add the interval
          elif newInterval[0] > intervals[i][1]:
            result_array.append(intervals[i])
          # And finally update the value of the new interval comparing with the interval taking the min and max values  
          else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # if the loop did not break that means that the interval was not added to the result so we add it here
        result_array.append(newInterval)
        
        return result_array
