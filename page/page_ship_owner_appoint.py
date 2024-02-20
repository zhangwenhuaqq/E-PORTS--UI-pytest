import page
from base.base import Base
from tools.get_yaml import *
import time
data = get_read(get_file_path('page_data','page_ship_owner_appoint.yaml'))

class PageShipOwnerAppint(Base):
    #点击点击委托方按钮
    def page_click_appoint(self):
        self.base_click(data[0]["type"],data[0]["element"])
    #点击点击确认委托按钮
    def page_click_appoint_confirm(self):
        self.base_click(data[1]["type"],data[1]["element"])
    #勾选付款协议
    def page_click_pay(self):
        self.base_click(data[2]["type"],data[2]["element"])
    #勾选服务条款
    def page_click_service(self,):
        self.base_click(data[3]["type"],data[3]["element"])
    #点击提交按钮
    def page_click_submit(self,):
        self.base_click(data[4]["type"],data[4]["element"])
    #点击查看订单详情
    def page_order_detial(self,):
        self.base_click(data[5]["type"],data[5]["element"])
    #截图
    def page_get_image(self):
        self.base_get_image()
    #判断”已委托“按钮存在
    def page_is_appoint_success(self):
        return self.base_element_is_exist(data[6]["type"], data[6]["element"])

    #组合业务方法
    def add_ship_owner_appoint(self):
        time.sleep(2)
        self.page_click_appoint()
        time.sleep(2)
        self.page_click_appoint_confirm()
        time.sleep(2)
        self.page_click_pay()
        time.sleep(2)
        self.page_click_service()
        time.sleep(2)
        self.page_click_submit()
        time.sleep(2)
        self.page_order_detial()

# if __name__=='__main__':
#     login=PageLogin()
