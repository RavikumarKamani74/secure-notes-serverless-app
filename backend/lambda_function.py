import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserNotes')

def lambda_handler(event, context):
    method = event.get('httpMethod')
    headers = {
        "Access-Control-Allow-Origin": "*",  # CORS header
        "Access-Control-Allow-Methods": "OPTIONS,GET,POST,PUT,DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    if method == 'OPTIONS':
        # Preflight CORS request
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps({'message': 'CORS preflight'})
        }
    
    try:
        if method == 'GET':
            # Scan and return all notes
            response = table.scan()
            notes = response.get('Items', [])
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'notes': notes})
            }
        
        elif method == 'POST':
            # Create a new note
            body = json.loads(event.get('body') or '{}')
            note_id = body.get('NoteId')
            content = body.get('content')
            
            if not note_id or not content:
                raise ValueError("Missing NoteId or content")
            
            table.put_item(Item={'NoteId': note_id, 'content': content})
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Note saved successfully!'})
            }
        
        elif method == 'PUT':
            # Update an existing note
            note_id = event['pathParameters'].get('id') if event.get('pathParameters') else None
            body = json.loads(event.get('body') or '{}')
            content = body.get('content')
            
            if not note_id or not content:
                raise ValueError("Missing NoteId or content for update")
            
            # Update the note content
            table.update_item(
                Key={'NoteId': note_id},
                UpdateExpression='SET content = :val1',
                ExpressionAttributeValues={':val1': content}
            )
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Note updated successfully!'})
            }
        
        elif method == 'DELETE':
            # Delete a note
            note_id = event['pathParameters'].get('id') if event.get('pathParameters') else None
            
            if not note_id:
                raise ValueError("Missing NoteId for delete")
            
            table.delete_item(Key={'NoteId': note_id})
            return {
                'statusCode': 200,
                'headers': headers,
                'body': json.dumps({'message': 'Note deleted successfully!'})
            }
        
        else:
            return {
                'statusCode': 405,
                'headers': headers,
                'body': json.dumps({'message': f'Method {method} not allowed'})
            }
        
    except Exception as e:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps({'message': str(e)})
        }
