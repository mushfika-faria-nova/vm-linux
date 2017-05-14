def string_split():

    data='X-DSPAM-Confidence:0.8475'

    pos=data.find(':')

    print(pos)

    res=data[pos+1:]

    print(res)

    final_output=float(res)

    print('output: ', final_output)

    return final_output

string_split()
