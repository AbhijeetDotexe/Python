def fibSum():
    first_term = 0
    second_term = 1
    result = 0
    while second_term <= 1000 :
        if second_term % 2 == 0 :
            result += second_term
        temp = second_term
        second_term += first_term
        first_term = temp
    
    return result

x = fibSum()
print( f'Sum of even valued terms of fibonacci sequence whose value do not exceed 1000 is {x}')
