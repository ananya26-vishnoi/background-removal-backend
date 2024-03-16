import base64
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from PIL import Image

BITLY_ACCESS_TOKEN = '2e5e5bb79324c5410a16b19df7b34dc97a8c6c04'  # Replace with your Bitly access token

@api_view(['POST'])
def upload_and_remove_background(request):
            uploaded_image = request.data['image']
            print(uploaded_image)
            
            image = Image.open("file_path.jpeg")

                # Process the image as needed
                # For example, you can resize the image:
            resized_image = image.resize((400, 500))

                # Save or further process the image
            resized_image.save('path_to_save_resized_image')

                # Return a success response
            # return JsonResponse({'message': 'Image processed successfully'}, status=200)
            print("ded_image")
            # Save the uploaded image locally
            # with open('uploaded_image.jpg', 'wb') as f:
            #     for chunk in uploaded_image.chunks():
            #         f.write(chunk)

            # Use remove.bg API to remove the background
            api_key = 'Tb94jCjUMck7bngZHmNFcPyn'
            response = requests.post(
                'https://api.remove.bg/v1.0/removebg',
                headers={'X-Api-Key': api_key},
                files={'image_file': open('uploaded_image.jpg', 'rb')},
            )

            # Check if the API call was successful
            if response.status_code == 200:
                # Encode the image content as base64
                image_content_base64 = base64.b64encode(response.content).decode('utf-8')

                # Provide the base64-encoded image content in the response
                result = {'success': True, 'image': image_content_base64}
            else:
                result = {'success': False, 'error': 'Failed to remove background.'}

            return JsonResponse(result)