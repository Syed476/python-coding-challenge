from collections import Counter, defaultdict, OrderedDict

# Counter
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'date']
word_counts = Counter(words)
print(word_counts)

# defaultdict
d = defaultdict(list)
d['fruits'].append('apple')
d['fruits'].append('banana')
print(d)

# OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)