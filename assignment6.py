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

def generate_baskets_matrix(n=100):
    # Makes an n x n matrix and uses 1 to represent in the bucket
    # Rows are buckets, and columns are items
    baskets_matrix = np.zeros((n,n))
    for bucket_i in range(1, n + 1):
        for item_i in range(1, bucket_i + 1):
            if bucket_i % item_i == 0:
                baskets_matrix[bucket_i - 1, item_i - 1] = 1
    return baskets_matrix

# Part a
def freq_items(s_threshold = 5):
    # Generates the basket matrix
    baskets = generate_baskets_matrix(100)
    # Sums down the columns to get the count of each item in baskets
    summed_baskets = baskets.sum(axis=0)
    # Return the number of baskets over the threshold
    return sum(summed_baskets >= s_threshold)

# Part b
#
# Brute force method
def freq_pairs(s_threshold = 5):
    n = 100
    baskets = generate_baskets_matrix(n)
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
def sum_bucket_size():
    baskets = generate_baskets_matrix(100)
    # Sum the rows to get the size of each bucket
    basket_sizes = baskets.sum(axis=1)
    # Sum the sums to get total size
    return int(basket_sizes.sum())

## Exercise 6.1.2
# Not needed for homework
def max_basket():
    baskets = generate_baskets_matrix(100)
    # Sum the rows for the basket length
    basket_lengths = baskets.sum(axis=1)
    return int(basket_lengths.max())

print "6.1.1"
print "frequent items: ", freq_items()
print "frequent pairs: ", freq_pairs()
print "Sum of bucket size: ", sum_bucket_size()

print "6.1.2"
print "Max bucket size: ", max_basket()
