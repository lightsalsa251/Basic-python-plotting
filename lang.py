class lang:
    def vowel_detect(list):
        set = {'a','e','i','o','u'}
        a = [i for i in list if i in set]
        return a

    b = vowel_detect('I am uppal')
    print(b)
