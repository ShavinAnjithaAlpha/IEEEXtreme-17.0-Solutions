from itertools import *
import operator

# count() returns an iterator that produces consecutive integers, indefinitely.
for i in count(10, 2):
    if i > 20:
        break
    else:
        print(i, end=' ')


print('\n')

# cycle() returns an iterator that repeats the contents of the arguments it is given indefinitely.
for i in cycle(('On', 'Off')):
    if i == 'Off':
        break
    else:
        print(i, end=' ')
print('\n')

# product takes several lists as arguments and produces a "cartesian product",
# combining the elements of the input lists.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print(list(product(list1, list2)))  # 3 * 3 = 9 elements
print(list(product(list2, list1, repeat=2)))
# repeat argument specifies the number of repetitions.
print(list(product(list1, repeat=3)))
print('\n')

# permutations() produces a sequence of tuples that rearranges the elements of the input iterable.
print("Permuttaions:")
print(list(permutations(list1)))
print(list(permutations(list2, 2)))
print('\n')

# combinations() returns successive r-length combinations of elements in the iterable.
print("Combinations:")
print("combination without replacement: ", list(combinations(list1, 2)))
print("combination with replacement: ", list(
    combinations_with_replacement(list1, 2)))
print('\n')

# accumulate() returns a sequence of partial results.
print("Accumulate:")
print("accumulate with default: ", list(accumulate(list1)))
print("accumulate with custom function: ",
      list(accumulate(list1, operator.mul)))
print('\n')

# chain takes several iterables as arguments and returns a single iterable that produces all of the values in the input iterables.
print("Chain:")
print(list(chain(list1, list2)))

print("list of list chain: ", list(chain.from_iterable([list1, list2])))
print('\n')

# compress() offers another way to filter the contents of an iterable.
print("Compress:")
print(list(compress(list1, [1, 0, 1])))
