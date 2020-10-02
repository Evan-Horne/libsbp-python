import io
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
from matplotlib import style
from sbp.client import Handler, Framer
from sbp.client.drivers.file_driver import FileDriver
from sbp.navigation import SBP_MSG_BASELINE_NED, SBP_MSG_GPS_TIME, SBP_MSG_POS_LLH_GNSS


def main():
    tow = []
    hacc = []
    plt.xlabel('TOW - Time of Week')
    plt.ylabel('Horizontal Acceleration')
    swiftBinary = open('28-220741.sbp', 'rb')
    filestream = FileDriver(swiftBinary)
    with Handler(Framer(filestream.read, None, verbose=True), autostart=True) as src:
        try:
            for msg, meta in src.filter(SBP_MSG_POS_LLH_GNSS):
                tow.append(msg.tow)
                hacc.append(msg.h_accuracy)
        except KeyboardInterrupt:
            pass
    plt.plot(tow, hacc)
    plt.xlim(min(tow), max(tow))
    plt.ylim(min(hacc), max(hacc))
    plt.show()


if __name__ == '__main__':
    main()


