# LeetCode-Style: MapReduce Word Count in Python (single file)

from collections import defaultdict

def map_phase(line):
    """Simulate the Mapper: emits (word, 1) pairs from a line of text"""
    words = line.strip().split()
    for word in words:
        yield word, 1

def shuffle_sort(mapped_data):
    """Simulate Shuffle and Sort: groups counts by word"""
    shuffled = defaultdict(list)
    for word, count in mapped_data:
        shuffled[word].append(count)
    return shuffled

def reduce_phase(shuffled_data):
    """Simulate the Reducer: aggregates counts for each word"""
    reduced = {}
    for word, counts in shuffled_data.items():
        reduced[word] = sum(counts)
    return reduced

def word_count_from_file(file_path):
    """Main function to read file and perform MapReduce word count"""
    mapped_data = []
    with open(file_path, 'r') as file:
        for line in file:
            mapped_data.extend(map_phase(line))
    
    shuffled_data = shuffle_sort(mapped_data)
    reduced_data = reduce_phase(shuffled_data)

    for word in sorted(reduced_data.keys()):
        print(f"{word}\t{reduced_data[word]}")

# Run the word count on a text file
if __name__ == "__main__":
    word_count_from_file("/Users/vishruti/workspace/ctci/leet_code/mapreduce/input.txt")
