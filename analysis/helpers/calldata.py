from web3 import Web3

def parse_og_calldata(calldata):
    
    result = {'method': calldata[0:10]}

    args = []

    arg_len = 64

    arg_start_i = 10
    arg_end_i = arg_start_i + arg_len

    while arg_start_i < len(calldata):
        next_arg = calldata[arg_start_i:arg_end_i]
        args.append(next_arg)
        arg_start_i += arg_len
        arg_end_i += arg_len

    result['args'] = args

    return result


def parse_bot_calldata(calldata):
    result = {}
    result['method'] = calldata[0:10]
    result['target_contract'] = calldata[10:50]
    result['og_calldata_length'] = calldata[50: 58]
    result['og_calldata'] = calldata[58:(58 + Web3.toInt(hexstr=result['og_calldata_length']) * 2)]
    return result
