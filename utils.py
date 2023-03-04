def retrieve_edge_list_from_file(fname):
    with open(fname, 'r') as f:
        raw_data = f.read()
    edge_list = [tuple(data.split('\t')) for data in raw_data.split('\n')]
    return [(int(edge[0]), int(edge[1])) for edge in edge_list]