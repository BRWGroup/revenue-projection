import os
from dotenv import load_dotenv

load_dotenv()

import ecp_cdk
from ecp_cdk.utils import load_spec

from product.infrastructure import MyAwesomeStack

spec = load_spec(os.environ("PRODUCT_SPEC_PATH"))
app = ecp_cdk.App()
MyAwesomeStack(app, f"MyAwesomeStack",)

app.synth()