#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_datalake.aws_cdk_datalake_stack import AwsCdkDatalakeStack


app = cdk.App()
AwsCdkDatalakeStack(app, "AwsCdkDatalakeStack")

app.synth()
