class Solution:
    def bin_search(self, arr, target):
        left = 0
        right = len(arr)
        med = (left+right)//2
        while(arr[med] != target and left < right -1):
            if(arr[med] > target):
                right = med
            else:
                left = med
            med = (left+right)//2
        if(arr[med] == target):
            return med
        else:
            return -1

    def check_ans(self, mas):
        if(mas[0] == -1):
            return -1
        else:
            return mas

    def getRange(self, arr, target):
        pos = Solution().bin_search( arr, target)
        i = pos
        if(pos != -1):
            while(arr[i] == target and i > 0):
                i -= 1
            if(arr[i] != target):
                i += 1 
            while(arr[pos] == target and pos < len(arr)-1):
                pos += 1
            if(arr[pos] != target):
                pos -= 1
        return Solution().check_ans([i, pos])
if __name__ == '__main__':
    # Test program 
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]
    x = 5
    print(Solution().getRange(arr, x))
    # -1