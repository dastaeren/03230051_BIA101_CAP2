class Employee:
    def __init__(self, salary, employment_type, organization_type):
        # Initialize an Employee object with salary, employment type, and organization type
        self.salary = salary
        self.employment_type = employment_type
        self.organization_type = organization_type
        self.sum_assured = sum_assured

class TaxCalculator:
    def __init__(self, employee, num_children, children_in_school):
        # Initialize a TaxCalculator object with an Employee, number of children, and whether they are in school
        self.employee = employee
        self.num_children = num_children
        self.children_in_school = children_in_school
        # Calculate taxable income, total deductions, and final tax immediately upon initialization
        self.taxable_income = self.calculate_taxable_income()
        self.total_deductions = self.calculate_total_deductions()
        self.final_tax = self.calculate_final_tax()
        

    def calculate_taxable_income(self):
        # Return the employee's salary as the taxable income
        return self.employee.salary
    
    def calculate_monthly_payment_for_gis(self):
        # Calculate monthly payment based on sum assured
        return self.employee.sum_assured / 12
    
    def calculate_total_deductions(self):
    # Calculate total deductions based on employment type, organization type, and number of children in school
        total_deductions = 0

        # Add deductions for regular employees and government employees
        if self.employee.employment_type == "Regular" or "Government":
         total_deductions += self.employee.salary * 0.11  # 11% Employee 
         total_deductions += self.employee.salary * 0.16  # 16% Pension
         total_deductions += self.employee.salary * 0.10  # 10% Provident Fund

        # Add deductions for private organizations
        if self.employee.organization_type == "Private":
            total_deductions += min(0.05 * self.employee.salary, 0.1 * self.employee.salary)  # Minimum 5% or 10% of total income

          # Adjusting for Corporate Agencies based on Pay Revision
        if self.employee.organization_type == "Corporate":
            pay_revision_rate = float(input("Enter the Pay Revision rate (22%, 26%, or 30%): "))
            if pay_revision_rate == 22:
                total_deductions += self.employee.salary * 0.16  # 16% Pension
                total_deductions += self.employee.salary * 0.06  # 6% PF
            elif pay_revision_rate == 26:
                total_deductions += self.employee.salary * 0.16  # 16% Pension
                total_deductions += self.employee.salary * 0.10  # 10% PF
            elif pay_revision_rate == 30:
                total_deductions += self.employee.salary * 0.16  # 16% Pension
                total_deductions += self.employee.salary * 0.14  # 14% PF

        # Add education allowance for each child in school
        for i in range(self.num_children):
            if self.children_in_school[i].lower() == "yes":
                total_deductions += 350000  # Education allowance for each child in school
        return total_deductions
    
    def calculate_final_tax(self):
        # Calculate the final tax based on taxable income after deductions
        if self.taxable_income <= 300000:
            return 0  # Exempt for individuals earning less than the minimum taxable income
        taxable_income_after_deductions = self.taxable_income - self.total_deductions
        if taxable_income_after_deductions <= 300000:
            return 0  # Additional check after deductions
        elif taxable_income_after_deductions <= 400000:
            return taxable_income_after_deductions * 0.10
        elif taxable_income_after_deductions <= 650000:
            return taxable_income_after_deductions * 0.15
        elif taxable_income_after_deductions <= 1000000:
            return taxable_income_after_deductions * 0.20
        elif taxable_income_after_deductions <= 1500000:
            return taxable_income_after_deductions * 0.25
        else:
            return taxable_income_after_deductions * 0.30

    def get_final_tax(self):
        # Return the final tax calculated earlier
        return self.final_tax
    
class GISCalculator:
    # Initialize a GISCalculator object with an Employee
    def __init__(self, employee):
        self.employee = employee

    def calculate_monthly_payment(self):
    # Calculate the monthly payment for GIS based on the sum assured
        return self.employee.sum_assured / 12

name = input("Enter your Name: ")
position = input("Enter your Designation: ")
salary = float(input("Enter your salary: "))

# Check if salary is less than 300,000 and print a message
if salary < 300000:
    print("Your salary must be at least 300,000.")
else:
    employment_type = input("Enter your employment type (Contract/Regular): ")
    organization_type = input("Enter your organization type (Government/Private/Corporate): ")

    sum_assured = float(input("Enter the sum assured for GIS: "))
    num_children = int(input("Enter the number of children: "))

    # Initialize an empty list to store whether each child is in school
    children_in_school = []
    # Loop through each child and ask if they are in school
    for i in range(num_children):
        children_in_school.append(input(f"Is child {i+1} in school? (Yes/No): "))

    # Create an Employee object with the provided salary, employment type, and organization type
    # Create a TaxCalculator object with the employee, number of children, and whether each child is in school
    # Create a GISCalculator object with the employee
    employee = Employee(salary, employment_type, organization_type)
    tax_calculator = TaxCalculator(employee, num_children, children_in_school)
    gis_calculator = GISCalculator(employee)

    print(f"Your final tax amount is: {tax_calculator.get_final_tax()}")
    print(f"Your monthly GIS payment is: {gis_calculator.calculate_monthly_payment()}")

