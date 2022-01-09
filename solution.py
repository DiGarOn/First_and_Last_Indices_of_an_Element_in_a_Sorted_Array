class Solution:
    def bin_search_left(self, arr, target):
        left = -1
        right = len(arr) - 1
        med = (left+right)//2
        while(left < right -1):
            if(arr[med] >= target):
                right = med
            else:
                left = med
            med = (left+right)//2
        if(arr[right] == target):
            return right
        else:
            return -1

    def bin_search_right(self, arr, target):
        left = 0
        right = len(arr)
        med = (left+right)//2
        while(left < right -1):
            if(arr[med] <= target):
                left = med
            else:
                right = med
            med = (left+right)//2
        if(arr[left] == target):
            return left
        else:
            return -1

    def check_ans(self, mas):
        if(mas[0] == -1):
            return -1
        else:
            return mas

    def getRange(self, arr, target):
        right = Solution().bin_search_right( arr, target)
        left = Solution().bin_search_left( arr, target)
        return Solution().check_ans([left, right])

if __name__ == '__main__':
    # Test program 
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]
    x = 5
    print(Solution().getRange(arr, x))
    # -1