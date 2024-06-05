import re
# http.request.full_uri contains "flag"
# tshark.exe -r .\SQL盲注.pcap -Y "http.request.full_uri contains flag" > out.txt
with open('./out.txt', encoding='utf-8') as f:
    tmp = f.read()
    flag = ''
    data = re.findall(r'=(\d*)%23',tmp)
    data = [int(i) for i in data]
    for i,num in enumerate(data):
        try:
            if num > data[i+1]:
                flag += chr(num)
        except Exception:
            pass
    print(flag)