from django.http import JsonResponse
from .tasks import process_demo
import random

def create_demo(request):
    demo_id = random.randint(1000, 9999)
    process_demo.delay(demo_id)  
    return JsonResponse({'message': f'demo {demo_id} enviado para processamento.'})
