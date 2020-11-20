#!/usr/bin/env python
import argparse
import json

import pandas as pd
import matplotlib.pyplot as plt

"""
Simple plotting program that takes the output from tcpwin and plots a graph similar to Figure 10-5 in BPF Performance Tools
"""

FIGSIZE = (10, 6)
MIN_PLOT_POINTS = 1000
PLOT_SK = True
KWARGS = dict() #{"marker":".","markersize":1}

def plot_cwnd(axes, df, plot_sk=True, alpha=0.5, **kwargs):
    x = df["time_us"].values / 1e6  # Convert x-scale to seconds
    handles = list()
    if plot_sk:
        #Plot sk_sndbuf and sk_wmem_queued on "right" axis"
        axes2 = axes.twinx()
        h3 = axes2.plot(x, df["sk_sndbuf"].values, c="C2", label="sk_sndbuf", alpha=alpha, **kwargs)[0]
        h4 = axes2.plot(x, df["sk_wmem_queued"].values, c="C3", label="sk_wmem_queued", alpha=alpha, **kwargs)[0]
        axes2.set_ylabel("sk_sndbuf, sk_wmem_queued")
        _, yh = axes2.get_ylim()
        axes2.set_ylim(0, 1.15*yh) # Add some extra space for legend
        handles += [h3, h4]

    # Plot snd_cwnd and snd_ssthresh on "left" axis
    h1 = axes.plot(x, df["snd_cwnd"].values, c="C0", label="snd_cwnd", alpha=alpha, **kwargs)[0]
    h2 = axes.plot(x, df["snd_ssthresh"].values, c="C1", label="snd_ssthresh", alpha=alpha, **kwargs)[0]
    axes.set_ylabel("snd_cwnd, snd_ssthresh")
    _, yh = axes.get_ylim()
    axes.set_ylim(0, 1.1*yh) # Add some extra space for legend
    handles = [h1, h2] + handles

    axes.set_xlabel("Time (s)")
    axes.legend(handles, [h.get_label() for h in handles], ncol=len(handles)//2, loc="upper right")
    return axes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot a csv-file from tcpwin.bt")
    parser.add_argument("file", help="CSV-file to plot")
    parser.add_argument("-p", "--plot_sk", help="In addition to cwnd and ssthresh, plot sndbuf and wmem_queued",
                        action="store_true")
    parser.add_argument("-n", "--min_points", default=1000, type=int, help="Minimum number of data-points for socket to plot it")
    parser.add_argument("-fw", "--width", default=10, type=float, help="Figure width (in inches)")
    parser.add_argument("-fh", "--height", default=6, type=float, help="Figure height (in inches)")
    parser.add_argument("-k", "--kwargs", default="{}", type=json.loads, help="Additional plotting kwargs")
    args = parser.parse_args()

    df = pd.read_csv(args.file, header=1);
    for socket, socket_df in df.groupby("sock"):
        if len(socket_df) >= args.min_points:
            print("Plotting {} points for socket {}".format(len(socket_df), socket))
            fig, axes = plt.subplots(1, 1, figsize=(args.width, args.height))
            plot_cwnd(axes, socket_df, args.plot_sk, **args.kwargs)
            axes.set_title("Socket: {} - {} points".format(socket, len(socket_df)))
            plt.show()
                
