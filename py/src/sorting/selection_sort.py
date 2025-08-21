def selection_sort(input_list: list[int]) -> list[int]:
    list_len = len(input_list)
    for i in range(list_len):
        min_ = i
        for j in range(i + 1, len(input_list)):
            if input_list[j] < input_list[min_]:
                min_ = j
        input_list[i], input_list[min_] = input_list[min_], input_list[i]
    return input_list
