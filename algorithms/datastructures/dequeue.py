# Deque
import collections
DoubleEnded = collections.deque(['Mon','Tue','Wed'])
DoubleEnded.append('Thu')
DoubleEnded.appendleft('Sun')
print(DoubleEnded)
DoubleEnded.pop()
DoubleEnded.popleft()
print(DoubleEnded)