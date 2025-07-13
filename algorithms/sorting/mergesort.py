def merge_sort(numbers):
    # dividing
    if len(numbers) > 1:
        middle = len(numbers) // 2
        left = numbers[:middle]
        right = numbers[middle:]

        merge_sort(left)
        merge_sort(right)

        # sorting and merging
        lp = 0
        rp = 0
        fp = 0

        while lp < len(left) and rp < len(right):
            if left[lp] < right[rp]:
                numbers[fp] = left[lp]
                lp += 1
            else:
                numbers[fp] = right[rp]
                rp += 1
            fp += 1

        while lp < len(left):
            numbers[fp] = left[lp]
            lp += 1
            fp += 1

        while rp < len(right):
            numbers[fp] = right[rp]
            rp += 1
            fp += 1

    return numbers

# test
numbers = [94, 3, 4, 5, 2, 6, 21]
print(f'unsorted list: {numbers}')
print(f'sorted list: {merge_sort(numbers)}')
