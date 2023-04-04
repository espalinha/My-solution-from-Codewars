def cube_checker(volume, length):
    if volume < 0 or length <= 0:
        return False
    else:
        if volume / length ** 3 == 1:
            return True
        else:
            return False



