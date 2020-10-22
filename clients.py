class clients(models.Model):
    id_client = models.SET_NULL,
    primary_key=True,
    blank=True,
    null=True,
)
    id_referral = models.ForeignKey('data', on_delete=models.CASCADE)
    email = models.EmailField
    telegram = models.CharField(max_length=20)
    old_client = models.BooleanField
    active = models.BooleanField
    bf_api_key = models.CharField(max_length=100)
    bf_api_secret = models.CharField(max_length=100)
    bf_sub_datetime = models.DateTimeField
    po_api_key = models.CharField(max_length=100)
    po_api_secret = models.CharField(max_length=100)
    credits = models.DecimalField(max_digits=7, decimal_places=2)
    eth_address = models.CharField(max_length=100, unique)

    def __str__(self):
        return f"{self.id_client}"
