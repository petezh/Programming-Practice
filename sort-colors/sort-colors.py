class Solution(object):
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        # red and white to the right, blue to the left
        while white <= blue:
            # push white to end of red, swapping
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            # push white to end of white
            elif nums[white] == 1:
                white += 1
            # swap white and blues
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1