import plotly.graph_objects as go
import plotly.io as pio

# Data from the JSON
months = ["Mar", "Apr", "May", "Jun", "Jul", "Aug"]
ai_tech_data = [1, 1, 0, 1, 2, 1]
product_ux_data = [2, 2, 3, 1, 0, 1]
substack_data = [1, 1, 0, 0, 0, 0]

# Use exact colors specified in user instructions
ai_tech_color = "#2B5722"  # dark green
product_ux_color = "#3D3B3B"  # dark gray
substack_color = "#FF5900"  # orange

# Create stacked bar chart
fig = go.Figure()

# Add each series as a bar trace with cliponaxis=False
fig.add_trace(go.Bar(
    name="AI & Tech",
    x=months,
    y=ai_tech_data,
    marker_color=ai_tech_color,
    cliponaxis=False
))

fig.add_trace(go.Bar(
    name="Product & UX", 
    x=months,
    y=product_ux_data,
    marker_color=product_ux_color,
    cliponaxis=False
))

fig.add_trace(go.Bar(
    name="Substack-Spec",
    x=months, 
    y=substack_data,
    marker_color=substack_color,
    cliponaxis=False
))

# Update layout for stacked bars with white background
fig.update_layout(
    title="Themes We Explore",
    barmode='stack',
    xaxis_title="Months",
    yaxis_title="Count",
    plot_bgcolor='white',
    paper_bgcolor='white',
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=1.05, 
        xanchor='center', 
        x=0.5
    )
)

# Save the chart
fig.write_image("themes_stacked_bar.png")