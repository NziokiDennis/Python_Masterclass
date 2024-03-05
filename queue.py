# Example of queue implementation using deque
from collections import deque
queue = deque()
queue.append(1)  # Enqueue operation
queue.append(2)
print(queue.popleft())  # Output: 1 (Dequeue operation)
