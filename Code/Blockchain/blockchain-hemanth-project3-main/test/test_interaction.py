import etherscan
import sys
from const import *

eth = etherscan.Etherscan(API_KEY, net="ropsten")
with open(sys.argv[1]) as f:
    student_addr = f.read().strip().lower()
    if len(student_addr) == 0:
        print("no address provided")
    else:
        res = eth.get_internal_txs_by_address(CONTRACT, 10308757, 'latest', 'asc')
        to_contract = [obj for obj in res if (obj['from'] == str(student_addr))]
        from_contract = list(filter(lambda x: x['from'] == CONTRACT.lower() and x['to'] == str(student_addr), res))

        if len(to_contract) > 0 and len(from_contract) > 0:
            print("passed")
        else:
            print("no contract interaction")
            print('To contract (%d tx): %s' % (len(to_contract), to_contract))
            print('From contract (%d tx): %s ' % (len(from_contract), from_contract))
