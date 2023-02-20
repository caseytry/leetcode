# My solution for  https://leetcode.com/problems/two-sum/
# first two lines given by leetcode


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #create a number, iterate from 0 to the length of the array.
        #because using range to do this, this will not go above the end of array
        for n in range(0,len(nums)):
            #same as above, but for the second digit. starting at n+1,
            #as each number only used once.
            for i in range((n+1),len(nums)):
                #if the values for the numbers at array position n and i = the target
                if nums[n] + nums[i] == target:
                    #return n & i, as we want the INDEXES of those numbers
                    return(n, i)
                #if numbers dont work, increase i first to see if different number in array
                #can add up
                else:
                    i += 1
            #increase n by one, retry loop with the remaining i values.
            else:
                n+=1