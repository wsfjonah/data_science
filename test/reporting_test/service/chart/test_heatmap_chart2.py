import reporting.services.chart.heatmap_chart as heatmap_chart
import reporting.services.echarts.heatmap_echarts as heatmap_echarts


heatmap = [[1063620, 291288, 213322, 120233, 972752, 1896180, 483012, 1609664, 413538, 778350, 420643, 212472, 2599510,
      1574470, 254141],
     [258914, 48064, 31948, 19534, 142792, 295841, 69143, 291524, 78926, 90238, 79336, 47938, 454656, 271486, 35304],
     [517687, 135483, 68418, 66670, 301544, 777798, 307562, 810314, 234086, 238859, 145959, 125258, 1480672, 764612,
      153237],
     [277377, 38581, 31145, 17612, 121162, 254534, 60746, 253148, 62054, 93499, 63346, 36422, 356036, 212109, 27758],
     [19030, 2835, 2174, 1575, 7325, 18258, 6837, 23457, 5340, 5277, 5120, 4017, 34122, 21314, 2961],
     [351720, 107299, 57186, 55485, 337368, 563436, 188368, 563515, 128047, 178664, 117886, 72451, 798121, 444825,
      65599]]

data_x = [u'3C电子', u'房产家居', u'服饰', u'健康保健', u'金融财经', u'旅游', u'美容美体', u'汽车', u'求职&教育', u'奢侈品', u'体育健身', u'网游', u'休闲&爱好',
           u'影视娱乐', u'孕婴育儿']
data_y = ['iphoneX', 'mix2', 'oppor11', 'samsang', 'vivo', 'mate10']

print(len(data_x))
print(len(data_y))

print(len(heatmap))
print(len(heatmap[0]))

chart = heatmap_chart.HeatMapChart('Data Chart', 'X bar', 'Y bar', 'Z')
chart.set_data(x=data_x, y=data_y, map=heatmap)
chart.plot().show()

chart = heatmap_echarts.HeatMapChart('Data Chart', 'X bar', 'Y bar')
chart.set_data(x=data_x, y=data_y, map=heatmap)
chart.plot().show().render()

