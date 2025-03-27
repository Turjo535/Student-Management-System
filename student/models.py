from django.db import models
from django.core.validators import RegexValidator,validate_email
# Create your models here.
class student_model(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(validators=[validate_email])
    phone=models.CharField(
        max_length=20,  # Adjust based on your needs
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',  # Example regex for international phone numbers
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    course=models.CharField( max_length=50)

    

    