import k3d
import os


def generate():
    filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            '../assets/arcade_carpet_512.png')

    with open(filepath, 'rb') as stl:
        data = stl.read()

    plt_texture = k3d.texture(data,
                              file_format='png')

    plot = k3d.plot()
    plot += plt_texture

    plot.snapshot_type = 'inline'
    return plot.get_snapshot()
