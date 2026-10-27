def main():
    names = ["Henry", "Jovan", "Matthew", "Jerry"]

    for name in names:
        print(write_letter(name, "John Parker"))
 

def write_letter(receiver, sender):
    return f"""
=============================================
Dear {receiver}, 

You are invited to the interview for the position
of Python Automation Engineer that you applied for.
The interview will commence on January 11th 2026
at 10:30 am

Sincerely,
{sender}
============================================="""

main()