
import datetime
from rest_framework import serializers
from tabulation.models import HatchRecord, HatchDetail


class HatchRecordSerializers(serializers.ModelSerializer):
    """
       孵化记录
    """
    key = serializers.SerializerMethodField("get_key")
    begin_time = serializers.SerializerMethodField("get_begin_time")
    
    class Meta:
        model = HatchRecord
        fields = (
            "id",
            "key",
            "begin_time",
            "customer",
            "batch",
            "beizhu",
            "incubator",
            "create_time",
            "end_time",
            "out_machine"
        )

    def get_key(self, obj):
        return obj.id

    def get_begin_time(self, obj):

        delta = datetime.timedelta(hours=8)
        end_time = (obj.begin_time + delta).strftime("%Y-%m-%d")  
        
        return end_time

class HatchRecordCreateSerializers(serializers.ModelSerializer):
    """
       孵化记录
    """
    key = serializers.SerializerMethodField("get_key")
    # begin_time = serializers.SerializerMethodField("get_begin_time")
    
    class Meta:
        model = HatchRecord
        fields = (
            "id",
            "key",
            "begin_time",
            "customer",
            "batch",
            "beizhu",
            "incubator",
            "create_time",
            "end_time",
            "out_machine"
        )

    def get_key(self, obj):
        return obj.id 

    # def get_begin_time(self, obj):

    #     # if obj:
    #     #     delta = datetime.timedelta(hours=8)
    #     #     end_time = (obj.begin_time + delta).strftime("%Y-%m-%d")  
    #     # else:
    #     end_time = obj.begin_time

    #     return end_time

class HatchRecordDetailSerializers(serializers.ModelSerializer):
    """
       品种详情
    """
    
    class Meta:
        model = HatchDetail
        fields = '__all__'