class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True) # Sort in reverse order
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s) # Append time taken to reach destination to stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # If the time taken by the next car is less then they will collide                               so can pop that car and consider it one fleet
        return len(stack)