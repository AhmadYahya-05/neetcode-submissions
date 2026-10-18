class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if not temperatures:
            return []

        stack = []
        results = [0] * len(temperatures)
        
        for index,temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                popped_index,popped_temp = stack.pop()
                results[popped_index] = (index - popped_index)

            stack.append((index,temp))

        return results

        