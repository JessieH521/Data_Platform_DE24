import matplotlib.pyplot as plt

def line_chart(x, y, **options):
    fig, ax = plt.subplots(1)

    ax.plot(x, y, linewidth=4)    # 绘制折线图，线宽 4
    ax.set(**options)             
    # 设置标题、标签等参数（通过可选参数 options）根据 options 传入的字典自动设置参数，但如 options 为空，不会有任何内容

    fig.tight_layout()            # 自动调整子图布局，防止重叠
    return fig
 




















