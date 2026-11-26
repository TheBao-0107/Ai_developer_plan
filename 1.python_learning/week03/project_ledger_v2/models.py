# W3D6：按任务页完成记账本 v2 上半部分，用旅途开销核对明细和分类合计。
# 在下面写你的代码
class Record:
    """开销记录类"""

    def __init__(self, amount, category, note, date):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = date


class Ledger:
    """账单类"""

    def __init__(self, ledger_list=[]):
        self.ledger_list = ledger_list

    def add(self, record):
        """新增一笔开销记录"""
        self.ledger_list.append(record)

    def list_all(self):
        """展示记录列表中所有记录"""
        return self.ledger_list

    def summary_by_category(self):
        """拿到一个字典，键是类别，值是该类别的总金额"""
        category_sum_dict = {}
        for record in self.ledger_list:
            category_sum_dict[record.category] = (
                category_sum_dict.get(record.category, 0) + record.amount
            )
        return category_sum_dict


if __name__ == "__main__":
    record_1 = Record(18, "交通", "去程车票", "2026-11-20")
    record_2 = Record(32, "餐饮", "午饭", "2026-11-20")
    record_3 = Record(12, "交通", "回程地铁", "2026-11-21")
    ledger = Ledger([record_1, record_2])
    ledger.add(record_3)
    record_list_all = ledger.list_all()
    if len(record_list_all) == 0:
        print([])
    for record in record_list_all:
        print(f"{record.date} | {record.category} | {record.amount}元 | {record.note}")
    summary_dict = ledger.summary_by_category()
    if len(summary_dict) == 0:
        print({})
    for category, amount in summary_dict.items():
        print(f"{category}合计 {amount}元")
