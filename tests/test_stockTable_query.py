#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlJhInvUpdateRptpy import *
import pytest


@pytest.mark.parametrize('token,FMaterialId,companyName,FLot,FBillNO,FSalesman,FCustName,output',
                         [('C0426D23-1927-4314-8736-A74B2EF7A039',
                           '01.3889U.904','江苏嘉好热熔胶股份有限公司',
                           'R-230809013-A03B-5202U-AD(1-)(印尼)',
                           'SCDD-100-20230807-0002',
                           '谢纪伟',
                           'PT.ANEKA MITRA GEMILANG', False)])

def test_stockTable_query(token,FMaterialId,companyName,FLot,FBillNO,FSalesman,FCustName,output):

    assert stockTable_query(token,FMaterialId,companyName,FLot,FBillNO,FSalesman,FCustName).empty == output
