import sys


def number_generate():
    start, end = input(
        'Enter start and end of numbers space seperated : ').split()
    # start,end = '21b91a0489','21b91a04r3'
    regd_list = []
    end = end.lower()
    curr_num = start.lower()

    while curr_num != end:
        if curr_num[-2:].isnumeric():
            regd_list.append(curr_num)
            if int(curr_num[-2:]) == 99:
                curr_num = curr_num[:-2]+'a0'
            elif (int(curr_num[-2:])+1) < 10:
                curr_num = curr_num[:-2] + '0' + str(int(curr_num[-2:])+1)
            else:
                curr_num = curr_num[:-2] + str(int(curr_num[-2:])+1)
        else:
            if ord(curr_num[-2]) == 111 or ord(curr_num[-2]) == 79:
                curr_num = curr_num[:-2] + 'p0'
                continue
            if curr_num[-2].isalpha() and curr_num[-1].isnumeric():
                regd_list.append(curr_num)
                if curr_num[-1] == '9':
                    curr_num = curr_num[:-2] + chr(ord(curr_num[-2])+1) + '0'
                else:
                    curr_num = curr_num[:-1] + str(int(curr_num[-1])+1)
    regd_list.append(curr_num)

    print(regd_list)

    with open("students_list.txt", 'w') as file:
        yn = input(
            'Check the numbers generated above. Do you really want to continue to get the result (y/n) : ')
        if yn != 'y':
            print('Numbers generation stopped')
            sys.exit(0)
        for regd_no in regd_list:
            file.write('%s\n' % regd_no)
    return True
