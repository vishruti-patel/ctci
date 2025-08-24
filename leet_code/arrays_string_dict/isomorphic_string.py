def isomorphic(s, t):
        map1 = []
        map2 = []

        for i in s:
            map1.append(s.index(i))
        for i in t:
            map2.append(t.index(i))
        if map1 == map2:
            return True

        return False

if __name__ == "__main__":
     print(isomorphic('eggb ', 'add'))
    
