
# EXPENSE, ATTENDANCE, GRADING AND BILLING MANAGEMENT SYSTEM

# Empty lists to store records
expenses = []
attendance = []
students = []
bills = []


# ---------------- EXPENSE MANAGEMENT ----------------

def expense_management():

    while True:

        print("\n--- EXPENSE MANAGEMENT ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            description = input("Enter expense name: ")
            category = input("Enter category: ")

            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:

                expense = {
                    "description": description,
                    "category": category,
                    "amount": amount
                }

                expenses.append(expense)

                print("Expense added successfully!")

        elif choice == "2":

            if len(expenses) == 0:
                print("No expenses found.")

            else:
                for e in expenses:
                    print("Name:", e["description"])
                    print("Category:", e["category"])
                    print("Amount: Rs.", e["amount"])
                    print("--------------------")

        elif choice == "3":

            total = 0

            for e in expenses:
                total = total + e["amount"]

            print("Total Expenses: Rs.", total)

        elif choice == "4":
            break

        else:
            print("Invalid choice!")


#                 ATTENDANCE MANAGEMENT

def attendance_management():

    while True:

        print("\n--- ATTENDANCE MANAGEMENT ---")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")

            total_days = int(input("Enter total working days: "))
            present_days = int(input("Enter present days: "))

            if total_days <= 0 or present_days < 0:
                print("Invalid attendance values.")

            elif present_days > total_days:
                print("Present days cannot exceed total days.")

            else:

                percentage = (present_days / total_days) * 100

                if percentage >= 75:
                    status = "Eligible"
                elif percentage >= 60:
                    status = "Warning"
                else:
                    status = "Shortage"

                record = {
                    "name": name,
                    "id": student_id,
                    "total": total_days,
                    "present": present_days,
                    "percentage": percentage,
                    "status": status
                }

                attendance.append(record)

                print("Attendance added successfully!")

        elif choice == "2":

            if len(attendance) == 0:
                print("No attendance records found.")

            else:
                for a in attendance:

                    print("\nStudent:", a["name"])
                    print("ID:", a["id"])
                    print("Present:", a["present"])
                    print("Total Days:", a["total"])
                    print("Percentage:", round(a["percentage"], 2), "%")
                    print("Status:", a["status"])

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


# ---------------- GRADING MANAGEMENT ----------------

def grading_management():

    while True:

        print("\n--- GRADING SYSTEM ---")
        print("1. Add Student Marks")
        print("2. View Student Report")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter student name: ")

            marks = []

            for i in range(5):

                mark = float(input("Enter marks for subject " + str(i + 1) + ": "))

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                    break

                marks.append(mark)

            if len(marks) == 5:

                total = 0

                for mark in marks:
                    total = total + mark

                average = total / 5

                if average >= 90:
                    grade = "A+"
                elif average >= 80:
                    grade = "A"
                elif average >= 70:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 50:
                    grade = "D"
                elif average >= 35:
                    grade = "E"
                else:
                    grade = "F"

                result = "PASS"

                for mark in marks:
                    if mark < 35:
                        result = "FAIL"

                student = {
                    "name": name,
                    "marks": marks,
                    "total": total,
                    "average": average,
                    "grade": grade,
                    "result": result
                }

                students.append(student)

                print("Student marks added successfully!")

        elif choice == "2":

            if len(students) == 0:
                print("No student records found.")

            else:
                for s in students:

                    print("\n------ REPORT CARD ------")
                    print("Student Name:", s["name"])
                    print("Marks:", s["marks"])
                    print("Total:", s["total"])
                    print("Average:", s["average"])
                    print("Grade:", s["grade"])
                    print("Result:", s["result"])

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


# ---------------- BILLING MANAGEMENT ----------------

def billing_management():

    customer = input("Enter customer name: ")

    items = []

    while True:

        print("\n--- BILLING SYSTEM ---")
        print("1. Add Item")
        print("2. Generate Bill")
        print("3. Back")

        choice = input("Enter choice: ")

        if choice == "1":

            item_name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter quantity: "))

            if price <= 0 or quantity <= 0:
                print("Invalid price or quantity.")

            else:

                total = price * quantity

                item = {
                    "name": item_name,
                    "price": price,
                    "quantity": quantity,
                    "total": total
                }

                items.append(item)

                print("Item added successfully!")

        elif choice == "2":

            if len(items) == 0:
                print("No items added.")

            else:

                subtotal = 0

                print("\n========== INVOICE ==========")
                print("Customer:", customer)

                for item in items:

                    print(item["name"],
                          item["price"],
                          item["quantity"],
                          item["total"])

                    subtotal = subtotal + item["total"]

                discount = 0

                if subtotal >= 1000:
                    discount = subtotal * 0.05

                taxable = subtotal - discount

                tax = taxable * 0.18

                grand_total = taxable + tax

                print("----------------------------")
                print("Subtotal:", subtotal)
                print("Discount:", discount)
                print("Tax:", tax)
                print("Grand Total:", grand_total)
                print("============================")

                bill = {
                    "customer": customer,
                    "total": grand_total
                }

                bills.append(bill)

                break

        elif choice == "3":
            break

        else:
            print("Invalid choice!")


# ---------------- VIEW REPORTS ----------------

def view_reports():

    print("\n--- ALL REPORTS ---")

    print("Total Expenses:", len(expenses))
    print("Total Attendance Records:", len(attendance))
    print("Total Students:", len(students))
    print("Total Bills:", len(bills))

    total_expense = 0

    for e in expenses:
        total_expense = total_expense + e["amount"]

    print("Total Expense Amount: Rs.", total_expense)

    total_billing = 0

    for b in bills:
        total_billing = total_billing + b["total"]

    print("Total Billing Amount: Rs.", total_billing)


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n====================================")
        print(" EXPENSE MANAGEMENT SYSTEM")
        print(" ATTENDANCE MANAGEMENT SYSTEM")
        print(" GRADING MANAGEMENT SYSTEM")
        print(" BILLING MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Expense Management")
        print("2. Attendance Management")
        print("3. Grading System")
        print("4. Billing System")
        print("5. View Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            expense_management()

        elif choice == "2":
            attendance_management()

        elif choice == "3":
            grading_management()

        elif choice == "4":
            billing_management()

        elif choice == "5":
            view_reports()

        elif choice == "6":
            print("Thank you! Program closed.")
            break

        else:
            print("Invalid choice. Try again.")


# Start Program

if __name__ == "__main__":
    main()
