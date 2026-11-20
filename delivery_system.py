from typing import Optional


class InvalidOrderOperationError(Exception):
    """自定义异常：订单状态不允许当前操作"""
    pass


class DeliveryOrder:
    """
    外卖订单类，支持订单创建、接单、配送完成、取消
    状态枚举：pending(待接单) → delivering(配送中) → completed(已完成)
              pending → cancelled(已取消)
    """
    VALID_STATUS = {"pending", "delivering", "completed", "cancelled"}

    def __init__(self, order_id: str, customer_name: str, address: str, fee: float):
        if fee < 0:
            raise ValueError("Order fee cannot be negative")
        self.order_id: str = order_id
        self.customer_name: str = customer_name
        self.address: str = address
        self.fee: float = fee
        self.status: str = "pending"

    def accept_order(self) -> None:
        """商家/骑手接单，pending → delivering"""
        if self.status != "pending":
            raise InvalidOrderOperationError(f"Cannot accept order in state {self.status}")
        self.status = "delivering"

    def finish_delivery(self) -> None:
        """配送完成，delivering → completed"""
        if self.status != "delivering":
            raise InvalidOrderOperationError(f"Cannot finish delivery in state {self.status}")
        self.status = "completed"

    def cancel_order(self) -> None:
        """取消订单，仅pending状态允许取消"""
        if self.status != "pending":
            raise InvalidOrderOperationError(f"Cannot cancel order in state {self.status}")
        self.status = "cancelled"

    def __repr__(self) -> str:
        return f"<DeliveryOrder id={self.order_id}, status={self.status}, fee={self.fee}>"