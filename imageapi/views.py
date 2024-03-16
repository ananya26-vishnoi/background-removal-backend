import base64
import requests
from rest_framework.decorators import api_view
import string
import base64
import random
from rest_framework.response import Response
from rest_framework import status
import os
from dotenv import load_dotenv
load_dotenv()

@api_view(['POST'])
def upload_and_remove_background(request):
        try:
            image = request.FILES['image'].read()
            image = b'\n' + image
            dd = image.hex()
            data = bytes.fromhex(dd[2:])  
            random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path = 'media/' + random_name + '.jpg'
            with open(path, 'wb') as file:
                file.write(data)  

            # Use remove.bg API to remove the background
            api_key = 'Tb94jCjUMck7bngZHmNFcPyn'
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                headers={'X-Api-Key': api_key},
                files={'image_file': open(path, 'rb')},
            )

            # Check if the API call was successful
            if response.status_code == 200:
                # Encode the image content as base64
                image_content_base64 = base64.b64encode(response.content).decode('utf-8')

                # save this image to the media folder
                with open(path, 'wb') as file:
                    file.write(response.content)

                # Provide the base64-encoded image content in the response
                result = {'success': True, 'image': image_content_base64, 'url' : os.getenv('BASE_URL') + "/"+path}
                return Response(result, status=status.HTTP_200_OK)
            else:
                print(response.content)
                result = {'success': False, 'error': 'Failed to remove background.'}
                return Response(result, status=status.HTTP_400_BAD_REQUEST)
            

        except Exception as e:
            print(e)
            result = {'success': False, 'error': e}
            return Response(result, status=status.HTTP_400_BAD_REQUEST)