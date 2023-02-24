from collections import *

# Counters -> give char count
name = "rahulsharma"
name_counter = Counter(name)
print(name_counter.items())
print(name_counter.keys())
print(name_counter.values())
print(name_counter.most_common(1)) # Can 1 or more depends on number of distinct chars
print(name_counter.elements()) # return itertools.chain object , conver to list
print(list(name_counter.elements()))  # note the result value will not have the same order but the chars will be group together based on the order of their appearance in the origianl input string

# nametuple -> create a class with given attributes
Person = namedtuple("Person", "name,age")
person1 = Person(name, "23")
print(person1.name, person1.age)

# OrderedDict has no use anymore as the default dict is ordered from py 3.7 >
o_dict = OrderedDict()
o_dict[1] = "The order"
o_dict[2] = "will"
o_dict[3] = "be the"
o_dict[4] = "same"
print(o_dict)

# defaultdict prevents KeyError while accessing keys not present, returns default Type value
d_dict = defaultdict(int) # can be int/float/list/dict/set -> 0/0.0/[]/{}/set()
d_dict[1] = "1"
print(d_dict[2]) # return 0 due to "int" type 

# deque -> double-ended queue | supports insertion and deletion at 0 and N at O(1)
# takes nothing or a existing list 
dq = deque([1, 2, 3]) # or just deque()
dq.append(4) # [1,2,3,4]
dq.appendleft(5) # [5,1,2,3,4]
print(dq)
dq.pop() # [5,1,2,3]
dq.popleft() # [1,2,3]
# list functions can also be used
dq.clear()
dq.extend([1, 2, 3, 4, 5])
dq.extendleft([6, 7, 8, 9, 0]) # [0, 9, 8, 7, 6, 1, 2, 3, 4, 5]
dq.rotate(1) # shifts elements to right by given number of indexes
dq.rotate(-2) # shifts elements to left by given number of indexes
print(dq)
