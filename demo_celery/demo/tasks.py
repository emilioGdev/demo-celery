from celery import shared_task
import time

@shared_task
def process_demo(demo_id):
    print(f"🔔 Processando demo {demo_id}...")
    time.sleep(5)  # Simula um processamento demorado
    print(f"✅ demo {demo_id} processado!")
    return f"demo {demo_id} processado"
