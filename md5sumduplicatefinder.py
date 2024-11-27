with open("md5sum_purged.txt","r",encoding="utf-8") as f:
    lines=f.readlines()
sum=[]
for i in lines:
    sum.append(i[:31])
num=1
top=len(sum)
while num<top:
    for k in range(num+1,top):
        if sum[num]==sum[k]:
            print(f"{num} line'da {lines[num]} oge || {k} linede {lines[k]} de bulundu")
            with open("logss.txt","a") as f:
                f.write(f"{num} line'da {lines[num][:-1]} oge || {k} linede {lines[k][:-1]} de bulundu\n")
    num=num+1
