def convertIntToStr(number):
    strNumb = ''
    isNegative = False

    if number < 0:
        number = number * (-1)
        isNegative = True

    DICT_INT_TO_STR = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    if number == 0:
        strNumb = DICT_INT_TO_STR[number]
        return strNumb

    while(number != 0):
        digit = number % 10
        strNumb = DICT_INT_TO_STR[digit] + strNumb
        number = number // 10

    if isNegative:
        strNumb = '-' + strNumb

    return strNumb

for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
