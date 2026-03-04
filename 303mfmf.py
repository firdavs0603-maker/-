'''def ff(p):
  return  p % 3600
p=int(input("p="))
natija=(P)
print("Soniyahoi pas az soathoi ohiron",natija)'''


def check_sequence(nums):
    if len(nums) < 2:
        return "Пайдарпаӣ кӯтоҳ аст"
    
    # тафтиш мекунем, ки ҳамаи ҷуфтҳо афзояндаанд
    is_increasing = all(map(lambda pair: pair[0] < pair[1], zip(nums, nums[1:])))
    
    # тафтиш мекунем, ки ҳамаи ҷуфтҳо камшавандаанд
    is_decreasing = all(map(lambda pair: pair[0] > pair[1], zip(nums, nums[1:])))
    
    if is_increasing:
        return "Пайдарпаӣ афзоянда аст"
    elif is_decreasing:
        return "Пайдарпаӣ камшаванда аст"
    else:
        return "Пайдарпаӣ на афзоянда ва на камшаванда аст"
print(check_sequence([1, 2, 3, 4, 5]))
