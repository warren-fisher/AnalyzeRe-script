import sys 

threshold, limit = float(sys.argv[1]), float(sys.argv[2])

currSum = 0

out = []

# Maximum of 100 inputs
while len(out) < 100: 
    in_val = input()
    # ASSUMPTION: There will be an empty line once inputs are done
    # If we have an empty input we assume that means the user is done
    if in_val == "":
        break 
    
    in_val = float(in_val)
    
    # If we are less than threshold or we reached our limit, output 0
    if in_val < threshold or currSum == limit:
        out.append(0)
    # we don't reach the limit yet
    elif (currSum + in_val) <= limit: 
        currSum += in_val
        out.append(in_val)
    else:
        # We reached out maximum sum, limit
        # output the remaining needed and set our current sum to limit
        out.append(limit-currSum)
        currSum = limit
    
# print our out values
for i in out:
    print(i)

# now finally print our sum
print(currSum)