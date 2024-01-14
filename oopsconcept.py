class Telecom :
    def numbers(self,code,number):
        self.code = code
        self.number = number
        #self.zipped_list = zipped_list
    def display(self):
       #self.zipped_list = zip(f"code{self.code},numbers{self.number}") """ This is not work """
       #print(zipped_list) """ This is not work """
       #print(f"code{self.code},numbers{self.number}")
      # print(zip(code,number)) """ This is not work """
      for i in range(len(code)):
        print(code[i], number[i])

Tel = Telecom()
#code = int(input()) " This line and below line are works but it takes single  code and single number data line by line "
#number = int(input())
code = [int(x) for x in input().split()[:6]]
number = [int(y) for y in input().split()[:6]]
Tel.numbers(code,number)
Tel.display()
