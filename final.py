import random
import time
import matplotlib.pyplot as plt


# Linear Search: checks each element one by one
# Time Complexity: O(n)
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


# Binary Search: repeatedly cuts the search range in half
# Requires the list to already be sorted
# Time Complexity: O(log n)
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


# Generates a sorted list of integers
def generate_test_data(size):
    numbers = list(range(size))
    return numbers


# Measures how long a search function takes (averaged over multiple runs)
def measure_time(search_function, numbers, target, runs=100):
    start_time = time.perf_counter()
    for _ in range(runs):
        search_function(numbers, target)
    end_time = time.perf_counter()

    return (end_time - start_time) / runs


def main():
    # Different input sizes to test
    input_sizes = [100, 1000, 5000, 10000, 50000, 100000, 500000]

    linear_times = []
    binary_times = []

    print("Searching Algorithm Efficiency Results")
    print("--------------------------------------")
    print(f"{'Size':<12}{'Linear Search':<20}{'Binary Search':<20}")

    for size in input_sizes:
        numbers = generate_test_data(size)

        # Worst-case target: last element in the list
        # Linear search has to scan the whole list
        target = numbers[-1]

        linear_time = measure_time(linear_search, numbers, target)
        binary_time = measure_time(binary_search, numbers, target)

        linear_times.append(linear_time)
        binary_times.append(binary_time)

        print(f"{size:<12}{linear_time:<20.10f}{binary_time:<20.10f}")

    # Create a graph comparing execution times
    plt.plot(input_sizes, linear_times, marker='o', label='Linear Search')
    plt.plot(input_sizes, binary_times, marker='o', label='Binary Search')

    plt.title("Linear Search vs Binary Search Execution Time")
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid(True)

    # Saves the graph as an image file
    plt.savefig("results.png")

    # Displays the graph
    plt.show()


if __name__ == "__main__":
    main()