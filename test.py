# -*- coding: utf-8 -*-
import top.api
from CONSTANT import *
#url="http://gw.api.taobao.com/router/rest"
req=top.api.TbkItemGetRequest( 'gw.api.taobao.com',80 )
req.set_app_info(top.appinfo(appkey,serect))

req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
req.q="女装"
resp= req.getResponse()
print(resp)
