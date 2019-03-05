# pip3 install bokeh
# pip3 install ipython

# Import modules
from bokeh.plotting import figure, output_notebook, show

# output the notebook
output_notebook()

# Create figure
p = figure(plot_width = 400, plot_height = 400)

# Add a line renderer
p.line([1,2,3,4,5], [3,1,2,6,5], line_width = 2, color = "green")

# Show results
show(p)