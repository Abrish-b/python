# bytecode with exceptions
import dis


def magic_calculation(a, b):
    result = 0

    for i in range(3, 1):
        try:
            if(i > a):
                raise Exception('too far')
            else:
                result += (a**b)/i
        except:
            result = b+a
            break
    return result


dis.dis(magic_calculation)
