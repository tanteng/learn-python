import random, string


def rand_str(num, length=7):
    f = open('Activation_code.txt', 'w')
    for i in range(num):
        chars = string.ascii_letters + string.digits
        s = [random.choice(chars) for i in range(length)]
        f.write('{0}\n'.format(''.join(s)))
    f.close()


if __name__ == '__main__':
    rand_str(200)
