import requests
import json
from flask import render_template

HEADERS_MVIDEO = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.mvideo.ru/products/noutbuk-asus-r565jf-br367-90nb0sw2-m000a0-30062392',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_GUEST_ID=21857423081; MVID_HANDOVER_SUMMARY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; searchType2=3; _sp_id.d61c=52241e73-5d98-4fda-8c43-56eaddfb739b.1668606033.2.1668683469.1668606055.da00a42a-f229-4824-89ba-0310b88f40d3.0a84e9d6-8d1c-41cc-9877-231f8f27ff90.73799ab9-2222-4b3f-be92-2730c2aa4f8f.1668682188485.125; _ga_CFMZTSS5FM=GS1.1.1668682188.2.1.1668684987.0.0.0; _ga=GA1.2.1576863425.1668606033; _ga_BNX5WPP3YK=GS1.1.1668682188.2.1.1668684987.60.0.0; _ym_uid=1668606033872520491; _ym_d=1668606033; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=274e97bb-6e1b-4af2-9fe0-842c5d8ac28a; flocktory-uuid=e3be03ed-cc55-4028-8254-7506f1c5784a-9; uxs_uid=40b9f200-65b4-11ed-9c9c-b908144bb57a; tmr_reqNum=61; tmr_lvid=962784a71d51c0537c1aa258d81d727f; tmr_lvidTS=1668606038150; afUserId=46ff819e-cb51-4368-b9e1-e9c87cc363c9-p; mindboxDeviceUUID=0d26c4a0-ca68-4383-bf1c-952a7d906992; directCrm-session=%7B%22deviceGuid%22%3A%220d26c4a0-ca68-4383-bf1c-952a7d906992%22%7D; __lhash_=0e33432136464febe764a64cebd3fa16; JSESSIONID=S6nrjHKJyhkrKP6GY9VGtm0pwKJhd2PMX50pxhLGCNJ0C3gwZdsP!-1676820433; bIPs=389543560; flacktory=no; SMSError=; authError=; BIGipServeratg-ps-prod_tcp80=1678040074.20480.0000; BIGipServeratg-ps-prod_tcp80_clone=1678040074.20480.0000; Old_Browser_Accept_the_Risk_and_Continue=1; MVID_AB_TOP_SERVICES=0; MVID_CREDIT_AVAILABILITY=true; MVID_IMG_RESIZE=true; MVID_INIT_DATA_OFF=false; MVID_LP_HANDOVER=2; MVID_MOBILE_FILTERS=true; MVID_SERVICES_MINI_BLOCK=var2; MVID_ENVCLOUD=prod1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

