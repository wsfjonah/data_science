import reporting.services.echarts.base_axis as base_axis


class FriendsCookieProj:
    chart = base_axis.BaseAxis('Data Chart', 'Name', 'Cookies', width=900, height=400, main_chart_type='bar')
    
    def __init__(self):
        pass
    
    def add_friends(self, friends):
        self.chart.set_x_axis(friends)
        
    def add_cookies(self, cookies):
        self.chart.add_y_axis(cookies)
        
    def get_output(self):
        return self.chart.get_chart()

