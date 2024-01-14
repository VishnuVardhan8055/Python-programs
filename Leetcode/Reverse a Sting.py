# class Reverse:
#     def ReverseSolution(self,Str):
#         data = []
#         for word in Str:
#             data.append(word[::-1])
#         return" ".join(data)
# S = Reverse()
# Str = input()
# S.ReverseSolution(Str)
class Reverse:
    def ReverseSolution(self, Str):
        data = []
        for word in Str.split():
            data.append(word[::-1])
        return " ".join(data)

S = Reverse()
Str = input()
print(S.ReverseSolution(Str))
