def closest_to_zero(num1, num2, num3, k):
    num1 = 2
    num2 = 7 
    num3 = 1
    k = 0
    
    int_list = [num1, num2, num3]

    return int_list[min(range(len(int_list)), key = lambda i: abs(int_list[i] - k))]

    print(closest_to_zero(int_list, k))