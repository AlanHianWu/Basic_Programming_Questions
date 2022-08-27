def check_unique(string):
    
    dict = {}
    i = 0
    while i != len(string):
        
        if string[i] in dict:
            return False
        dict[string[i]] = i
        i += 1
    return True



if __name__ == '__main__':
    t = 'abcd'
    
    '''Run speed should be O(n^2) or O(nlogn) depending on the speed of the in operator'''
    
    print(check_unique(t))
