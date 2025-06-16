# word_count_mapreduce.py

from collections import defaultdict

def mapper(line):
    """Map function that yields (word, 1) pairs."""
    words = line.strip().split()  # split only by space
    for word in words:
        yield (word, 1)

def reducer(word, counts):
    """Reduce function that sums counts for a word."""
    return (word, sum(counts))

def main():
    intermediate = []

    # Step 1: Read the file and apply mapper
    with open("input.txt", "r") as file:
        for line in file:
            for pair in mapper(line):
                intermediate.append(pair)

    # Step 2: Sort intermediate output by word (key)
    intermediate.sort(key=lambda x: x[0])

    # Step 3: Group by word and apply reducer
    word_counts = defaultdict(list)
    for word, count in intermediate:
        word_counts[word].append(count)

    # Step 4: Apply reducer and print results
    for word in sorted(word_counts.keys()):
        output = reducer(word, word_counts[word])
        print(f"{output[0]} {output[1]}")

if __name__ == "__main__":
    main()
