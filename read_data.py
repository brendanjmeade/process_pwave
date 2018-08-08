import h5py
import matplotlib.pyplot as plt
import numpy as np

LINE_WIDTH = 0.5


def plot_time_series(data, idx):
    ''' Extract and plot a single time series '''
    time_series = data['X'].value[idx, :]
    time_vec = np.linspace(-3.0, 3.0, time_series.size)
    label = data['sncls'].value[idx].decode('UTF-8')
    magnitude = data['mag'].value[idx]

    plt.figure(figsize=(12, 6))
    plt.fill([0, 3, 3, 0], [-1, -1, 1, 1], c=[0.85, 0.85, 0.85])
    plt.plot(time_vec, time_series, '-b', linewidth=LINE_WIDTH)
    plt.xlabel(r'$\Delta \; \mathrm{time} \; \mathrm{(s)}$')
    plt.ylabel('normalized acceleration')
    plt.title(label + ', M=' + str(magnitude))
    plt.xlim(-3, 3)
    plt.ylim(-1.0, 1.0)
    plt.xticks(np.arange(-3, 3.5, 0.5))
    plt.yticks([-1, 0, 1])
    plt.show(block=False)
    plt.savefig(label + '.pdf')


def main():
    ''' Read and plot Zach Ross data '''
    data = h5py.File('scsn_p_2000_2017_6sec_0.5r_pick_train.hdf5')
    plot_time_series(data, 1)


if __name__ == "__main__":
    main()
