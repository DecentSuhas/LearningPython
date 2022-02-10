# import openpyxl module
import openpyxl

# import BarChart class from openpyxl.chart sub_module
from openpyxl.chart import LineChart, Reference

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()

# Get workbook active sheet
# from the active attribute.
sheet = wb.active

# write o to 9 in 1st column of the active sheet
for i in range(10):
    sheet.append([i])

# create data for plotting
values = Reference(sheet, min_col=1, min_row=1,
                   max_col=1, max_row=10)

# Create object of BarChart class
chart = LineChart()

# adding data to the Bar chart object
chart.add_data(values)

# set the title of the chart
chart.title = " LINE-CHART "

# set the title of the x-axis
chart.x_axis.title = " X_AXIS "

# set the title of the y-axis
chart.y_axis.title = " Y_AXIS "

# add chart to the sheet
# the top-left corner of a chart
# is anchored to cell E2 .
sheet.add_chart(chart, "E2")

# save the file
wb.save("sample2.xlsx")