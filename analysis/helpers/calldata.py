def parse_og_calldata(calldata):
    
    result = [calldata[0:10]]

    arg_len = 64

    arg_start_i = 10
    arg_end_i = arg_start_i + arg_len

    while arg_start_i < len(calldata):
        next_arg = calldata[arg_start_i:arg_end_i]
        result.append(next_arg)
        arg_start_i += arg_len
        arg_end_i += arg_len

    return result
