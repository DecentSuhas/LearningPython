def pattern_1():
    '''
    *
    * *
    * * *
    * * * *
    * * * * *
    '''

    for i in range(0, 5):
        for j in range(0, i+1):
            print(' * ', end='')
        print('')


def patter_2():
    '''
     *  *  *  *  *
     *  *  *  *
     *  *  *
     *  *
     *
    '''
    for i in range(0, 5):
        for j in range(i, 5):
            print(' * ', end='')
        print('')


def patter_3():
    '''
     *  *  *  *  *
     *  *  *  *  *
     *  *  *  *  *
     *  *  *  *  *
     *  *  *  *  *
    '''
    for i in range(0, 5):
        for j in range(0, 5):
            print(' * ', end='')
        print('')