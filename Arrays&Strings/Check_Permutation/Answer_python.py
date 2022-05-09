'''Fix needed god == dog'''
'''CASE! GOD == dog'''

# simple python built in
def check_permutation(str1, str2):
    
    if str1 in str2:
        return True
    else:
        return False

def check_permutation2(str1, str2):
    'if char start at the same char as str1, check the rest to see if it a match'
    
    i = 0
    while i != len(str2):
        if str2[i] == str1[0]:
            #check rest of string
            for i in range(len(str2[i:i+len(str1)])):
                if str2[i:i+len(str1)][i] != str1[i]:
                    break
                else:
                    return True
        return False
    


if __name__ == '__main__':
    # print(check_permutation('abc', 'aabbaadsabc'))
    print(check_permutation2('abc', 'asjhdafhoiqhwidabcadasdage'))
    