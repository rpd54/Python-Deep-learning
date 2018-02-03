def fndTrplts(lst, n):
    fnd = True
    #for the first digit
    for p in range(0, n - 2):
        #for 2nd digit
        for q in range(p + 1, n - 1):
            #for 3rd digit
            for r in range(q + 1, n):
                #taking 3 nos at index level and checking it to "0"
                if (lst[p] + lst[q] + lst[r] == 0):
                    tup=(lst[p], lst[q], lst[r])
                    out=list(tup)
                    print("Triplets are as follows:",out,)
                    found = True

    # If there are no triplets in the array
    if (fnd == False):
        print("No triplets found in the Array ")
# Input
lst = [1,3,6,2,-1,2,8,-2,9]
print("Given list",lst)
n = len(lst)
#calling the function
fndTrplts(lst, n)