# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin("admin","123","B1 1AB") # username is "admin", password is "123"
    doctors = [Doctor("John","Smith","Internal Med."), Doctor("Jone","Smith","Pediatrics"), Doctor("Jone","Carlos","Cardiology")]
    patients = [Patient("Sara","Smith", 20, "07012345678", "B1 234", symptoms = ["headache"]), Patient("Mike","Jones", 37,"07555551234", "L2 2AB", symptoms = ["heavy breathing"]), Patient("Daivd","Smith", 15, "07123456789", "C1 ABC", symptoms = ["bodyache"])]
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print("Incorrect username or password.")

    while running:
        # print the menu
        print("\nChoose the operation:")
        print(" 1- Register/view/update/delete doctor")
        print(" 2- Discharge patients")
        print(" 3- View discharged patient")
        print(" 4- Assign doctor to a patient")
        print(" 5- Update admin detais")
        print(" 6- Quit")

        with open ("patient_details.txt","w") as file:
            for patient in patients:
                file.write(f"{patient._Patient__first_name}, {patient._Patient__surname}, {patient._Patient__age}{patient._Patient__mobile}, {patient._Patient__postcode}, {patient._Patient__doctor}, {patient._Patient__symptoms}\n")
        with open ("patient_details.txt","w") as file:
            for doctor in doctors:
                file.write(f"{doctor._Doctor__first_name}, {doctor._Doctor__surname}, {doctor._Doctor__speciality}, {doctor._Doctor__patients}\n")

        # get the option
        op = input("Option: ")

        if op == "1":
            # 1- Register/view/update/delete doctor
         #ToDo1
          admin.doctor_management(doctors = doctors)

        elif op == "2":
            # 2- View or discharge patients
            #ToDo2
            while True:
                op = input("Do you want to discharge a patient(Y/N):").lower()

                if op == "yes" or op == "y":
                    #ToDo3
                    admin.discharge(patients, discharged_patients)

                elif op == "no" or op == "n":
                    break

                # unexpected entry
                else:
                    print("Please answer by yes or no.")
        
        elif op == "3":
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients=discharged_patients)


        elif op == "4":
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif op == "5":
            # 5- Update admin detais
            admin.update_details()

        elif op == "6":
            # 6 - Quit
            #ToDo5
            print("-----Thank you!-----")
            break

        else:
            # the user did not enter an option that exists in the menu
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()
