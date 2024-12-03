import json

class EmployeeData():
    def __init__(self):
        self.file_path = "DATA/DATAFILES/employees.json"
    def get_employee_data(self, employee_id):
        try:
            with open(self.file_path, "r") as file:
                employees = json.load(file)
            #Leitar af kennitölunni og returnar {} af öllum upplýsingum
            for employee in employees: 
                if employee["employeeID"] == employee_id:
                    return employee 
            return None
        except FileNotFoundError:
            print("Employee data file not found.")
            return None
    
    def get_all_employee_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Employee data file not found.")
            return []
    
    def update_employee_data(self, employee_id, updated_attributes):
        #Þegar það er kallað á þetta function þarf að kalla fram(kennitölu starfsmann, {"breyta": "nýtt gildi"})
        #Getur verið eins langt og þarf
        try:
            with open(self.file_path, "r") as file:
                employees = json.load(file)
            for employee in employees:
                if employee["employeeID"] == employee_id:
                    for key, value in updated_attributes.items():
                        if key in employee:
                            employee[key] = value
                    with open(self.file_path, "w") as file:
                        json.dump(employees, file, indent=4)
                    return True 
            return False  
        except FileNotFoundError:
            print("Employee data file not found.")
            return False
    


#Testing----------------
test = EmployeeData()
employee = test.get_employee_data(1404004412)
print(employee)
employees = test.get_all_employee_data()
print(employees)
#-----------------------