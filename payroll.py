import copy

# ── Global variables — do not modify ─────────────────────────────────────────

employee_list = []
employee_set  = set()
employee_records  = {}
employee_benefits = {}

VALID_LEVELS      = {'employee', 'manager', 'executive'}
VALID_DEPARTMENTS = {'engineering', 'marketing', 'hr', 'finance', 'operations'}
VALID_PAY_TYPES   = {'hourly', 'salary'}

BENEFITS = {
    'healthcare': ('Health Insurance',        150.0),
    'childcare':  ('Child Care Support',      100.0),
    'transport':  ('Public Transport Benefit', 50.0),
}

change_log = []

# ── Your implementations go below ────────────────────────────────────────────


# Part 1 — Employee Registration

def add_employee(input_str):
    fields = input_str.split()

    if len(fields) != 5:
        raise ValueError(f"Expected 5 fields, got {len(fields)}")

    name, level, dept, pay_type, pay_amount = fields

    if name in employee_set:
        raise ValueError(f"Name already exists: {name}")

    if level not in VALID_LEVELS:
        raise ValueError(f"Invalid level: {level}")

    if dept not in VALID_DEPARTMENTS:
        raise ValueError(f"Invalid department: {dept}")

    if pay_type not in VALID_PAY_TYPES:
        raise ValueError(f"Invalid pay type: {pay_type}")

    try:
        pay_amount = float(pay_amount)
    except:
        raise ValueError(f"Invalid pay amount: {pay_amount}")

    employee_list.append(name)
    employee_set.add(name)

    employee_records[name] = {
        'level': level,
        'department': dept,
        'pay_type': pay_type,
        'pay_amount': pay_amount,
    }

    employee_benefits[name] = set()

    return employee_records[name]


def run_registration():
    count = 0

    while True:
        input_str = input("Enter employee info (or 'quit' to stop): ")

        if input_str == 'quit':
            break

        try:
            add_employee(input_str)

            name = input_str.split()[0]
            print(f"Employee {name} added successfully.")

            count += 1

        except ValueError as err:
            print(f"Error: {str(err)}. Please try again.")

    print(f"{count} employee(s) registered.")

# Part 2 — Accessors

def get_employee(name):
    return employee_records[name]

def get_employees_by_department(dept):
    result = []

    for name in employee_records:
        if employee_records[name]['dept'] == dept:
            result.append(name)

    return result

def get_employees_by_level(level):
    result = []

    for name in employee_records:
        if employee_records[name]['level'] == level:
            result.append(name)

    return result


# Part 3 — Benefit Assignment

def assign_benefit(name, benefit_code):
    if name not in employee_records:
        raise KeyError(name)

    if benefit_code not in BENEFITS:
        raise ValueError(f"Invalid benefit code: {benefit_code}")

    employee_benefits[name].add(benefit_code)


# Part 4 — Change Log and Modifiers

def save_to_change_log(name):
    snapshot = copy.deepcopy(employee_records[name])

    change_log.append({
        'name': name,
        'old_record' : snapshot
    })


def update_employee_pay(name, new_amount):
    if name not in employee_records:
        raise KeyError(name)

    try:
        new_amount = float(new_amount)
    except:
        raise ValueError(f"Invalid pay amount: {new_amount}")

    save_to_change_log(name)

    employee_records[name]['pay_amount'] = new_amount


def update_employee_level(name, new_level):
    if name not in employee_records:
        raise KeyError(name)

    if new_level not in VALID_LEVELS:
        raise ValueError(f"Invalid level: {new_level}")

    save_to_change_log(name)

    employee_records[name]['level'] = new_level


def remove_employee(name):
    if name not in employee_records:
        raise KeyError(name)

    save_to_change_log(name)

    del employee_records[name]

    employee_set.remove(name)

    employee_list.remove(name)

    del employee_benefits[name]

