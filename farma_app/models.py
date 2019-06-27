from django.db import models
import datetime
import re
from django.db.models import F

# Create your models here.

class ItemTable(models.Model):
    refno = models.CharField("Reference No", max_length=50, unique=True, null=False)
    slno = models.CharField("Serial No", max_length=50, null=False)
    date = models.DateField("Entry Date")
    mata_name = models.TextField("Name of Materials", blank=True)
    manu_name = models.CharField("Manufacturer Name", max_length=50, blank=True)
    batch_no = models.CharField("Batch No", max_length=50, blank=True)
    product = models.TextField("Used in Product", blank=True)
    agent = models.CharField("Local Agent", max_length=250, blank=True)
    mfgdate = models.DateField("MFG Date", null=True, blank=True)
    expdate = models.DateField("EXP Date", null=True, blank=True)
    amount = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    consumption = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    coa = models.FileField("Certificate of Analysis", upload_to='pdf/coa', blank=True, null=True)
    msds = models.FileField(upload_to='pdf/msds', blank=True, null=True)
    moa = models.FileField("Method of Analysis", upload_to='pdf/moa', blank=True, null=True)

# calculation of expire date
    def days_to_exp(self):
        if self.expdate:
            now = datetime.date.today()  # gets today's date
            exp = (self.expdate - now).days  # calculates days & time and return only days

            if exp > 1:
                if exp <= 365:
                    return exp, "days"
                else:
                    return  exp, "days,More than a year"
            elif exp < 1 and exp > 0:
                return exp, "day, Today"
            elif exp <0:
                return exp, "days,Expired"
            else:
                return "Invalid date entered"

    # To delete files from media root
    '''def delete(self, *args, **kwargs):
        self.coa.delete()
        self.msds.delete()
        self.moa.delete()
        super().delete(*args, **kwargs)'''

    '''def query(self):
        qs = list(ItemTable.objects.all().annotate(stock=F('amount') - F('consumption')))
        myiter = iter(qs)
        return myiter'''


# shows ref no in the first place in admin view

    def __str__(self):
        return str(self.refno)
