from collections.abc import Iterable, Iterator

a = [1, 2]
iter_rator = iter(a)

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(iter_rator, Iterator))
