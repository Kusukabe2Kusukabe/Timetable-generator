print("Welcome to the Timetable Generator!\n")

# Get the days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create an empty timetable
timetable = {}

# Number of subjects
num_subjects = int(input("Enter the number of subjects: "))

# Input the subject names
subjects = []
for i in range(num_subjects):
    subject = input(f"Enter subject {i+1}: ")
    subjects.append(subject)

# Input class hours per day
for day in days:
    timetable[day] = []
    num_classes = int(input(f"Enter the number of classes for {day}: "))
    
    # Get subjects for the day
    for i in range(num_classes):
        print(f"\nAvailable subjects: {', '.join(subjects)}")
        subject = input(f"Enter subject for class {i+1} on {day}: ")
        
        if subject in subjects:
            timetable[day].append(subject)
        else:
            print("Invalid subject! Please enter a valid subject.")
            subject = input(f"Enter subject for class {i+1} on {day}: ")
            timetable[day].append(subject)

# Display the timetable
print("\nYour generated timetable is:\n")
for day in days:
    print(f"{day}:")
    for i, subject in enumerate(timetable[day]):
        print(f"  {i+1}. {subject}")
    print()
