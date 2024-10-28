# Use this to setup the required infrastructure for your data product
import os
from dotenv import load_dotenv

load_dotenv()

from constructs import Construct

from ecp_cdk.core import (
  Stack,
  DataProduct
)

from ecp_cdk.azure.io import Blob
from ecp_cdk.utils import load_spec


class MyAwesomeStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    # Create data_product from spec
    spec = load_spec(os.environ("PRODUCT_SPEC_PATH"))
    self.data_product = DataProduct.from_spec(spec)

    # IO ports
    self.input_port = Blob(
      id="revenue",
      owner="finance",
      port="input",
      key="revenue.parquet"
    )
    
    self.output_port = Blob(
      id="revenue-projection",
      owner="finance",
      port="output",
      accepts=["parquet", "avro"],
    )

    # Adding ports to data product
    self.data_product.add_input(self.input_port)
    self.data_product.add_output(self.output_port)

