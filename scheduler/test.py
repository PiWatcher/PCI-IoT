from datetime import datetime

today = datetime.now()
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")


with open('test.txt', 'a+') as test_file:
    test_file.write(f"Accessed at: {dt_string}\n")
