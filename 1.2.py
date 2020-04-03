my_list=get_n_random_numbers(5,-3,3)
my_hist_d=my_frequency_with_dict(my_list)
my_hist_list=my_frequency_with_list_of_tuples(my_list)


def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        #print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max

def my_mode_with_list(my_hist_list):
    frequency_max=-1
    mode=-1
    for item,frequency in my_hist_list:
        #print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
    return mode,frequency_max


print my_mode_with_list(my_hist_list)
