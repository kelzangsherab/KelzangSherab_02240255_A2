def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n-i-1):
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    return names

def insertion_sort(scores):
    for i in range(1, len(scores)):
        key = scores[i]
        j = i - 1
        while j >= 0 and key < scores[j]:
            scores[j + 1] = scores[j]
            j -= 1
        scores[j + 1] = key
    return scores

def quick_sort(prices, low, high, recursive_calls):
    if low < high:
        pi, recursive_calls = partition(prices, low, high, recursive_calls)
        recursive_calls = quick_sort(prices, low, pi-1, recursive_calls)
        recursive_calls = quick_sort(prices, pi+1, high, recursive_calls)
    return recursive_calls

def partition(prices, low, high, recursive_calls):
    pivot = prices[high]
    i = low - 1
    for j in range(low, high):
        if prices[j] <= pivot:
            i += 1
            prices[i], prices[j] = prices[j], prices[i]
    prices[i + 1], prices[high] = prices[high], prices[i + 1]
    return i + 1, recursive_calls + 1

def main():
    student_names = ["Dechen", "Dorji", "Kinga", "Kinley", "Lhamo", 
                     "Ugyen", "Dhendup", "Wangchu", "Rinchn", "Kezang", 
                     "Pema", "Samten", "Gyelpo", "Nidup", "Choki", "Phuntsho"]
    
    test_scores = [ 0, 1, 1.5, 2, 3, 3, 3.5, 4, 5.5, 6, 7, 8, 9,]
    
    book_prices = [20, 40, 65, 80, 85, 120, 130,175, 200, 210, 220, 240,275, 300, 450, 500]

    while True:
        print("\n=== Sorting Algorithms Menu ===")
        print("Select a sorting operation (1-4):")
        print("1. Bubble Sort - Sort Student Names")
        print("2. Insertion Sort - Sort Test Scores")
        print("3. Quick Sort - Sort Book Prices")
        print("4. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Original names: {student_names}")
            sorted_names = bubble_sort(student_names.copy())
            print(f"Sorted names: {sorted_names}")

        elif choice == '2':
            print(f"Original scores: {test_scores}")
            sorted_scores = insertion_sort(test_scores.copy())
            print(f"Sorted scores: {sorted_scores}")
            print("Top 5 Scores:")
            for i in range(1, 6):
                print(f"{i}. {sorted_scores[-i]}")

        elif choice == '3':
            print(f"Original prices: {book_prices}")
            recursive_calls = 0
            sorted_prices = book_prices.copy()
            recursive_calls = quick_sort(sorted_prices, 0, len(sorted_prices) - 1, recursive_calls)
            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {recursive_calls}")

        elif choice == '4':
            print("Thank you for using the sorting program!")
            break

        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
