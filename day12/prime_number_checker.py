def is_prime(num):
    i = 0
    if num == 2 or num == 5 or num == 3:
        return True
    else:
        if num % 2 == 0:
            i += 1
        if num % 3 == 0:
            i += 1
        if num % 5 == 0:
            i += 1
        if i >= 1:
            return False
        else:
            return True