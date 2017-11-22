import networkx as nx

from IPython.display import Image

def draw_dot(graph, file):
    """
    Writes a graph to png using pydot and returns that file
    as an IPython Image object
    IPython.display.Image
    
    Arguments:
        graph: a NetworkX graph
        file: a file name to save png file to
    """
    if not file.endswith(".png"):
        file = file+".png"
    ag = nx.nx_pydot.to_pydot(graph)
    ag.write_png(file)
    return Image(filename=file)