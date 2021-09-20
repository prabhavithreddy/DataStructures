from StackUsingLinkedList import Stack

prices = [10, 4, 5, 90, 120, 80]
spans = []
s = Stack()
i = 0
while i < len(prices):
    c = prices[i]
    if s.is_empty() or c < s.peek()[0]:
        s.push((c, 1))
        spans.append(1)
    else:
        span = 1
        while not s.is_empty() and c > s.peek()[0]:
            span+=s.pop()[1]
        s.push((c, span))
        spans.append(span)
    i+=1
print(spans)