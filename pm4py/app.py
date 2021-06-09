
# %%
import pandas as pd
import pm4py

# importer + converter
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.conversion.process_tree import converter

# algo
from pm4py.algo.discovery.dfg import algorithm as dfg_algo
from pm4py.algo.discovery.inductive import algorithm as inductive_algo

# visualizer
from pm4py.visualization.dfg import visualizer as dfg_vis
from pm4py.visualization.process_tree import visualizer as pt_visualizer
from pm4py.visualization.bpmn import visualizer as bpmn_visualizer


## IMPORT and STATISTIC
log = xes_importer.apply('./ressources/log1.xes')


## DISCOVERY
dfg = dfg_algo.apply(log)
gviz = dfg_vis.apply(dfg,log=log)
dfg_vis.view(gviz)

tree = inductive_algo.apply_tree(log)
gviz = pt_visualizer.apply(tree)
pt_visualizer.view(gviz)

bpmn_graph = converter.apply(tree, variant=converter.Variants.TO_BPMN)
gviz = bpmn_visualizer.apply(bpmn_graph)
bpmn_visualizer.view(gviz)
# %%
