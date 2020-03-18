import sys
lists = int(sys.stdin.readline().strip())
user_tb_dict={}
for i in range(lists):
    tb_name, user_name = sys.stdin.readline().strip().split()
    user_tb_dict.setdefault(user_name,[])
    user_tb_dict[user_name].append(tb_name)

result = {}

for user in user_tb_dict.keys():
    tb_names = user_tb_dict[user]
    for i in range(len(tb_names)):
        result.setdefault(tb_names[i],{})
        for j in range(len(tb_names)):
            result[tb_names[i]].setdefault(tb_names[j],0)
            result[tb_names[i]][tb_names[j]]+=1
results = []
for i in result.keys():
    for j in result[i].keys():
        if(result[i][j]>2 and i!=j):
            results.append(i+' '+j+' '+str(result[i][j]))
results = sorted(results)
for s in results:
    print(s)