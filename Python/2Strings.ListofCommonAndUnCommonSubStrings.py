def stringDiff(base, delta, compared={'common':[], 'added':[], 'removed':[]}, look_for_same_char=True):
    if len(base) == 0:
        compared.get('added').append(delta)
        return compared
    elif len(delta) == 0:
        compared.get('removed').append(base)
        return compared   
    else:
        tempString1 = ""
        tempString2 = ""
        i = 0
        while i < min(len(base), len(delta)):
            if look_for_same_char and base[i] == delta[i] or look_for_same_char and base[i] != delta[i]:
                tempString1.append(base[i])
                tempString2.append(delta[i])
            elif look_for_same_char and base[i] != delta[i]:
                compared.common.append(tempString1)
                # TODO: figure out how to work this so it breaks appropriately for the given type of sam_char its checking for
                break
            else:
                compared.get('removed').append(tempString1)
                compared.get('added').append(tempString2)
                i += 1
                break
            i += 1
        return stringDiff(base[i:], delta[i:], compared, not 