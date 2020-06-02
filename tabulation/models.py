from django.db import models

# Create your models here.


class HatchRecord(models.Model):
    
    HATCH_TYPE=(
        (1, "冬温大蛋"),
        (2, "冬温小蛋"),
        (3, "夏温大蛋"),
        (4, "夏温小蛋"),
    )
    
    create_time = models.DateTimeField(verbose_name="来蛋时间")
    batch = models.IntegerField(verbose_name="批次")
    customer = models.CharField(verbose_name="来蛋客户", max_length=255)
    incubator = models.IntegerField(verbose_name="孵化机")
    hatch_pattern = models.SmallIntegerField(choices=HATCH_TYPE, verbose_name="孵化模式", default=3)
    out_machine = models.CharField(verbose_name="出壳机", null=True, blank=True, max_length=32)
    begin_time = models.DateTimeField(verbose_name="够温时间", null=True, blank=True)
    end_time = models.DateTimeField(verbose_name="出苗时间", null=True, blank=True)
    beizhu = models.TextField(verbose_name="备注", null=True, blank=True, max_length=3200)
    

class HatchDetail(models.Model):

    hatchrecord = models.ForeignKey(HatchRecord, verbose_name='孵化基础信息', on_delete=models.DO_NOTHING)
    pinzhong = models.CharField(verbose_name="品种", max_length=32)
    jianshu = models.IntegerField(verbose_name="件数")
    zhuangjidanshu = models.IntegerField(verbose_name="装机蛋数")
    cipodanshu = models.IntegerField(verbose_name="次破总数", null=True, blank=True)
    wujingdanshu = models.IntegerField(verbose_name="无精总数", null=True, blank=True)
    huojingdanshu = models.IntegerField(verbose_name="活精总数", null=True, blank=True)
    shoujinglv = models.DecimalField(verbose_name="受精率", max_digits=10, decimal_places=2, default=0.00)
    maodanshu = models.IntegerField(verbose_name="毛蛋数", null=True, blank=True)
    gongmiao = models.IntegerField(verbose_name="公苗", null=True, blank=True)
    mumiao = models.IntegerField(verbose_name="母苗", null=True, blank=True)
    hunhemiao = models.IntegerField(verbose_name="混合苗", null=True, blank=True)
    heji = models.IntegerField(verbose_name="总苗数", null=True, blank=True)
    shuojingdanchumiaol = models.DecimalField(verbose_name="受精率", max_digits=10, decimal_places=2, default=0.00)
    zhongdanchumiaolv = models.DecimalField(verbose_name="受精率", max_digits=10, decimal_places=2, default=0.00)




class HatchContrast(models.Model):

    HATCH_TYPE=(
        (1, "冬温大蛋"),
        (2, "冬温小蛋"),
        (3, "夏温大蛋"),
        (4, "夏温小蛋"),
    )

    hatch_pattern = models.SmallIntegerField(choices=HATCH_TYPE, verbose_name="孵化模式")
    tailing = models.IntegerField(verbose_name="胎龄")
    biaowen = models.DecimalField(verbose_name="标温", max_digits=10, decimal_places=2, default=0.00)
    tiaowen = models.DecimalField(verbose_name="调温", max_digits=10, decimal_places=2, default=0.00)
    cefengmen = models.CharField(verbose_name="侧风门", max_length=32)
    shangfengmen = models.CharField(verbose_name="上风门", max_length=32)
    shidu = models.IntegerField(verbose_name="湿度")
    zhaodan = models.CharField(verbose_name="照蛋", max_length=255, null=True, blank=True)
    luopan = models.CharField(verbose_name="落盘", max_length=255, null=True, blank=True)
    other = models.CharField(verbose_name="其他", max_length=255, null=True, blank=True)