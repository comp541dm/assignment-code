import numpy as np

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

# Part c
def sum_bucket_size():
    baskets = generate_baskets_matrix(100)
    # Sum the rows to get the size of each bucket
    basket_sizes = baskets.sum(axis=1)
    # Sum the sums to get total size
    return int(basket_sizes.sum())

print freq_items()
print sum_bucket_size()
