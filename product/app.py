# Define your inputs, transformations and outputs here!

from infrastructure import MyAwesomeStack
import pandas as pd

# Import data from input_port
data = MyAwesomeStack.input_port.read(format="parquet")

MyAwesomeStack.output_port.upload(data.to_parquet('revenue_doubled.parquet'))