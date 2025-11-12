def linear_search(student_ids, target_id):
    comparisons = 0
    for index, student_id in enumerate(student_ids):
        comparisons += 1
        if student_id == target_id:
            return index + 1, comparisons  
    return -1, comparisons 

def binary_search(scores, target_score):
    left, right = 0, len(scores) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if scores[mid] == target_score:
            return mid + 1, comparisons  
        elif scores[mid] < target_score:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons  # Not found

def main():
    student_ids = [2240240, 2240241, 2240242, 2240243, 2240244, 2240245, 2240246, 2240247, 2240248, 2240249, 2240250, 
                   2240251, 2240252, 2240253, 2240254, 2240255, 2240256, 2240257,]
    
    sorted_scores = [35, 40, 48, 53, 57, 62, 65, 70, 82, 87,
                     88, 90, 94]

    while True:
        print("\n=== Searching Algorithms Menu ===")
        print("Select a search operation (1-3):")
        print("1. Linear Search - Find Student ID")
        print("2. Binary Search - Find Score")
        print("3. Exit program")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Searching in the list: {student_ids}")
            target_id = int(input("Enter Student ID to search: "))
            result, comparisons = linear_search(student_ids, target_id)
            if result != -1:
                print(f"Result: Student ID {target_id} found at position {result} | Comparisons made: {comparisons}")
            else:
                print("Result: Student ID not found.")
        
        elif choice == '2':
            print(f"Sorted scores: {sorted_scores}")
            target_score = int(input("Enter Score to search: "))
            result, comparisons = binary_search(sorted_scores, target_score)
            if result != -1:
                print(f"Result: Score {target_score} found at position {result} | Comparisons made: {comparisons}")
            else:
                print("Result: Score not found.")
        
        elif choice == '3':
            print("Thank you for using the search program!")
            break
        
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
