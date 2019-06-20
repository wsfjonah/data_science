from mpl_toolkits.mplot3d import Axes3D
import reporting.services.chart.base_chart as base_chart

'''
X = [1,2,3]  # coordinates of each bar
Y = [2,4,0]  # coordinates of each bar
Z = [0,0,0]  # coordinates of each bar
dx = [0.5, 0.5, 0.5]  #width of each bar
dy = [0.5, 0.5, 0.5]  #depth of each bar
dz = [5, 4, 7]        #height of each bar
'''


class Bar3DChart(base_chart.BaseChart):
    directions = [[30, 30], [10, 10], [10, -80], [90, -90]]
    width = 2
    depth = 0.5
    color = 'lightblue'
    label_z = ''

    def __init__(self, title, label_x, label_y, label_z):
        base_chart.BaseChart.__init__(self, title, label_x, label_y, win_x=20, win_y=20)
        self.label_z = label_z
        self.fig.suptitle(title, fontsize=20)

    def set_data(self, **data):
        if ('x' in data) & ('y' in data) & ('z' in data):
            self.data = [[[], [], [], [], [], []]]  # X, Y, Z, dx, dy, dz

            index = 0
            for k in data['x']:
                self.data[0][0].append(k)
                self.data[0][1].append(data['y'][index])
                self.data[0][2].append(0)
                self.data[0][3].append(self.width)
                self.data[0][4].append(self.depth)
                self.data[0][5].append(data['z'][index])
                index += 1
        else:
            raise Exception("Input Data Set need to have data list x, y, z")
        return self

    def get_multi_plotter(self, pos):
        axes = self.fig.add_subplot(221+pos, projection='3d')
        axes.view_init(elev=self.directions[pos][0], azim=self.directions[pos][1])
        # axes.set_title(self.title, fontsize=20)
        axes.set_xlabel(self.label_x)
        axes.set_ylabel(self.label_y)
        axes.set_zlabel(self.label_z)
        return axes

    def plot(self):
        self.get_multi_plotter(0).bar3d(self.data[0][0], self.data[0][1], self.data[0][2], self.data[0][3], self.data[0][4], self.data[0][5], color=self.color, label=self.label_z)
        self.get_multi_plotter(1).bar3d(self.data[0][0], self.data[0][1], self.data[0][2], self.data[0][3], self.data[0][4], self.data[0][5], color=self.color, label=self.label_z)
        self.get_multi_plotter(2).bar3d(self.data[0][0], self.data[0][1], self.data[0][2], self.data[0][3], self.data[0][4], self.data[0][5], color=self.color, label=self.label_z)
        self.get_multi_plotter(3).bar3d(self.data[0][0], self.data[0][1], self.data[0][2], self.data[0][3], self.data[0][4], self.data[0][5], color=self.color, label=self.label_z)
        return self
