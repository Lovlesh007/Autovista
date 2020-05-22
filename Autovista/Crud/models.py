from django.db import models
# Create your models here.
class Leads(models.Model):
	INTERESTED_IN =(
		('Buy New Car', 'Buy New Car'),
		('Buy Second hand Car','Buy Second hand Car'),
		('Sell Second hand Car','Sell Second hand Car'),
		('Others', 'Others'),
	)
	Name           = models.CharField(max_length=50)  #max length=required length
	Phone 		   = models.CharField(max_length=12)
	Email_address  = models.EmailField(max_length=30)
	Interested_in  =models.CharField(max_length=50,choices=INTERESTED_IN)
	def __str__(self):
		return str((self.Name,self.Phone,self.Email_address,self.Interested_in))
 


