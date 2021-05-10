
days_in_year = 365
hours_in_year = days_in_year * 24
minutes_in_year = hours_in_year * 60
seconds_in_year = minutes_in_year * 60
convert_type = input("Display your age using 1: days, 2:hours, 3:minutes,4: seconds\n")


def convert_age(age, choice):
    """
    This function convert age to a value specified by choice parameter
    :param age: age in years
    :param choice: specify how to convert given age
    :return: age converter to chosen form
    """

    if type(age) not in [float, int]:
        raise TypeError("Age must be a number! ")
    if age < 0:
        raise ValueError("Age can not have minus value")

    age_in_days = age * days_in_year
    age_in_hours = age * hours_in_year
    age_in_minutes = age * minutes_in_year
    age_in_seconds = age * seconds_in_year

    if choice == '1':
        return age_in_days
    elif choice == '2':
        return age_in_hours
    elif choice == '3':
        return age_in_minutes
    elif choice == '4':
        return age_in_seconds


