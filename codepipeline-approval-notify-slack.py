import boto3
import json
import logging
import os
import slackweb

SLACK_CHANNEL = os.environ['slackChannel']

HOOK_URL = "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX"
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    message = json.loads(event['Records'][0]['Sns']['Message'])
    logger.info("Message: " + str(message))

    slack = slackweb.Slack(url=HOOK_URL)

    short_message = message['approval']['customData']
    pipeline_link = message['approval']['approvalReviewLink']
    pipeline_name = message['approval']['pipelineName']
    cfn_link = message['approval']['externalEntityLink']
    expires = message['approval']['expires']
    environment = os.environ['environment']

    attachments = []
    attachment = {
            'title': '<%s|APPROVAL NEEDED>' % (pipeline_link),
            'color': 'good',
            'pretext': '*Please review the latest changes and approve or reject*',
            'fields': [
                {
                    'title': 'Environment',
                    'value': '%s' % (environment),
                    'short': 'true'
                },
                {
                    'title': 'Expires at',
                    'value': '%s' % (expires),
                    'short': 'true'
                }],
            'text': '*Pipeline Name:* \n   %s \n *Review:* \n   %s \n *Approval:* \n  %s' % (pipeline_name, cfn_link, pipeline_link),
            'mrkdwn_in': ['title', 'text', 'pretext']
            }
    attachments.append(attachment)
    slack.notify(attachments=attachments)

