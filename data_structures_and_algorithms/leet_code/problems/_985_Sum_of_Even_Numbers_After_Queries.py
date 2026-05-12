#You are given an integer array nums and an array queries where queries[i] = [vali, indexi].
#For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the even values of nums.
#Return an integer array answer where answer[i] is the answer to the ith query.



def sumEvenAfterQueries(nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        results = []
        result = sum([n for n in nums if not n%2])
        for query in queries:
            
            previous = nums[query[-1]]
            nums[query[-1]] = previous + query[0]
            current = nums[query[-1]]
            
            if current%2==0:
                if previous%2==1:
                    result += current
                else:
                    result += (current-previous)
            else:
                if previous%2==0:
                    result = result - previous
         
            results.append(result) 
            
        return results                
            
                
          
# Input:
nums = [1,2,3,4] 
queries = [[1,0],[-3,1],[-4,0],[2,3]]

# Output: [8,6,2,4]
print(sumEvenAfterQueries(nums, queries))