COOKIES_MVIDEO = {
    '__lhash_': '79cde6ef05240b77d22844d7ada14038',
    'CACHE_INDICATOR': 'false',
    'COMPARISON_INDICATOR': 'false',
    'HINTS_FIO_COOKIE_NAME': '2',
    'JSESSIONID': '4Mx3j0wG9X35Wxr7gQ6DYJ6fmhdTD93JrJz4wZr6q53dThnnB1Zd!-580586657',
    'MVID_AB_PDP_CHAR': '2',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_AB_TOP_SERVICES': '2',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
    'MVID_CART_AVAILABILITY': 'true',
    'MVID_CART_MULTI_DELETE': 'false',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_CREDIT_AVAILABILITY': 'true',
    'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GIFT_KIT': 'true',
    'MVID_GLC': 'true',
    'MVID_GLP': 'true',
    'MVID_GTM_ENABLED': '011',
    'MVID_GUEST_ID': '21856542605',
    'MVID_HANDOVER_SUMMARY': 'true',
    'MVID_IMG_RESIZE': 'true',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '7700000000000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_MCLICK': 'true',
    'MVID_MINDBOX_DYNAMICALLY': 'true',
    'MVID_MINI_PDP': 'true',
    'MVID_MOBILE_FILTERS': 'true',
    'MVID_MULTIOFFER': 'true',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '1',
    'MVID_REGION_SHOP': 'S002',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'SENTRY_ERRORS_RATE': '0.1',
    'SENTRY_TRANSACTIONS_RATE': '0.5',
    'bIPs': '155255760',
    'flacktory': 'no',
    'searchType2': '2',
    '_sp_ses.d61c': '*',
    '_sp_id.d61c': 'a4c98070-c340-4f67-bdec-d665637107c7.1668587293.1.1668591931..bdcf3b63-20de-4381-9539-1f8fdca988f3..128e9d7c-bcb4-423c-a192-a1ff0eb1be1e.1668587293307.356',
    '_ga_CFMZTSS5FM': 'GS1.1.1668587293.1.1.1668591931.0.0.0',
    '_ga': 'GA1.2.694903322.1668587293',
    '_ga_BNX5WPP3YK': 'GS1.1.1668587293.1.1.1668591931.56.0.0',
    '_gid': 'GA1.2.1592977637.1668587293',
    '_ym_uid': '1668587293293056443',
    '_ym_d': '1668587293',
    '_ym_isad': '2',
    'SMSError': '',
    'authError': '',
    'gdeslon.ru.__arc_domain': 'gdeslon.ru',
    'gdeslon.ru.user_id': 'd0297d0e-ced8-43f9-8b5a-11150819ecb6',
    'tmr_reqNum': '202',
    'tmr_lvid': 'f3f4912d206cee856425b357b0776892',
    'tmr_lvidTS': '1668587296737',
    'uxs_uid': '9e857f20-6588-11ed-92bf-bf860254b519',
    'advcake_track_id': 'c3abf2b3-43f9-bed3-c7e1-5fa9efa9aabb',
    'advcake_session_id': 'ace44de8-bd49-6a41-29d3-3985b960e15f',
    'flocktory-uuid': '240e9b8a-6c49-4b7b-a33d-a11b4bcc5d2e-3',
    'BIGipServeratg-ps-prod_tcp80': '1912921098.20480.0000',
    'afUserId': '57f52354-0a90-4b40-9884-38cb50519131-p',
    'AF_SYNC': '1668587298512',
    'tmr_detect': '0%7C1668591937351',
    'BIGipServeratg-ps-prod_tcp80_clone': '1912921098.20480.0000',
    'Old_Browser_Accept_the_Risk_and_Continue': '1',
    'wurfl_device_id': 'generic_web_browser',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'MVID_GTM_BROWSER_THEME': '1',
    'deviceType': 'desktop',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpDCofIUcdQHZWVihdYlcfCkdpI0spY3MIETBfKyZfTV5oXyYTKmVaUXd0Q1VNSXhhfhZBGjhmI2JHXyBKVVNqJh8Xf3ArVxAPX0ZIcWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFAbSVoUFogS15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=e9l+eQ==',
    '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpDCofIUcdQHZWVihdYlcfCkdpI0spY3MIETBfKyZfTV5oXyYTKmVaUXd0Q1VNSXhhfhZBGjhmI2JHXyBKVVNqJh8Xf3ArVxAPX0ZIcWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFAbSVoUFogS15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=e9l+eQ==',
    'cfidsgib-w-mvideo': 'HNggI4uyXw5//sjD6nGaWp1X/fKlhwk8vbndAfG1MZposvw3RMzb/DIB/hDQWOYkp6ePx6CF6Y10rBrEWvCec74BJeICzQuBkP5XGY0eGtVpQ95AajDod/LnoqFKkCSSarO5+T6rrlYzRKS2h0Yxvyr/s3eZt6I8DjAo',
    'cfidsgib-w-mvideo': 'ZDdfMO7OGe4iUBDW95W5BSunK8qA6+Xttj3TuqvfJsTP/rEd3jPVTXBota+2P1tjNLSYf8nRcv4Ad6KUe7MqmqC9cBhPPo5Nd8yQ3sDR4H/W0Sj/E4XrAQsQqyPsxmjylen5+1h2uZa5RqP8sLCO9n8x9uN+0jDkjHm7',
    'cfidsgib-w-mvideo': 'ZDdfMO7OGe4iUBDW95W5BSunK8qA6+Xttj3TuqvfJsTP/rEd3jPVTXBota+2P1tjNLSYf8nRcv4Ad6KUe7MqmqC9cBhPPo5Nd8yQ3sDR4H/W0Sj/E4XrAQsQqyPsxmjylen5+1h2uZa5RqP8sLCO9n8x9uN+0jDkjHm7',
    'gsscgib-w-mvideo': 'BOWmhyLnYJB1JG3I37ZITsMH/3qIr/tjtCpMLGyQd1YVvcw4SUpURJfdeMpbqCI55To4CbJSkHbwgQl7GGds27NhmurYR7lzk5W305HEy8V0Y3Ap/DVvpvG119np60v7LRtRH5APNROiQxrOm1sX8srgpEDUFFoS2UCNcdV0jAmM3cQLGBgXJ2JFgbHHy/ioFdxSMZFmcDmNZ8gy0bfa+AUbf+8cTOIcEJp9Fnlv/6i5AQJTUcGv/620DcnutQ==',
    'gsscgib-w-mvideo': 'BOWmhyLnYJB1JG3I37ZITsMH/3qIr/tjtCpMLGyQd1YVvcw4SUpURJfdeMpbqCI55To4CbJSkHbwgQl7GGds27NhmurYR7lzk5W305HEy8V0Y3Ap/DVvpvG119np60v7LRtRH5APNROiQxrOm1sX8srgpEDUFFoS2UCNcdV0jAmM3cQLGBgXJ2JFgbHHy/ioFdxSMZFmcDmNZ8gy0bfa+AUbf+8cTOIcEJp9Fnlv/6i5AQJTUcGv/620DcnutQ==',
    'fgsscgib-w-mvideo': 'LnWs5a248645a188b751e467400e90e9285a19d3',
    'fgsscgib-w-mvideo': 'LnWs5a248645a188b751e467400e90e9285a19d3',
    'cookie_ip_add': '188.32.121.158',
    'MVID_ENVCLOUD': 'prod2',
    '_dc_gtm_UA-1873769-1': '1',
    'mindboxDeviceUUID': 'b6d56858-2da4-4ed2-b75e-8600c2b83890',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22b6d56858-2da4-4ed2-b75e-8600c2b83890%22%7D',
    '_dc_gtm_UA-1873769-37': '1',
}

