from UI.employees_ui import EmployeeMenu
from LOGIC.logic_wrapper import LogicWrapper

class MainMenu():
    def __init__(self):
        self.running = True
        self.logic_wrapper = LogicWrapper()

    def run(self):
        while self.running:
            self.user_input = self.print_menu()
            if self.user_input == "1":
                EmployeeMenu(self.logic_wrapper).run()
            elif self.user_input == "2":
                #freelancers_ui.run()
                print("#freelancers_ui.run()")
            elif self.user_input == "3":
                #properties_ui.run()
                print("#properties_ui.run()")
            elif self.user_input == "4":
                #destinations_ui.run()
                print("#destinations_ui.run()")
            elif self.user_input.lower() == "q":
                self.running = False
                print("Quitting...")
            else:
                print("Invalid Choice")

    def print_menu(self):
        print(f"\n[1] Employees")
        print("[2] Freelancers")
        print("[3] Properties")
        print("[4] Destinations")
        print(f"[Q] Quit\n")
        return input("Choice: ")
        