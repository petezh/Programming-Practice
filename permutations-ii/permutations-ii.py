class Solution(object):
    def permuteUnique(self, nums):
        ans = [[]]
        # for each number
        for n in nums:
            new_ans = []
            # for each existing ans
            for l in ans:
                # iterate through the answer
                for i in xrange(len(l)+1):
                    # insert n at each index
                    new_ans.append(l[:i]+[n]+l[i:])
                    # if duplicate, dont add
                    if i<len(l) and l[i]==n: break
            # update ans
            ans = new_ans
        return ans