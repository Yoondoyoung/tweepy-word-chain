import json
import twitbot
import wordtest


def wordchain(event, context):
    wordtest.wordFinding('가')
    twitbot.tweet_upload()

    body = {
        "message": "tweepy test success!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
