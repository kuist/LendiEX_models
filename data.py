class data(models.Model):
    id_client = models.ForeignKey('id_client', on_delete=models.CASCADE, primary_key=True)
    platform = models.CharField(max_length=20)
    currency = models.CharField(max_length=20)
    rate = models.DecimalField
    max_duration = models.IntegerField
    max_lend = models.IntegerField
    total = models.DecimalField(max_digits=12, decimal_places=2)
    win = models.DecimalField(max_digits=12, decimal_places=2)
    total_win_last_24h = models.DecimalField(max_digits=12, decimal_places=2)
    total_win_last_30d = models.DecimalField(max_digits=12, decimal_places=2)

        def __str__(self):
        return f"{self.data}"