HEADERS_CITYLINK = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.citilink.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://www.citilink.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    }

COOCKIES_ELDORADO = {
    '__lhash_': 'eaf6b8c6cc20c910ca205448aff3bd52',
    'cfidsgib-w-eldorado': 'onW5u8AKfCecEHMVnSJNG0iWuhQcOthQ8iS9ltkrAOMuR5Aih9MAmv2iafVehskIUhV7PnFsXKMioxSeotH9FYqEzxsieq1JV5mWrwiZRlztIswyGWFU0L8uPVp00pZdn9I4xrftmHKFb8CX+y5fYerylRychLJR/DWaVTU=',
    'ab_user': '2630322480100',
    'ab_segment': '26',
    'iRegionSectionId': '11324',
    'grs': '11324',
    'ABT_test': 'A',
    'ek_ab_test': 'B',
    'AUTORIZZ': '0',
    'AC': '1',
    'lv_user_org': '0',
    'el_group_user_org': '0',
    'bonus_cobrand_showed': '0',
    'BITRIX_SM_SALE_UID': '31240836939',
    'BITRIX_SM_SALE_UID_CS': 'f753a30042be59180eb56ddc1b676655',
    '_userGUID': '0:lb9at04o:zX~xKNFolGyvDB8GTQXCCtTuSgTNT8Ms',
    'USER_AUTH_GTM': '0',
    'bCNT': '0%3A0',
    'BITRIX_SM_ELD_TZ_OFFSET': '-180',
    'digi-SearchVisitor': '10%3A10',
    'unauthorizedId': 'c4po6h0qo3xqqd46dg6uzusbiy5qrv8ozdfhi4qoastr3c0qivev9fn8viq8inf75o9875lku5vsn3foufb7bi4ezjz3lrxma0j1rwaz81ely3c97gqwnnip2vga48fal48jfhcemvnezd1zx9fccuqpsb90k9etheex6ejvndl7t7o8k4s0p843dczg4rat8qdotcnxiaireylf7mnmofq04wod0k6ycauf5ez9m59jhojtl0ti8wf8aybzubme',
    '__js_p_': '74,300,0,1,0',
    'dt': '1',
    'PHPSESSID': '1o1vprh8rvs4m087gs9bkgn282',
    '__hash_': 'da211069c53e24beada51c48d148c9f9',
    'show_region_popup': '0',
    '_slfs': '1670581249622',
    'dSesn': 'dce05dec-eb3a-8022-fa7f-c5f173dec9c8',
    '_dvs': '0:lbgcj1mu:4MGZ0LQNZOxyGVIK~hNWxAweBbhM8FFM',
    '__jhash_': '1030',
    '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A107.0%29%20Gecko%2F20100101%20Firefox%2F107.0',
    '__zzatgib-w-eldorado': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2UqemZjJxEZJw0jGH1iGRl+KmZYOUYae0N1dRs3V10cESRYDiE/C2lbVjRnFRtASBgvS255MDtqJWBJXh9IXU11F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NOTMyMGZaK1kwOWNVdBkYNnJmdUyadw==',
    'cfidsgib-w-eldorado': 'onW5u8AKfCecEHMVnSJNG0iWuhQcOthQ8iS9ltkrAOMuR5Aih9MAmv2iafVehskIUhV7PnFsXKMioxSeotH9FYqEzxsieq1JV5mWrwiZRlztIswyGWFU0L8uPVp00pZdn9I4xrftmHKFb8CX+y5fYerylRychLJR/DWaVTU=',
    'gsscgib-w-eldorado': 'XBk8XLutb5M8MeVHIip0Ik1ld6U0JaCiirWUWFcmVWs5tpuVdf9gD7tvu8vNgvs8A7wJga3U3sMJUNrVl1sBCy+jg9ouDkzsa2VALP9GLzqx4e13hFteAJFippJR1GnBma6WvXPLMi76jcE89x10LX//XUvvZQQ0946CAZkgXRs0pqUqWYQUGHy/7qnAp49Q5hX9tcnmbINlhBQNSz+elxqdvqbioX/iXSKpd8Fdk6xDTeHzwo9m95cgM7y2A7Tcmw==',
}

