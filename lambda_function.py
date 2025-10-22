import json
import boto3

# Initialize the Amazon Translate client
translate = boto3.client('translate')

def lambda_handler(event, context):
    try:
        # 1. Parse the incoming request body
        # The ALB sends the body as a JSON string
        body = json.loads(event['body'])
        original_text = body['text']
        target_code = body['target_language_code']

        # 2. Call the Amazon Translate API
        response = translate.translate_text(
            Text=original_text,
            SourceLanguageCode='auto',  # Auto-detect the source language
            TargetLanguageCode=target_code
        )

        # 3. Format the successful response
        translated_text = response['TranslatedText']
        source_code = response['SourceLanguageCode']

        response_body = {
            'original_text': original_text,
            'translated_text': translated_text,
            'source_language_code': source_code,
            'target_language_code': target_code
        }

        # 4. Return a proper HTTP response for the ALB
        return {
            'statusCode': 200,
            'statusDescription': '200 OK',
            'isBase64Encoded': False,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps(response_body)
        }

    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'statusDescription': '500 Internal Server Error',
            'isBase64Encoded': False,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'error': 'Failed to process translation.'})
        }