import sys

N= int(sys.stdin.readline())

ip = []
for i in range(N):
    a,b,c,d = map(int,sys.stdin.readline().split("."))
    ip.append([a,b,c,d])

netmask = []
address_min = []
flag = True
for j in range(4):
    if flag:
        min_ip = int(ip[0][j])
        max_ip = int(ip[0][j])
        for check in ip:
            if max_ip < check[j]:
                max_ip = check[j]
            if min_ip > check[j]:
                min_ip = check[j]

        if min_ip == max_ip:
            netmask.append(255)
            address_min.append(min_ip)

        else:
            bin_min = format(min_ip, 'b')
            bin_max = format(max_ip, 'b')

            # 8bit 맞춰주기
            if len(bin_min) < 8:
                zero = ''
                for z in range(8-len(bin_min)):
                    zero += "0"
                bin_min = zero + bin_min
            if len(bin_max) < 8:
                zero = ''
                for z in range(8-len(bin_max)):
                    zero += "0"
                bin_max = zero + bin_max

            temp_net_ip = ''
            for h in range(8):
                if bin_min[h] == bin_max[h]:
                    temp_net_ip += (bin_min[h])
                else:
                    zero_point = "0" * (8-h)
                    temp_net_ip += zero_point
                    address_min.append(int(temp_net_ip, 2))
                    netmask.append(256-(2 ** (8-h)))
                    flag = False
                    break
    else:
        netmask.append(0)
        address_min.append(0)

print('.'.join(map(str, address_min)))
print('.'.join(map(str, netmask)))