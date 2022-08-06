from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(('GET', ))
def get_data(request):
    print(dir(request))
    static_files_path = settings.STATIC_URL
    data = {
        'title': 'ReviseDay',
        'headline': 'WE ARE CRAFTING THIS PLATFORM AND WILL SOON MAKE IT AVAILABLE TO EVERYONE HERE',
        'banner_description': 'Learn and revise something new everyday to remain consistent in Software industry.',
        'launch_date': '2022/10/05 09:15',
        'header_image_url': f'{static_files_path}images/header_image.png',
        'brief_description_title': 'We are working hard to launch our awesome new platform.',
        'brief_description': '',
        'description_image_url': f'{static_files_path}images/description_image.png',
        'logo_image_url': f'{static_files_path}images/logo.png',
        'short_description': '',
        'contact_information': 'Connect with us on linkedin. ',
        'social_media_links': ['https://www.linkedin.com/in/shashidharreddy25/'],

    }
    return Response(data)
