'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # set target
    target = "th"
    # set length of input
    word_len = len(word)
    # set length of target
    target_len = len(target)
    
    # base case, no word
    if word_len == 0:
        return 0
    
    # recursive case, check if first substring passes
    if(word[0 : target_len] == target):
        return count_th(word[target_len - 1:]) + 1
    
    # otherwise, return the count from remaining index
    return count_th(word[target_len - 1:])




if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4, 5]
    word = "that"

    print(f"Output of product_of_all_other_numbers: {count_th(word)}")
