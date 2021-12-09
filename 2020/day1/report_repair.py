# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Day 1 Challenge
#
# Find the two entries that sum to `2020` and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
# ```
# 1721
# 979
# 366
# 299
# 675
# 1456
# ```
#
# ## Part 1
# ---
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer to submit is `514579`.
#
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?
#
# ## Part 2
# ---
# Use the same list to find 3 addends that sum up to 2020, and then submit their product

# %%
""" Load the data """
import pandas as pd

data = pd.read_table('expense_report.txt')


# %%
""" Sort the data and explore it a bit """
df = data.sort_values(by=data.columns[0])
count = len(df.values)
print('Number of entries:', count)


# %%
df.head()


# %%
df.tail()


# %%
""" Find the two addends that make 2020 """
GOAL = 2020
HALF = round(count / 2)

for i, value in enumerate(df.values[:HALF]):
    diff = GOAL - value
    if diff in df.values[i + 1:]:
        addend_1 = value
        addend_2 = diff

print('Addend  -> ', addend_1)
print('Addend  -> ', addend_2)

# Expected
# [829]
# [1191]


# %%
""" Get the product of the addends which is the answer to the challenge """
answer = addend_1 * addend_2
print(answer)

# Expected
# [987339]


# %%
""" Find the three addends that make 2020 """
GOAL = 2020
HALF = round(count / 2)

addend_1 = 0
addend_2 = 0
addend_3 = 0

for low in df.values[:HALF]:
    for i in range(len(df.values)):
        high = df.values[-1-i]
        if high + low > GOAL:
            continue  # to save lookup
        diff = GOAL - high - low
        if diff in df.values:
            addend_1 = low
            addend_2 = high
            addend_3 = diff

print('Addend  -> ', addend_1)
print('Addend  -> ', addend_2)
print('Addend  -> ', addend_3)

# Expected
# [418]
# [657]
# [945]


# %%
""" Get the product of the addends which is the answer to the challenge """
answer = addend_1 * addend_2 * addend_3
print(answer)

# Expected
# [259521570]


# %%
