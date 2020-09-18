#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    O(n), because the runtime increases as n does.

b) O(n^c) ? 


c) Also O(n) because runtime increases as the recursive case runs?

## Exercise II
set lowest floor number
get number of floors
if the nuimber of floors is greater than 0
    divide total floors in half to set the middle
    set your guess to the middle
    if the guess is f
        return middle
    if guess is greater than f
        set the new max floor to be 0 - middle -1
    else
        set the new low and middle + 1


runtime: 0(log n)

