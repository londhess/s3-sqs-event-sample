from aws_cdk import (
    aws_s3 as s3,
    aws_s3_notifications as aws_s3_notifications,
    aws_sqs as sqs,
    core
    )


class S3SqsEventSampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        bucket = s3.Bucket(self,"ssl_s3_bucket_raw")

        queue = sqs.Queue(self,"ssl_sqs_event_queue")
        #queue.grant()
        notification = aws_s3_notifications.SqsDestination(queue)
        filter1=s3.NotificationKeyFilter(prefix="home/")
        bucket.add_event_notification(s3.EventType.OBJECT_CREATED,notification,filter1)
        