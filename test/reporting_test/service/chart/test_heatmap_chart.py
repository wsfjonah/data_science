from matplotlib import pyplot as plt
from matplotlib import cm
import pylab

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文乱码
pylab.mpl.rcParams['axes.unicode_minus'] = False  # 防止中文乱码


def draw_heatmap(data, xlabels, ylabels):
    cmap = cm.Blues
    figure = plt.figure(facecolor='w')
    ax = figure.add_subplot(2, 1, 1, position=[0.1, 0.15, 0.8, 0.8])
    ax.set_yticks(range(len(ylabels)))
    ax.set_yticklabels(ylabels)
    ax.set_xticks(range(len(xlabels)))
    ax.set_xticklabels(xlabels)
    vmax = data[0][0]
    vmin = data[0][0]
    for i in data:
        for j in i:
            if j > vmax:
                vmax = j
            if j < vmin:
                vmin = j
    map = ax.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=vmin, vmax=vmax)
    cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
    plt.xticks(rotation=90)  # 将字体进行旋转
    plt.yticks(rotation=360)
    plt.show()


a = [[1063620, 291288, 213322, 120233, 972752, 1896180, 483012, 1609664, 413538, 778350, 420643, 212472, 2599510,
      1574470, 254141],
     [258914, 48064, 31948, 19534, 142792, 295841, 69143, 291524, 78926, 90238, 79336, 47938, 454656, 271486, 35304],
     [517687, 135483, 68418, 66670, 301544, 777798, 307562, 810314, 234086, 238859, 145959, 125258, 1480672, 764612,
      153237],
     [277377, 38581, 31145, 17612, 121162, 254534, 60746, 253148, 62054, 93499, 63346, 36422, 356036, 212109, 27758],
     [19030, 2835, 2174, 1575, 7325, 18258, 6837, 23457, 5340, 5277, 5120, 4017, 34122, 21314, 2961],
     [351720, 107299, 57186, 55485, 337368, 563436, 188368, 563515, 128047, 178664, 117886, 72451, 798121, 444825,
      65599]]

xlabels = [u'3C电子', u'房产家居', u'服饰', u'健康保健', u'金融财经', u'旅游', u'美容美体', u'汽车', u'求职&教育', u'奢侈品', u'体育健身', u'网游', u'休闲&爱好',
           u'影视娱乐', u'孕婴育儿']
ylabels = ['iphoneX', 'mix2', 'oppor11', 'samsang', 'vivo', 'mate10']
draw_heatmap(a, xlabels, ylabels)