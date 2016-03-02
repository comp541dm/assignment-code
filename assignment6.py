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

print generate_baskets(100)
