# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './api/src/')))
print(sys.path)

import random

from CorpApi import *
from myconf import *

## test
api = CorpApi(TestConf['CORP_ID'], TestConf['APP_SECRET'])

try :
    response = api.httpCall(
            CORP_API_TYPE['MESSAGE_SEND'],
            {
                "touser": "134",
                "agentid": 0,
                'msgtype' : 'text',
                # 'climsgid' : 'climsgidclimsgid_%f' % (random.random()),
                'text' : {
                    'content':'方法论',
                },
                'safe' : 0,
            })
    print(response)
except ApiException as e :
    print(e.errCode, e.errMsg)

