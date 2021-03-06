import numpy as np
import itertools as it

# Problem 6.1.1
def generate_baskets(n=100):
    all_buckets = []
    for bucket_i in range(1, n + 1):
        curr_bucket = []
        for item_i in range(1, bucket_i + 1):
            if bucket_i % item_i == 0:
                curr_bucket.append(item_i)
        all_buckets.append(curr_bucket)
    return all_buckets

def generate_alt_baskets(n=100):
    all_buckets = []
    for bucket_i in range(1, n + 1):
        curr_bucket = []
        for item_i in range(bucket_i, n + 1):
            if item_i % bucket_i == 0:
                curr_bucket.append(item_i)
        all_buckets.append(curr_bucket)
    return all_buckets

def generate_baskets_matrix(n=100):
    # Makes an n x n matrix and uses 1 to represent in the bucket
    # Rows are buckets, and columns are items
    baskets_matrix = np.zeros((n,n))
    for bucket_i in range(1, n + 1):
        for item_i in range(1, bucket_i + 1):
            if bucket_i % item_i == 0:
                baskets_matrix[bucket_i - 1, item_i - 1] = 1
    return baskets_matrix

def generate_alt_baskets_matrix(n=100):
    # Makes an n x n matrix and uses 1 to represent in the bucket
    # Rows are buckets, and columns are items
    baskets_matrix = np.zeros((n,n))
    for bucket_i in range(1, n + 1):
        # Since item will only divide bucket if item_i > bucket_i
        for item_i in range(bucket_i, n + 1):
            # Item i is in basket b if and only if
            # b divides i with no remainder.
            if item_i % bucket_i == 0:
                baskets_matrix[bucket_i - 1, item_i - 1] = 1
    return baskets_matrix

# Part a
def freq_items(baskets, s_threshold = 5):
    # Sums down the columns to get the count of each item in baskets
    summed_baskets = baskets.sum(axis=0)
    # Return the number of baskets over the threshold
    return sum(summed_baskets >= s_threshold)

# Part b
#
# Brute force method
def freq_pairs(baskets, s_threshold = 5):
    n = 100
    # Generate pairs of combinations
    results = []
    total_count = 0
    for i,j in it.combinations(xrange(n), 2):
        count = 0
        for k in range(n):
            if (baskets[k,i] * baskets[k,j]) == 1:
                count += 1
            if count >= s_threshold:
                total_count += 1
                count = 0
    return total_count

# Part c
def sum_bucket_size(baskets):
    # Sum the rows to get the size of each bucket
    basket_sizes = baskets.sum(axis=1)
    # Sum the sums to get total size
    return int(basket_sizes.sum())

## Exercise 6.1.2
# Not needed for homework
def max_basket(baskets):
    # Sum the rows for the basket length
    basket_lengths = baskets.sum(axis=1)
    return int(basket_lengths.max())

# Get support for baskets in non-matrix form
def support(baskets, items):
    count = 0
    set_items = set(items)
    n = len(set_items)
    for b in baskets:
        set_b = set(b)
        intersect = set_items.intersection(set_b)
        if len(intersect) >= n:
            count += 1
    return count

def confidence(baskets, items, j):
    return support(baskets, items + [j]) / float(support(baskets, items))

print "Exercise: 6.1.1"
baskets_m = generate_baskets_matrix(100)
print "frequent items: ", freq_items(baskets_m)
print "frequent pairs: ", freq_pairs(baskets_m)
print "Sum of bucket size: ", sum_bucket_size(baskets_m)
print ""

print "Exercise: 6.1.2"
print "Max bucket size: ", max_basket(baskets_m)
print ""

print "Exercise: 6.1.3"
alt_baskets_m = generate_alt_baskets_matrix(100)
print "frequent items: ", freq_items(alt_baskets_m)
print "frequent pairs: ", freq_pairs(alt_baskets_m)
print "Sum of bucket size: ", sum_bucket_size(alt_baskets_m)
print ""

print "Exercise: 6.1.5"
baskets = generate_baskets(100)
print "Confidence -  {5, 7} -> 2:", confidence(baskets, [5,7], 2)
print "Confidence - {2, 3, 4} -> 5:", confidence(baskets, [2,3,4], 5)
print ""

print "Exercise: 6.1.6"
alt_baskets = generate_alt_baskets(100)
print "Confidence -  {24, 60} -> 8:", confidence(alt_baskets, [24,60], 8)
print "Confidence -  {2, 3, 4} -> 5:", confidence(alt_baskets, [2,3,4], 5)
print ""
