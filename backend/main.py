import requests
from bs4 import BeautifulSoup
import json

def get_data(query):

    cookies = {
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': 'b1ce4c8c-be00-4b63-a868-c680bc8e1d49',
        'sentry-trace': 'ec70e93a26f04572a20ee9bd00493fe1-a29db98d4ecf0a77-0',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=ec70e93a26f04572a20ee9bd00493fe1,sentry-sample_rate=0%2C5',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mvideo.ru/product-list-page?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA+lenovo+thinkpad',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '__lhash_=79cde6ef05240b77d22844d7ada14038; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; JSESSIONID=4Mx3j0wG9X35Wxr7gQ6DYJ6fmhdTD93JrJz4wZr6q53dThnnB1Zd!-580586657; MVID_AB_PDP_CHAR=2; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TOP_SERVICES=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_AVAILABILITY=true; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_AVAILABILITY=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GLC=true; MVID_GLP=true; MVID_GTM_ENABLED=011; MVID_GUEST_ID=21856542605; MVID_HANDOVER_SUMMARY=true; MVID_IMG_RESIZE=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_MULTIOFFER=true; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; bIPs=155255760; flacktory=no; searchType2=2; _sp_ses.d61c=*; _sp_id.d61c=a4c98070-c340-4f67-bdec-d665637107c7.1668587293.1.1668591931..bdcf3b63-20de-4381-9539-1f8fdca988f3..128e9d7c-bcb4-423c-a192-a1ff0eb1be1e.1668587293307.356; _ga_CFMZTSS5FM=GS1.1.1668587293.1.1.1668591931.0.0.0; _ga=GA1.2.694903322.1668587293; _ga_BNX5WPP3YK=GS1.1.1668587293.1.1.1668591931.56.0.0; _gid=GA1.2.1592977637.1668587293; _ym_uid=1668587293293056443; _ym_d=1668587293; _ym_isad=2; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=d0297d0e-ced8-43f9-8b5a-11150819ecb6; tmr_reqNum=202; tmr_lvid=f3f4912d206cee856425b357b0776892; tmr_lvidTS=1668587296737; uxs_uid=9e857f20-6588-11ed-92bf-bf860254b519; advcake_track_id=c3abf2b3-43f9-bed3-c7e1-5fa9efa9aabb; advcake_session_id=ace44de8-bd49-6a41-29d3-3985b960e15f; flocktory-uuid=240e9b8a-6c49-4b7b-a33d-a11b4bcc5d2e-3; BIGipServeratg-ps-prod_tcp80=1912921098.20480.0000; afUserId=57f52354-0a90-4b40-9884-38cb50519131-p; AF_SYNC=1668587298512; tmr_detect=0%7C1668591937351; BIGipServeratg-ps-prod_tcp80_clone=1912921098.20480.0000; Old_Browser_Accept_the_Risk_and_Continue=1; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpDCofIUcdQHZWVihdYlcfCkdpI0spY3MIETBfKyZfTV5oXyYTKmVaUXd0Q1VNSXhhfhZBGjhmI2JHXyBKVVNqJh8Xf3ArVxAPX0ZIcWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFAbSVoUFogS15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=e9l+eQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VpDCofIUcdQHZWVihdYlcfCkdpI0spY3MIETBfKyZfTV5oXyYTKmVaUXd0Q1VNSXhhfhZBGjhmI2JHXyBKVVNqJh8Xf3ArVxAPX0ZIcWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeTFAbSVoUFogS15Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MBI=e9l+eQ==; cfidsgib-w-mvideo=HNggI4uyXw5//sjD6nGaWp1X/fKlhwk8vbndAfG1MZposvw3RMzb/DIB/hDQWOYkp6ePx6CF6Y10rBrEWvCec74BJeICzQuBkP5XGY0eGtVpQ95AajDod/LnoqFKkCSSarO5+T6rrlYzRKS2h0Yxvyr/s3eZt6I8DjAo; cfidsgib-w-mvideo=ZDdfMO7OGe4iUBDW95W5BSunK8qA6+Xttj3TuqvfJsTP/rEd3jPVTXBota+2P1tjNLSYf8nRcv4Ad6KUe7MqmqC9cBhPPo5Nd8yQ3sDR4H/W0Sj/E4XrAQsQqyPsxmjylen5+1h2uZa5RqP8sLCO9n8x9uN+0jDkjHm7; cfidsgib-w-mvideo=ZDdfMO7OGe4iUBDW95W5BSunK8qA6+Xttj3TuqvfJsTP/rEd3jPVTXBota+2P1tjNLSYf8nRcv4Ad6KUe7MqmqC9cBhPPo5Nd8yQ3sDR4H/W0Sj/E4XrAQsQqyPsxmjylen5+1h2uZa5RqP8sLCO9n8x9uN+0jDkjHm7; gsscgib-w-mvideo=BOWmhyLnYJB1JG3I37ZITsMH/3qIr/tjtCpMLGyQd1YVvcw4SUpURJfdeMpbqCI55To4CbJSkHbwgQl7GGds27NhmurYR7lzk5W305HEy8V0Y3Ap/DVvpvG119np60v7LRtRH5APNROiQxrOm1sX8srgpEDUFFoS2UCNcdV0jAmM3cQLGBgXJ2JFgbHHy/ioFdxSMZFmcDmNZ8gy0bfa+AUbf+8cTOIcEJp9Fnlv/6i5AQJTUcGv/620DcnutQ==; gsscgib-w-mvideo=BOWmhyLnYJB1JG3I37ZITsMH/3qIr/tjtCpMLGyQd1YVvcw4SUpURJfdeMpbqCI55To4CbJSkHbwgQl7GGds27NhmurYR7lzk5W305HEy8V0Y3Ap/DVvpvG119np60v7LRtRH5APNROiQxrOm1sX8srgpEDUFFoS2UCNcdV0jAmM3cQLGBgXJ2JFgbHHy/ioFdxSMZFmcDmNZ8gy0bfa+AUbf+8cTOIcEJp9Fnlv/6i5AQJTUcGv/620DcnutQ==; fgsscgib-w-mvideo=LnWs5a248645a188b751e467400e90e9285a19d3; fgsscgib-w-mvideo=LnWs5a248645a188b751e467400e90e9285a19d3; cookie_ip_add=188.32.121.158; MVID_ENVCLOUD=prod2; _dc_gtm_UA-1873769-1=1; mindboxDeviceUUID=b6d56858-2da4-4ed2-b75e-8600c2b83890; directCrm-session=%7B%22deviceGuid%22%3A%22b6d56858-2da4-4ed2-b75e-8600c2b83890%22%7D; _dc_gtm_UA-1873769-37=1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'query': query,
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
        'context': 'eyJxdWVyeSI6ItC90L7Rg9GC0LHRg9C6IGxlbm92byB0aGlua3BhZCIsInNob3BJZHMiOlsiUzAwMiJdLCJzdHJhdGVneUlkIjoic3RlcDEiLCJoaWRkZW5GaXJzdEdyb3VwIjpbXSwiZmlyc3RHcm91cCI6WyIxMTgiXSwiZmlyc3RHcm91cFN0YWdlIjoiQkkiLCJyZXNwb25zZVR5cGUiOiJwbGFpbiIsImVucmljaG1lbnRJbmZvIjp7Im1hdGNoZWRCeUNvbmNlcHRzVG9rZW5zIjpbItCd0L7Rg9GC0LHRg9C60LgiLCJMZW5vdm8iLCJUaGlua1BhZCBUNDgwcyJdLCJjcHRDYXRlZ29yeUlzUmVsYXRlZCI6ZmFsc2UsImlzQ29tcGF0aWJpbGl0eSI6ZmFsc2UsIm1hdGNoZWRTZXJpZXNCeUNvbmNlcHRzIjoiVGhpbmtQYWQgVDQ4MHMifSwiYmlTdGF0cyI6eyIxMTgiOjEwMDB9fQ==',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/search', params=params, cookies=cookies, headers=headers).json()

    product_ids = response.get('body').get('products')
    with open('product_ids.json', 'w') as file:
        json.dump(product_ids, file, indent=4)
    print('https://www.mvideo.ru/' + 'products/' + product_ids[0])


def main():
    query = input('Введите запрос\n')
    get_data(query)


if __name__ == "__main__":
    main()