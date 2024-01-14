class AIDS():
    Student_name = ''
    Roll_Number = ''
    Year = ''
    Mobile_Number = ''
    Percentage = ''
    def DATA(self,Student_name,Roll_Number,Year,Mobile_Number,Percentage):
        self.Student_name = Student_name 
        self.Roll_Number = Roll_Number
        self.Year = Year
        self.Mobile_Number = Mobile_Number
        self.Percentage = Percentage
class HOD(AIDS):     #  """ Used Inheretence Concept here """
    def Display(self):
        for i in range(len(Student_name)):
            print(Student_name[i],Roll_Number[i],Year[i],Mobile_Number[i],Percentage[i],sep = "\n")
#Student_name = input('')
Student_name = [ str(x) for x in input().split()[:43]]
Roll_Number = [int(y) for y in input().split()[:43]]
Year = [int(z) for z in input().split()[:43]]
Mobile_Number = [int(w) for w in input().split()[:43]]
Percentage = [float(t) for t in input().split()[:43]]
print("Name", "Roll_Number", "Year", "Mobile Number", "percentage", end="   ")
HOD.Display(Student_name)

