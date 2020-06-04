import time
import datetime
from django.shortcuts import render

# Create your views here.

from django.utils.timezone import utc

from django.shortcuts import get_object_or_404
from .serializers import HatchRecordSerializers, HatchRecordCreateSerializers, HatchRecordDetailSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from .models import HatchDetail, HatchRecord, HatchContrast


class HatchViewSet(viewsets.ModelViewSet):

    serializer_class = HatchRecordSerializers
    queryset = HatchRecord.objects.filter()

    def create(self, request, *args, **kwargs):

        # 判断用户是否是修改密码,这3个字段是必须填写的
        self.serializer_class=HatchRecordCreateSerializers
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # return super().create(request, *args, **kwargs)
        fuhuashilu_list = request.data.get('fuhuashilu', None)
        fuhuadata_List = []
        if fuhuashilu_list:
            for i in fuhuashilu_list:
                hatch_detail = HatchDetail(**i, hatchrecord_id=serializer.instance.id)
                fuhuadata_List.append(hatch_detail)
        HatchDetail.objects.bulk_create(fuhuadata_List)

        return Response(
            data={"msg": "操作成功", "data": serializer.data, "code": 20000},
            status=status.HTTP_200_OK,
        )

    def update(self, request, pk=None, *args, **kwargs):
        """
          编辑
        """
        self.serializer_class=HatchRecordCreateSerializers
        fuhuashilu_list = request.data.get('fuhuashilu', None)
        if fuhuashilu_list:
            for i in fuhuashilu_list:
                HatchDetail.objects.filter(id=i['id']).update(**i)

        resp = super().update(request, *args, **kwargs)
        return Response(
            data={"data": resp.data, "msg": "更新成功", "code": 20000}, status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
          套餐详情
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        """
        query = HatchRecord.objects.filter(id=pk).first()
        if query:
            serializer = HatchRecordSerializers(query).data
            hatchdetails = HatchDetail.objects.filter(hatchrecord_id=pk)
            hatchdetail_list = HatchRecordDetailSerializers(hatchdetails, many=True).data
            serializer['fuhuashilu'] = hatchdetail_list
            return Response(
                data={"msg": "操作成功", "data": serializer, "code": 20000}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={"msg": "操作失败", "code": 20001}, status=status.HTTP_400_BAD_REQUEST
            )

    @action(methods=["get"], detail=False)
    def free(self, request):
        """
         获取1~30台机器的状态
        :param request:
        :return:
        """
        date_time = request.query_params.get('date_time', datetime.datetime.now(utc).strftime("%Y-%m-%d"))
        print(date_time)
        machine_list = []
        for i in range(1, 31):
            hatchrecord = HatchRecord.objects.filter(incubator=i).last()
            if hatchrecord:
                if hatchrecord.end_time.strftime("%Y-%m-%d") > date_time:
                    # taining = 时间差
                    tailing = (self.parse_ymd(date_time) - self.parse_ymd(hatchrecord.begin_time.strftime("%Y-%m-%d"))).days
                    hatch_pattern = hatchrecord.hatch_pattern
                    hatch_contrast = HatchContrast.objects.get(hatch_pattern=hatch_pattern, tailing=tailing)
                    # 获取对应的公式
                    dict = {
                        "key": i,
                        "id": hatchrecord.id,
                        "out_machine": hatchrecord.out_machine,
                        "incubator": i,
                        "pici": hatchrecord.batch,
                        "taining": tailing,
                        "biaowen": hatch_contrast.biaowen,
                        "cefengmen": hatch_contrast.cefengmen,
                        "shangfengmen": hatch_contrast.shangfengmen,
                        "shidu": hatch_contrast.shidu,
                        "tiaowen": hatch_contrast.tiaowen if hatch_contrast.tiaowen else "---",
                        "zhaodan": hatch_contrast.zhaodan if hatch_contrast.zhaodan else "---",
                        "luopan": hatch_contrast.luopan if hatch_contrast.luopan else "---",
                        "other": hatch_contrast.other if hatch_contrast.other else "---",
                    }
                else:
                    dict = {
                        "key": i,
                        "out_machine": "",
                        "incubator": i,
                        "pici": "---",
                        "taining": "---",
                        "biaowen": "---",
                        "cefengmen": "---",
                        "shangfengmen": "---",
                        "shidu": "---",
                        "tiaowen": "---",
                        "zhaodan": "---",
                        "luopan": "---",
                        "other": "---",
                    }
            else:
                dict = {
                        "key": i,
                        "out_machine": "",
                        "incubator": i,
                        "pici": "---",
                        "taining": "---",
                        "biaowen": "---",
                        "cefengmen": "---",
                        "shangfengmen": "---",
                        "shidu": "---",
                        "tiaowen": "---",
                        "zhaodan": "---",
                        "luopan": "---",
                        "other": "---",
                }

            machine_list.append(dict)
        if machine_list:
            return Response(
                data={"msg": "查询孵化机状态正常", "data": machine_list, "code": 20000},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data={"msg": "查询孵化状态异常", "code":100001},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def parse_ymd(self, s):
        year_s, mon_s, day_s = s.split('-')
        return datetime.datetime(int(year_s), int(mon_s), int(day_s))
