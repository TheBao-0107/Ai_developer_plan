# 可选挑战：逐笔创建独立字典形成账目草稿，修改草稿后验证原账不变。
# 在下面写你的代码
money_dict_list = [{"amount": 3}, {"amount": 12}]
new_money_dict_list = []
for money_dict in money_dict_list:
    new_money_dict = {}
    for k,v in money_dict.items():
        new_money_dict[k] = v
    new_money_dict_list.append(new_money_dict)
new_money_dict_list[0]['amount'] = 5
for money_dict in money_dict_list:
    print(f"原账：{money_dict["amount"]}元")

for money_dict in new_money_dict_list:
    print(f"草稿：{money_dict["amount"]}元")