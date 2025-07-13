#1st sum


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        subarr=set()

        while right<len(s):
            if s[right] not in subarr:
                subarr.add(s[right])
                longest=max(longest,right-left+1)
                right+=1

            else:

                subarr.remove(s[left])
                left+=1
        return longest if longest else 0

sol=Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))



#2nd sum
class Solution2:
    def minSubArrayLen(self, target: int, nums) :
        left=0
        right=0
        minlenarr=[]
        subsum=0

        while right < len(nums):
            subsum=subsum+nums[right]
            if subsum < target:
                right+=1

            else:
                while subsum>=target:
                    minlenarr.append(right-left+1)
                    subsum=subsum-nums[left]
                    left=left+1
                right += 1
                

        return min(minlenarr) if minlenarr else 0


target = 7
nums = [2,3,1,2,4,3]
fir=Solution2()
print(fir.minSubArrayLen(target,nums))          
            
        