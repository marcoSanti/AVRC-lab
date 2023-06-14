def retrieve_edge_list_from_file(fname):
    edge_list = []
    with open(fname, 'r') as f:
        edge_list = [tuple(map(int, line.split())) for line in f.readlines()]
    return edge_list
