def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    
    result = []

    while lng != wdth:
        trim_size = 0
        if lng > wdth:
            trim_size = wdth
            lng -= wdth
        else:
            trim_size = lng
            wdth -= lng
        result.append(trim_size)

    result.append(lng)

    return result
