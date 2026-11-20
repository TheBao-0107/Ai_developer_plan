# 两张行李取件单：用函数生成取件单，更新第一张后查看两张单子。
# 在下面写你的代码
def claim_tickets(cabinet, number):
    """返回接收柜和行李件数这两项信息组成的字典"""
    return {"柜号": cabinet, "行李件数": number}


claim_tickets_list = []
claim_tickets_list.append(claim_tickets("A03", 1))
claim_tickets_list.append(claim_tickets("B12", 2))
claim_tickets_list[0]["行李件数"] = 3
for claim_ticket in claim_tickets_list:
    print(f"{claim_ticket['柜号']} 柜：{claim_ticket['行李件数']} 件")
