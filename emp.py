employee_data = {
    "John": {"age": 30, "salary": 50000},
    "Alice": {"age": 25, "salary": 60000},
    "Bob": {"age": 40, "salary": 70000}
}
salaries = [employee["salary"] for employee in employee_data.values()]
print("Total salary:", sum(salaries))
print("Minimum salary:", min(salaries))
print("Maximum salary:", max(salaries))