HEADERS_ELDORADO = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.eldorado.ru/',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7IlNJRCI6ImNxMzZpY2E5bjdzamw1cnBxOGxtMG80Z3NrIn0sImV4cCI6MTY3MDQyMjc1MH0.ksJwVgXMxd0uAQMF94bjnfeRammD9KHAu_X68xCPMg_EB9GDl3c1vPsj6f0xKAyUqPFE6cCKUNXkejvwExWZLw',
    'Connection': 'keep-alive',
    # 'Cookie': '__lhash_=eaf6b8c6cc20c910ca205448aff3bd52; cfidsgib-w-eldorado=Eo8vOy9Ot6KhbiUeOcrPpOzaNDhcPxDPDvcS9+ZtCtV263uhQgurtt2maFtjEErnpjMCcDgr5T/83x4Xh1ezL6RRuxd6Mzdj2+UhoOb3ChqLdmW7+Fkl8y5zwz2jfxX5u3aRDj8GcUPLmWsvzZ7Uow5Am1W5082ZbFc0Mw==; iRegionSectionId=11324; grs=11324; ABT_test=A; ek_ab_test=B; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; USER_AUTH_GTM=0; bCNT=0%3A0; BITRIX_SM_ELD_TZ_OFFSET=-180; digi-SearchVisitor=10%3A10; _userGUID=0:lbaq5nn9:r7WpZVeMS26rZ0c6mHWzRl8avTtHz2D_; unauthorizedId=ml7b2rxxzd7qnew6wcogfwiusxrg5trtmy9wqxwavypa8geejmt8jt1128dfndjrax66bxmpqoqm7vdk9l03rghlekh58e5lv2i26nc443aftlvfn0ivn137j0nsfkcqnux1j4lv80dzediqz4to4pms7abuzayuh3ytnx28cld3dgdu25tqw1hf1wh9yh88hluj63ejml1bt097nxc6l6s7uzeepyhxkk9cbnvzso9s9qg3nrlj2tqmsnmsvs5h; __js_p_=545,300,0,1,0; dt=1; PHPSESSID=cq36ica9n7sjl5rpq8lm0o4gsk; __hash_=da8d465dd02ebd520a719faefb192b5e; ab_user=3579922490100; ab_segment=35; show_region_popup=0; _slfs=1670421521654; BITRIX_SM_SALE_UID=31237860953; BITRIX_SM_SALE_UID_CS=1f2c3e9220c9f769b07f63c0b052751b; dSesn=cbe2ccdb-d6c5-fc08-9c39-118507da9c9f; _dvs=0:lbdphmfi:YHdryWxRS2LFcOLm3BTyDemVbDzJq27i; __jhash_=36; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%3B%20rv%3A107.0%29%20Gecko%2F20100101%20Firefox%2F107.0; gssc157=; __zzatgib-w-eldorado=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VcfGgjIHoSKAlcGDthHlM/NCsTRAsiQXg4Nhs3V10cESRYDiE/C2lbVjRnFRtASBgvS255MDtpH2BMWyFMWE51F2BKQys2FkZGHHIzdz9rCCIZURMqX3hHV2tlVUI4MWcMT09NOTMyMGZaK1kwOWNVdBkYNnJmMNK9iw==; cfidsgib-w-eldorado=Eo8vOy9Ot6KhbiUeOcrPpOzaNDhcPxDPDvcS9+ZtCtV263uhQgurtt2maFtjEErnpjMCcDgr5T/83x4Xh1ezL6RRuxd6Mzdj2+UhoOb3ChqLdmW7+Fkl8y5zwz2jfxX5u3aRDj8GcUPLmWsvzZ7Uow5Am1W5082ZbFc0Mw==; gsscgib-w-eldorado=WcxdaYQ4K6zlqCMpmq1S87ZoAr3C+n6DVR8vpnlSjEqwcbWqZoAxlDWFEDkGt9xY0NXEy3SLI2RUfmuxPJ9Te6OBhMt9D35MjQj4/LATn5Mx0LM47KAnyUFn9NMP3fMU2jEsFiWqEdNCvJ0rlvnQjzC9PNuIRxxA1RpL8d5WXiMWRoxIVMbHmxmZa9IHhldzmZQ3kc+BgJd0tbm2l1jFWJ7CIzw+ZK4bpBPwYik1BcRufnowxv8dIy6C0dR4EQE059gDgA==',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

