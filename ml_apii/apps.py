from django.apps import AppConfig
import onnxruntime as ort


class MlApiiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ml_apii"
    

