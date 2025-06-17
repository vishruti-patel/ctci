def greatest_candy(candies,extracandy):
    greatest_candy = max(candies)
    new = []
    print('max is', greatest_candy)
    for  i in range(len(candies)):
        if candies[i] + extracandy >= greatest_candy:
            new.append(True)
        else:
            new.append(False)
    print(new)


greatest_candy([3,1,2,5,5], 3)