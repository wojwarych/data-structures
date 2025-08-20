def selection_sort(input_list: list[int]) -> list[int]:
    for i in range(len(input_list)):
        min_ = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_]:
                min_ = j
        input_list[i], input_list[min_] = input_list[min_], input_list[i]
    return input_list


l = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(selection_sort(l))
