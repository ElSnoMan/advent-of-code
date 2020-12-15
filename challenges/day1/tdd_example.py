""" 1. Start with a Test so we can visualize our end goal. Now we know what to build and we have a test to tell us if we made it. """
GOAL     = 2020
ENTRIES  = [1721, 979, 366, 299, 675, 1456]
EXPECTED = 514579

a1, a2 = find_addends(GOAL, ENTRIES)
answer = a1 * a2
assert EXPECTED == answer, f'Expected: {EXPECTED}, but got {answer} instead'

""" 2. Explore the data a bit """
import pandas as pd

data = pd.read_table('expense_report.txt', header=None)

# Check the head
data.head()

# Then check the tail.
# Looks like there are 200 entries and they're not ordered
data.tail()

""" 3. Structure the data a bit better """
df = data.sort_values(by=data.columns[0])
count = len(df.values)
print('Number of entries:', count)
# Number of entries: 200

# check the head and tail
df.head()
df.tail()

""" 4. Define the find_addends() function. We know what we want it to look like, so now we just need to implement it.

* Run our Test. Did it pass? If yes, your implementation works! If not, what feedback did it provide?
* What pros and cons do you see with our current implementation?
"""
def find_addends(goal, entries):
    for entry in entries:
        diff = goal - entry
        if diff in entries:
            return entry, diff
            
""" 5. What if we timed it?

Quality is more than just code correctness or functionality. There are a lot of non-functional requirements or NFRs:

* A11y
* Performance
* Security
* Reliability
* Availability
* etc
"""
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        stop_time = time.time()
        elapsed = str(stop_time - start_time)
        print(f'{func.__name__} took {elapsed[:5]} seconds')
        return output
    return wrapper

# Output: find_addends took 2.145 seconds

""" 6. We can do better than that. Especially if we had to deal with a LOT of data... What about a binary search? """
@timer
def find_addends(goal, entries):
    count = len(entries)
    half = round(count / 2)

    for i, entry in enumerate(entries[:half]):
        diff = goal - entry
        if diff in entries[i + 1:]:
            return entry, diff
       
""" 7. Run the test again. Does it still pass after our optimization? How long did it take? """
# Output: find_addends took 1.120 seconds

""" 8. Finally, let's put in our production data to see if we get the right answer """
a1, a2 = find_addends(GOAL, df.values)
answer = a1 * a2
print(answer)

# Expected output: [987339]
