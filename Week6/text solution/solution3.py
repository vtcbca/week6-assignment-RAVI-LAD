with open('Python.txt','r') as file_read:
    file_data = file_read.read()
    total_no_lines = len(file_data.split('.'))
    print(f"Total No Of Lines :: {total_no_lines}")
    print("Total No Of Words :: {}".format(len(file_data.split())))
