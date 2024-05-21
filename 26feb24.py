import graphviz

# Create a new graph
graph = graphviz.Digraph()

# Add nodes to the graph
graph.node('data_collection', label='Data Collection')
graph.node('data_integration', label='Data Integration')
graph.node('model_training', label='Model Training')
graph.node('prediction', label='Prediction')
graph.node('monitoring_debugging', label='Monitoring & Debugging')

# Add edges to connect the nodes
graph.edge('data_collection', 'data_integration')
graph.edge('data_integration', 'model_training')
graph.edge('model_training', 'prediction')
graph.edge('model_training', 'monitoring_debugging')

# Render and save the graph as an image file
graph.render('machine_learning_flowchart', format='png')
