#Q1, Program takes 3 integers as an input
#The integer represent the number of times each employee traveled per trip
#Input 1 = Employee A * 1 etc.
#All inputs are then combined as a total then printed as a single input

A_input = int(input('Enter the number of trips Employee A travled'))
B_input = int(input('Enter the number of trips Employee B travled'))
C_input = int(input('Enter the number of trips Employee C travled'))

EmployeeA = float(15.62)
EmployeeB = float(41.85)
EmployeeC = float(32.67)

TotalMiles = ((A_input * EmployeeA) + 
              (B_input * EmployeeB) + 
              (C_input * EmployeeC))

print(f'Distance: {TotalMiles} miles')