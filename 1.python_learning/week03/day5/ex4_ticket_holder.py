# 可选挑战：把一张车票装入票夹，展示持票人和票面文字。
# 在下面写你的代码
from ex1_tickets import Ticket
from ex2_ticket_desk import SleeperTicket


class TicketHolder:
    """票夹类"""

    def __init__(self, destination, name, place=None):
        self.name = name
        if place:
            self.ticket = SleeperTicket(destination, place)
        else:
            self.ticket = Ticket(destination)

    def ticket_holder_label(self):
        """生成展示文字"""
        return f"{self.name}的票夹｜{self.ticket.label()}"


print(TicketHolder("西安", "小林", "上铺").ticket_holder_label())
