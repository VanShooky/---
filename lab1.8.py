import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.arange(0, 6.28, 0.1)
    y = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    line, = ax.plot(x, y)
    line.set_color('pink')
    ax.set_title('sin(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')

    ax.grid(visible=True, color='gray', linestyle='-', linewidth=0.5)

    ax.set_xticks(np.linspace(0, 7, 10))
    ax.set_yticks(np.linspace(y.min(), y.max(), 10))

    plt.show()
    fig.savefig('sin(x).tiff')


if __name__ == "__main__":
    main()
