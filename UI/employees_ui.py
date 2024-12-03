from Models.employee import Employee


class EmployeeMenu:
    def __init__(self, logic_wrapper):
        self.running = True
        self.logic_wrapper = logic_wrapper
    def run(self):
        while self.running:
            print()
            self.user_input = self.print_menu()
            if self.user_input == "1":
                self.logic_wrapper.addEmployee()
            elif self.user_input == "2":
                #logic_wrapper.changeEmployeeInfo()"
                print("change")
            elif self.user_input == "3":
                #logic_wrapper.viewEmployeeList()"
                print("list")
            elif self.user_input == "4":
                #logic_wrapper.searchForEmployee()"
                print("search")
            elif self.user_input.lower() == "b":
                self.running = False
            else:
                print("Invalid Choice")

    def print_menu(self):
        print(f"\n[1] Add New Employee")
        print("[2] Change Employee Information")
        print("[3] View Employee List")
        print("[4] Search For Employee")
        print(f"[B] Back\n")
        return input("Choice: ")
        