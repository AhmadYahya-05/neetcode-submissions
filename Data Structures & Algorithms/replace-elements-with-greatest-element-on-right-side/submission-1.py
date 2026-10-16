class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        curr_max = arr[-1]
    
        for i in range(len(arr)-1,-1,-1):
            temp = curr_max
            if arr[i] > curr_max:
                curr_max = arr[i]
            arr[i] = temp
            
        arr[-1] = -1
        return arr    