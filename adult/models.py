from django.db import models

# Create your models here.
#Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked
class WorkClass(models.Model):
	WorkClass = (
		('Private', "Private"),
		('Self-emp-not-inc', "Self-emp-not-inc"),
		('Self-emp-inc', "Self-emp-inc"),
		('Federal-gov', "Federal-gov"),
		('Local-gov', "Local-gov"),
		('State-gov', "State-gov"),
		('Without-pay', "Without-pay"),
		('Never-worked', "Never-worked"),
	)
	workclass = models.CharField(max_length=30,choices=WorkClass,unique=True)
	def __str__(self):
		return self.workclass
#Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool
class Education(models.Model):
	Education=(
		('Bachelors',"Bachelors"),
		('Some-college',"Some-college"),
		('11th',"11th"),
		('HS-grad',"HS-grad"),
		('Assoc-acdm',"Assoc-acdm"),
		('9th',"9th"),
		('7th-8th',"7th-8th"),
		('Masters',"Masters"),
		('1st-4th',"1st-4th"),
		('10th',"10th"),
		('Doctorate',"Doctorate"),
		('5th-6th',"5th-6th"),
		('Preschool',"Preschool"),
	)
	education = models.CharField(max_length=30,choices=Education,unique=True)
	def __str__(self):
		return self.education

#Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse
class MartialStatus(models.Model):
	MartialStatus=(
		('Married-civ-spouse',"Married-civ-spouse"),
		('Divorced',"Divorced"),
		('Never-married',"Never-married"),
		('Separated',"Separated"),
		('Widowed',"Widowed"),
		('Married-spouse-absent',"Married-spouse-absent"),
		('Married-AF-spouse',"Married-AF-spouse"),
	)
	martialstatus = models.CharField(max_length=40,choices=MartialStatus,unique=True)
	def __str__(self):
		return self.martialstatus

#Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried
class Occupation(models.Model):
	Occupation=(
		('Wife',"Wife"),
		('Own-child',"Own-child"),
		('Husband',"Husband"),
		('Not-in-family',"Not-in-family"),
		('Other-relative',"Other-relative"),
		('Unmarried',"Unmarried"),
	)
	occupation = models.CharField(max_length=30,choices=Occupation,unique=True)
	def __str__(self):
		return self.occupation

class Relationship(models.Model):
	Relationship=(
		('Wife',"Wife"),
		('Own-child',"Own-child"),
		('Husband',"Husband"),
		('Not-in-family',"Not-in-family"),
		('Other-relative',"Other-relative"),
		('Unmarried',"Unmarried"),
	)
	relationship = models.CharField(max_length=20,choices=Relationship,unique=True)
	def __str__(self):
		return self.relationship
#White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black
class Race(models.Model):
	Race=(
		('White',"White"),
		('Asian-Pac-Islander',"Asian-Pac-Islander"),
		('Amer-Indian-Eskimo',"Amer-Indian-Eskimo"),
		('Other',"Other"),
		('Black',"Black"),
	)
	race = models.CharField(max_length=40,choices=Race,unique=True)
	def __str__(self):
		return self.race
#Female, Male
class Sex(models.Model):
	Sex=(
		('Female',"Female"),
		('Male',"Male"),
	)
	sex = models.CharField(max_length=6,choices=Sex,unique=True)
	def __str__(self):
		return self.sex

#United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands

class NativeCountry(models.Model):
	NativeCountry=(
		('United-States',"United-States"),
		('Cambodia',"Cambodia"),
		('England',"England"),
		('Puerto-Rico',"Puerto-Rico"),
		('Canada',"Canada"),
		('Germany',"Germany"),
		('Outlying-US',"Outlying-US(Guam-USVI-etc)"),
		('India',"India"),
		('Japan',"Japan"),
		('Greece',"Greece"),
		('South',"South"),
		('China',"China"),
		('Cuba',"Cuba"),
		('Iran',"Iran"),
		('Honduras',"Honduras"),
		('Philippines',"Philippines"),
		('Italy',"Italy"),
		('Poland',"Poland"),
		('Jamaica',"Jamaica"),
		('Vietnam',"Vietnam"),
		('Mexico',"Mexico"),
		('Portugal',"Portugal"),
		('Ireland',"Ireland"),
		('France',"France"),
		('Dominican-Republic',"Dominican-Republic"),
		('Laos',"Laos"),
		('Ecuador',"Ecuador"),
		('Taiwan',"Taiwan"),
		('Haiti',"Haiti"),
		('Columbia',"Columbia"),
		('Hungary',"Hungary"),
		('Guatemala',"Guatemala"),
		('Nicaragua',"Nicaragua"),
		('Scotland',"Scotland"),
		('Thailand',"Thailand"),
		('Yugoslavia',"Yugoslavia"),
		('El-Salvador',"El-Salvador"),
		('Trinadad&Tobago',"Trinadad&Tobago"),
		('Peru',"Peru"),
		('HongKong',"HongKong"),
		('Holand-Netherlands',"Holand-Netherlands"),
	)
	nativecountry = models.CharField(max_length=40,choices=NativeCountry,unique=True)
	def __str__(self):
		return self.nativecountry

class adult(models.Model):
	age=models.IntegerField(default=20)
	workclass= models.ForeignKey("WorkClass", on_delete=models.CASCADE)
	fnlwgt=models.IntegerField(default=100000)
	education= models.ForeignKey("Education", on_delete=models.CASCADE)
	education_num= models.IntegerField(default=20)
	marital_status= models.ForeignKey("MartialStatus", on_delete=models.CASCADE)
	occupation= models.ForeignKey("Occupation", on_delete=models.CASCADE)
	relationship= models.ForeignKey("Relationship", on_delete=models.CASCADE)
	race= models.ForeignKey("Race", on_delete=models.CASCADE)
	sex= models.ForeignKey("Sex", on_delete=models.CASCADE)
	capital_gain=models.IntegerField(default=10)
	capital_loss=models.IntegerField(default=10)
	hours_per_week=models.IntegerField(default=10)
	native_country= models.ForeignKey("NativeCountry", on_delete=models.CASCADE)
	

