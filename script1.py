org_msg =[["hi" ,"how are you?"],['10','hello!']]
import copy
shal_cpy=copy.copy(org_msg)
shal_cpy[0]=['hey']
print(shal_cpy)



org_msg =[["hi" ,"how are you?"],['10','hello!']]
import copy
deep_cpy=copy.deepcopy(org_msg)
deep_cpy[0]=['hey']
print(deep_cpy)
print(org_msg)