def parse_mvideo(query):

    params_product = {
        'query': query,
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
        'context': 'eyJxdWVyeSI6ItC90L7Rg9GC0LHRg9C6IGxlbm92byB0aGlua3BhZCIsInNob3BJZHMiOlsiUzAwMiJdLCJzdHJhdGVneUlkIjoic3RlcDEiLCJoaWRkZW5GaXJzdEdyb3VwIjpbXSwiZmlyc3RHcm91cCI6WyIxMTgiXSwiZmlyc3RHcm91cFN0YWdlIjoiQkkiLCJyZXNwb25zZVR5cGUiOiJwbGFpbiIsImVucmljaG1lbnRJbmZvIjp7Im1hdGNoZWRCeUNvbmNlcHRzVG9rZW5zIjpbItCd0L7Rg9GC0LHRg9C60LgiLCJMZW5vdm8iLCJUaGlua1BhZCBUNDgwcyJdLCJjcHRDYXRlZ29yeUlzUmVsYXRlZCI6ZmFsc2UsImlzQ29tcGF0aWJpbGl0eSI6ZmFsc2UsIm1hdGNoZWRTZXJpZXNCeUNvbmNlcHRzIjoiVGhpbmtQYWQgVDQ4MHMifSwiYmlTdGF0cyI6eyIxMTgiOjEwMDB9fQ==',
    }

    params_prices = {
        'isPromoApplied': 'true',
        'addBonusRubles': 'true'
    }

    params_details = {
        'multioffer': 'true'
    }

    response = requests.get('https://www.mvideo.ru/bff/products/search', params=params_product, cookies=COOKIES_MVIDEO, headers=HEADERS_MVIDEO).json()
    product_ids = response.get('body').get('products')

    while (len(product_ids) > 3):
        product_ids.pop(len(product_ids) - 1)

    product_list = {}
    product_list['products'] = []

    for i in range(len(product_ids)):
        params_prices['productIds'] = product_ids[i]
        params_details['productId'] = product_ids[i]

        response_prices = requests.get('https://www.mvideo.ru/bff/products/prices', params=params_prices, cookies=COOKIES_MVIDEO, headers=HEADERS_MVIDEO).json()
        response_details = requests.get('https://www.mvideo.ru/bff/product-details', params=params_details, cookies=COOKIES_MVIDEO, headers=HEADERS_MVIDEO).json()

        price = response_prices.get('body').get('materialPrices')[0]['price']['salePrice']
        details = response_details.get('body').get('name')
        link = 'https://www.mvideo.ru/' + 'products/' + product_ids[i]

        product_list['products'].append({'name': details, 'price': price, 'link': link})
    
    with open('jsons\mvideo.json', 'w', encoding='utf-8') as file:
        json.dump(product_list, file, indent=4, ensure_ascii=False)

        return product_list


