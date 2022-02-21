def check_palindrome(str_list):

    result = []
    for name in str_list:
        if name[::-1].lower() == name.lower():
            result.append(name)
    return result


if __name__ == '__main__':
    count = int(input())
    inp_str = []
    for i in range(count):
        inp_str.append(input())
    output = check_palindrome(inp_str)
    if len(output) != 0:
        for i in output:
            print(i)
    else:
        print('No palindrome found')
