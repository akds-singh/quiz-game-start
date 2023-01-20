from graphviz import Digraph

dot = Digraph()
dot.attr(rankdir='LR', size='8,5')

dot.node('A', 'Start')
dot.node('B', 'Process 1')
dot.node('C', 'Process 2')
dot.node('D', 'End')

dot.edges(['AB', 'BC', 'CD'])

dot.render('flowchart', view=True)