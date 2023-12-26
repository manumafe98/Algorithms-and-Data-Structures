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