def parse_citylink(query):

    params = {
        'st': query,
        'apiKey': 'UCC76J09GL',
    }

    response = requests.get('https://autocomplete.diginetica.net/autocomplete', params=params, headers=HEADERS_CITYLINK).json()

    product_list = {}
    product_list['products'] = []
    products_temp = response.get('products')

    count = 0
    for i in products_temp:
        if count == 3:
            break
        if i.get('brand') != "NONAME":
            product_list['products'].append({'name': i.get('name')[:i.get('name').find(',')], 'price': int(i.get('price')[0:len(i.get('price'))-2]), 'link': 'https://www.citilink.ru/' + i.get('link_url')})
        count += 1
    
    with open('jsons\citylink.json', 'w', encoding='utf-8') as file:
        json.dump(product_list, file, indent=4, ensure_ascii=False)

    return product_list


def parse_eldorado(query):

    params = {
    'rootRestrictedCategoryId': '0',
    'query': query,
    'orderField': 'popular',
    'limit': '3',
    'regionId': '11324',
    'strategy': 'sold_amount_relevance',
    }

    response = requests.get('https://www.eldorado.ru/sem/v3/a408/products', params=params, cookies=COOCKIES_ELDORADO, headers=HEADERS_ELDORADO).json()

    product_list = {}
    product_list['products'] = []
    products_temp = response.get('data')
    
    count = 0
    for i in products_temp:
        if count == 3:
            break
        product_list['products'].append({'name': i.get('name'), 'price': i.get('price'), 'link': 'https://www.eldorado.ru/cat/detail/' + str(i.get('id'))})
        count += 1

    with open ('jsons\eldorado.json', 'w', encoding='utf-8') as file:
        json.dump(product_list, file, indent=4, ensure_ascii=False)

    return product_list


def main(q):
    return[parse_mvideo(q), parse_citylink(q), parse_eldorado(q)]


if __name__ == "__main__":
    main('iphone 13 pro max')