#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import (
    App,
    Environment
)


from cdk_workshop.pipeline_stack import WorkshopPipelineStack

app = cdk.App()
WorkshopPipelineStack(app, "WorkshopPipelineStack")


app.synth()