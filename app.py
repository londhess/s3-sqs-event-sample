#!/usr/bin/env python3

from aws_cdk import core

from s3_sqs_event_sample.s3_sqs_event_sample_stack import S3SqsEventSampleStack


app = core.App()
S3SqsEventSampleStack(app, "s3-sqs-event-sample",  env={'region': 'ap-south-1'})

app.synth()
