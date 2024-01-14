class Solution:
    def defangIPaddr(self, address):
        l = []
        for i in address:
            if i != '.':
                l.append(i)
            else:
                l.append('[.]')
        return ''.join(l)

address = '1.1.1'
Sol = Solution()
print(Sol.defangIPaddr(address))

