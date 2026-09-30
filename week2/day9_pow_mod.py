def power_mod(base,exp,mod):
    if exp==0:
        return 1%mod
    return (base*power_mod(base,exp-1,mod))%mod

print(power_mod(2,10,1000))   #24
