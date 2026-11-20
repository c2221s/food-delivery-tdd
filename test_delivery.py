import pytest
from delivery_order import DeliveryOrder, InvalidOrderOperationError


def test_order_initial_state():
    """测试订单初始化默认状态为pending"""
    order = DeliveryOrder("O001", "Alice", "10 Main St", 18.5)
    assert order.status == "pending"
    assert order.fee == 18.5
    assert order.customer_name == "Alice"


def test_accept_order_success():
    """成功接单：pending → delivering"""
    order = DeliveryOrder("O002", "Bob", "22 Park Rd", 25.0)
    order.accept_order()
    assert order.status == "delivering"


def test_finish_delivery_success():
    """成功完成配送：delivering → completed"""
    order = DeliveryOrder("O003", "Charlie", "5 Lake Ave", 12.0)
    order.accept_order()
    order.finish_delivery()
    assert order.status == "completed"


def test_cancel_pending_order_success():
    """待接单订单可以取消"""
    order = DeliveryOrder("O004", "David", "7 Hill St", 22.0)
    order.cancel_order()
    assert order.status == "cancelled"


def test_accept_already_cancelled_order_raise_error():
    """已取消的订单不能接单，抛异常"""
    order = DeliveryOrder("O005", "Ella", "1 Ocean Rd", 15.0)
    order.cancel_order()
    with pytest.raises(InvalidOrderOperationError):
        order.accept_order()


def test_cancel_delivering_order_raise_error():
    """配送中订单不能取消"""
    order = DeliveryOrder("O006", "Frank", "8 River Ln", 30.0)
    order.accept_order()
    with pytest.raises(InvalidOrderOperationError):
        order.cancel_order()


def test_finish_pending_order_raise_error():
    """待接单订单不能直接标记完成"""
    order = DeliveryOrder("O007", "Grace", "9 Sunny Ave", 10.0)
    with pytest.raises(InvalidOrderOperationError):
        order.finish_delivery()


def test_negative_fee_raise_value_error():
    """订单金额不能为负数，初始化校验"""
    with pytest.raises(ValueError):
        DeliveryOrder("O008", "Henry", "3 Green St", -5.0)