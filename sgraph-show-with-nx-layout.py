import networkx as nx
g = nx.Graph()

# put the nodes and edges from the SGraph into a NetworkX graph
g.add_nodes_from(list(sg.vertices['__id']))
g.add_edges_from([(e['__src_id'], e['__dst_id']) for e in sg.edges])

# create the layout with NetworkX and convert to regular Python types
# you can substitute any of the layout algorithms here for circular_layout:
# http://networkx.github.io/documentation/latest/reference/drawing.html#module-networkx.drawing.layout
layout = nx.circular_layout(g)
layout = {k: map(float, list(v)) for k,v in layout.iteritems()}

# show the SGraph in Canvas with that layout
sg.vertices['x'] = sg.vertices.apply(lambda v: layout[v['__id']][0])
sg.vertices['y'] = sg.vertices.apply(lambda v: layout[v['__id']][1])
sg.show(vertex_positions=('x', 'y'))
