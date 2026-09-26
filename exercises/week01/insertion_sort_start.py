"""
Oefening 1: Insertion Sort
===========================
Implementeer insertion sort volgens het stappenplan in opgave_week1.md.
"""


def insertion_sort(sequence):
    for i in range(1, len(sequence)):
        key = sequence[i]
        j = i - 1
        while j >= 0 and sequence[j] > key:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = key
    return sequence


#aaa

if __name__ == "__main__":
    # Test je implementatie met deze voorbeelden
    test_lijsten = [
        [],
        [42],
        [1, 2, 3, 4],
        [5, 4, 3, 2, 1],
        [3, 1, 2, 1, 3],
        [5, 2, 4, 6, 1, 3],
    ]

    for lijst in test_lijsten:
        origineel = lijst.copy()
        gesorteerd = insertion_sort(lijst)
        print(f"Origineel: {origineel} -> Gesorteerd: {gesorteerd}")

    # Stap 5 (uitbreiding): vergelijk met bubble sort en merge sort
    # Kopieer bubble_sort en merge_sort uit de cursus en test hier:
    import random
    import time
    # ...

    def bubble_sort(sequence):
        n = len(sequence)
        for i in range(n-1):
            for j in range(n-i-1):
                if sequence[j] > sequence[j+1]:
                    sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
        return sequence


    def merge_sort(sequence):
        size = len(sequence)
        if size > 1:
            middle = size // 2
            left_arr = sequence[:middle]
            right_arr = sequence[middle:]
            
            merge_sort(left_arr)
            merge_sort(right_arr)
            
            p = q = r = 0
            while p < len(left_arr) and q < len(right_arr):
                if left_arr[p] < right_arr[q]:
                    sequence[r] = left_arr[p]
                    p += 1
                else:
                    sequence[r] = right_arr[q]
                    q += 1
                r += 1
            
            while p < len(left_arr):
                sequence[r] = left_arr[p]
                p += 1
                r += 1
            
            while q < len(right_arr):
                sequence[r] = right_arr[q]
                q += 1
                r += 1

# Plak dit helemaal onderaan je bestand:
    for n in [10, 100, 1000, 10000]:
        test_lijst = [random.randint(0, 10000) for _ in range(n)]
        print(f"\n--- Tijd voor {n} items ---")
        
        start = time.time()
        insertion_sort(test_lijst.copy())
        print(f"Insertion Sort: {time.time() - start:.5f} sec")
        
        start = time.time()
        bubble_sort(test_lijst.copy())
        print(f"Bubble Sort:    {time.time() - start:.5f} sec")
        
        start = time.time()
        merge_sort(test_lijst.copy())
        print(f"Merge Sort:     {time.time() - start:.5f} sec")

