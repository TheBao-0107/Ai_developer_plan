camera_list = [{"name": "相机", "帧率": 30}]
print(f"{camera_list[0]['name']}：{camera_list[0]['帧率']}fps")

money_spent = {"交通": [2, 3]}
for k in money_spent:
    print(f"{k}：{sum(money_spent[k])}元")

budget_dict = {"餐饮": {"budget": 40}}
for k in budget_dict:
    print(f"{k}预算：{budget_dict[k]['budget']}元")
