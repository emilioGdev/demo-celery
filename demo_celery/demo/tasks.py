from celery import shared_task
import time

from demo.classifier import classify_alert
from demo.models import Alert

@shared_task
def process_demo(demo_id):
    print(f"🔔 Processando demo {demo_id}...")
    time.sleep(5)  # Simula um processamento demorado
    print(f"✅ demo {demo_id} processado!")
    return f"demo {demo_id} processado"

@shared_task
def classify_alert_task(alert_id):
    try:
        alert = Alert.objects.get(id=alert_id)
        if alert.status == 'pending':
            category = classify_alert(alert.message)
            alert.category = category
            alert.status = 'classified'
            alert.save()
            return f"Alert {alert_id} classified as {category}"
        else:
            return f"Alert {alert_id} already classified"
    except Alert.DoesNotExist:
        return f"Alert {alert_id} does not exist"