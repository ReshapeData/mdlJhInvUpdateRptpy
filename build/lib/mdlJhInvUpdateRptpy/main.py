#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .inventory import *

def stockTable_query(token,FMaterialId,companyName,FLot,FBillNO,FSalesman,FCustName):
    '''
    嘉好即时库存更新报表查询入口函数
    :param token: ERP数据库token
    :param FMaterialId: 物料编码
    :param companyName: 业务组织
    :param FLot: 批号
    :param FBillNO: 入库单号
    :param FSalesman: 销售员
    :param FCustName: 客户名称
    :return:
    '''

    res=sql_query(token,FMaterialId,companyName,FLot,FBillNO,FSalesman,FCustName)

    return res