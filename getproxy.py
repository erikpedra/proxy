#Coded Eric Pedra
#Free
#No Sale ! 
import requests
import json, sys
import loguru, js2py, time
import pyquery
def MencariProxy():
    proxies = []
    countries = ['AF','AX','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BA','BW','BV','BR','IO','BN','BG','BF','BI','KH','CM','CA','CV','KY','CF','TD','CL','CN','CX','CC','CO','KM','CG','CD','CK','CR','CI','HR','CU','CY','CZ','DK','DJ','DM','DO','EC','EG','SV','GQ','ER','EE','ET','FK','FO','FJ','FI','FR','GF','PF','TF','GA','GM','GE','DE','GH','GI','GR','GL','GD','GP','GU','GT','GG','GN','GW','GY','HT','HM','VA','HN','HK','HU','IS','IN','ID','IR','IQ','IE','IM','IL','IT','JM','JP','JE','JO','KZ','KE','KI','KP','KR','KW','KG','LA','LV','LB','LS','LR','LY','LI','LT','LU','MO','MK','MG','MW','MY','MV','ML','MT','MH','MQ','MR','MU','YT','MX','FM','MD','MC','MN','MS','MA','MZ','MM','NA','NR','NP','NL','AN','NC','NZ','NI','NE','NG','NU','NF','MP','NO','OM','PK','PW','PS','PA','PG','PY','PE','PH','PN','PL','PT','PR','QA','RE','RO','RU','RW','SH','KN','LC','PM','VC','WS','SM','ST','SA','SN','CS','SC','SL','SG','SK','SI','SB','SO','ZA','GS','ES','LK','SD','SR','SJ','SZ','SE','CH','SY','TW','TJ','TZ','TH','TL','TG','TK','TO','TT','TN','TR','TM','TC','TV','UG','UA','AE','GB','US','UM','UY','UZ','VU','VE','VN','VG','VI','WF','EH','YE','ZM','ZW']
    for country in countries:
        url = f'https://www.proxynova.com/proxy-server-list/country-{country}/'
        loguru.logger.debug(f'Get Proxy COENG: {url}')
        loguru.logger.warning(f'Get Proxy COENG: downloading...')
        response = requests.get(url)
        if response.status_code != 200:
            loguru.logger.debug(f'Get Proxy COENG: status code is not 200')
            continue
        loguru.logger.success(f'Get Proxy COENG: downloaded.')
        d = pyquery.PyQuery(response.text)
        table = d('table#tbl_proxy_list')
        rows = list(table('tbody:first > tr').items())
        loguru.logger.warning(f'Get Proxy COENG : scanning...')
        for row in rows:
            tds = list(row('td').items())
            if len(tds) == 1:
                continue
            js = row('td:nth-child(1) > abbr').text()
            js = 'let x = %s; x' % (js[15:-2])
            ip = js2py.eval_js(js).strip()
            port = row('td:nth-child(2)').text().strip()
            proxy = f'{ip}:{port}'
            proxies.append(proxy)
        loguru.logger.success(f'Get Proxy COENG: scanned.')
        loguru.logger.debug(f'Get Proxy COENG: {len(proxies)} proxies is found.')
        time.sleep(1)
    return proxies
if __name__ == "__main__":
    MencariProxy()
