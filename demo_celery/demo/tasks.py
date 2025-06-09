from celery import shared_task
import joblib
import os
from demo.models import Alert
import time
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'alert_classifier.joblib')

model = joblib.load(MODEL_PATH)

@shared_task
def process_demo(demo_id):
    print(f"🔔 Processando demo {demo_id}...")
    time.sleep(5)  
    print(f"✅ demo {demo_id} processado!")
    return f"demo {demo_id} processado"
@shared_task
def classify_alert_task(alert_id):
    try:
        alert = Alert.objects.get(id=alert_id)
        if alert.status == 'pending':
            message = alert.message.lower()

            category = model.predict([message])[0]

            alert.category = category
            alert.status = 'classified'
            alert.save()

            return f"Alert {alert_id} classified as {category}"
        else:
            return f"Alert {alert_id} already classified"
    except Alert.DoesNotExist:
        return f"Alert {alert_id} does not exist"
