random_dict = {}

def main():
    random = input("Enter any details you want to store, i.e Name, School, House, Gender, etc: ")
    random_value = input(f"What is your {random}? ")
    random2 = input("Enter second details you want to store, i.e Name, School, House, Gender, etc: ")
    random2_value = input(f"What is your {random2}? ")

    random_dict[random] = random_value
    random_dict[random2] = random2_value 

    print(details_report(random_dict, random, random2))

def details_report(random_dict, random, random2):
    return f"""
======== REPORT ========
Here are all your details:

{random}: {random_dict.get(random, "Unknown")}
{random2}: {random_dict.get(random2, "Unknown")}

========================
"""

main()