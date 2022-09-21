class solution():
    def shuffle(self, l, n):
        result = []
        
        for i in range(n):
            result.append(l[i])
            result.append(l[i+n])

        return result

a = solution()
l = [2,5,1,3,4,7]
n = 3
print(a.shuffle(l, n))