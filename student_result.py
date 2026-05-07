students = {}

while True:
    print("\n--- STUDENT RESULT SYSTEM ---")
    print("1. Add Student")
    print("2. View Result")
    print("3. View All Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        
        if marks >= 90:
            grade = "A+"
        elif marks >= 75:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "Fail"

        students[name] = (marks, grade)
        print("✅ Student added successfully!")

    elif choice == "2":
        name = input("Enter student name: ")
        if name in students:
            print(f"Marks: {students[name][0]}")
            print(f"Grade: {students[name][1]}")
        else:
            print("❌ Student not found")

    elif choice == "3":
        print("\n📋 All Students:")
        for name, data in students.items():
            print(f"{name} -> Marks: {data[0]}, Grade: {data[1]}")

    elif choice == "4":
        print("👋 Exiting...")
        break

    else:
        print("❌ Invalid choice")