# طلب إدخال وصف المهمة
task = input("Enter your task: ")

# طلب إدخال أولوية المهمة
priority = input("Priority (high/medium/low): ")

# طلب إدخال ما إذا كانت المهمة محددة بوقت
time_bound = input("Is it time-bound? (yes/no): ")

# معالجة المهمة بناءً على الأولوية وحساسية الوقت
reminder = ""

# استخدام Match Case لمعالجة الأولوية
if priority == "high":
    reminder = f"'{task}' is a high priority task"
elif priority == "medium":
    reminder = f"'{task}' is a medium priority task"
elif priority == "low":
    reminder = f"'{task}' is a low priority task"

# تعديل التذكير إذا كانت المهمة محددة بوقت
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# طباعة التذكير المخصص
print("Reminder:", reminder)
