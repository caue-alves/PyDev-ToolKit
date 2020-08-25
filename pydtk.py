import is_in

def that_in(trigger, to_verify):
    if type(trigger) is str:
        if is_in.str(trigger, to_verify):
            return True
        else:
            return False
    else:
        if is_in.str(trigger, to_verify):
            if is_in.array(trigger, to_verify):
                return True
            else:
                return False

def media(values):
    final = 0
    for value in values:
        final += value
    return final / len(values)

def explode(string):
    final_array = []
    for i in string:
        final_array.append(i)
    return final_array

def array_diff(array1, array2):
    final_list = []
    for i in array1:
        for a in array2:
            if i != a:
                final_list.append(i)

def implode(array):
    str = ""
    for i in array:
        str.join(i)
