def map(key, value, map_func):
    """
    Applies the map function to a key-value pair and emits intermediate pairs.
    Args:
    key: The input key.
    value: The input value.
    map_func: The map function to apply.
    Returns:
    A list of intermediate key-value pairs.
    """
    intermediate_pairs = []
    for key_out, value_out in map_func(key, value):
        intermediate_pairs.append((key_out, value_out))
    return intermediate_pairs

def reduce(key, values, reduce_func):
    """
    Applies the reduce function to a key and its associated values.
    Args:
    key: The intermediate key.
    values: A list of intermediate values for the key.
    reduce_func: The reduce function to apply.
    Returns:
    The final value for the key.
    """
    return reduce_func(key, values)

def mapreduce(data, map_func, reduce_func):
    """
    Executes the MapReduce job on a single machine.
    Args:
    data: An iterable containing key-value pairs.
    map_func: The map function to apply.
    reduce_func: The reduce function to apply.
    Returns:
    A dictionary containing the final results (key-value pairs).
    """
    # Apply map phase
    intermediate_data = {}
    for key, value in data:
        for key_out, value_out in map(key, value, map_func):
            if key_out not in intermediate_data:
                intermediate_data[key_out] = []
            intermediate_data[key_out].append(value_out)

    # Shuffle & sort (simulated)
    sorted_data = {}
    for key, values in intermediate_data.items():
        sorted_data[key] = sorted(values)

    # Apply reduce phase
    results = {}
    for key, values in sorted_data.items():
        results[key] = reduce(key, values, reduce_func)

    return results

# Example usage

def word_count_map(key, value):
    """
    Map function for word count example.
    """
    for word in value.split():
        yield (word, 1)

def word_count_reduce(key, values):
    """
    Reduce function for word count example.
    """
    return sum(values)

data = [("doc1", "my name is riya patil"), ("doc2", "my fathers name is rajesh")]
word_counts = mapreduce(data, word_count_map, word_count_reduce)
print(word_counts)
