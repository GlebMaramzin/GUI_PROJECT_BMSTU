import time
import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
'''
selenium_options = {
    'proxy': {
        'http': 'http://shear23u671:k6hpn2pz@proxy.bmstu.ru:8476',
        'https': 'https://shear23u671:k6hpn2pz@proxy.bmstu.ru:8476',
        'no_proxy': 'localhost,127.0.0.1'
        }
}
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(seleniumwire_options=selenium_options)
driver.get('https://proxy.bmstu.ru')
time.sleep(5)
driver.quit()
'''
basic = HTTPBasicAuth('shear23u671','k6hpn2pz')
proxy = {
        'https': 'https://shear23u671:k6hpn2pz@proxy.bmstu.ru:8476',
        }
userAgent = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
cookies = {
    "Set_cookie": "__portal3_info=eyJuYW1lIjoiXHUwNDI4XHUwNDQyXHUwNDM1XHUwNDM0XHUwNDQzXHUwNDNiIFx1MDQyZFx1MDQzMlx1MDQzMFx1MDQzZCBcdTA0MjBcdTA0M2VcdTA0MzFcdTA0MzVcdTA0NDBcdTA0NDJcdTA0M2VcdTA0MzJcdTA0MzhcdTA0NDciLCJleHBpcmUiOjE3MTQzOTg1MTl9; path=/; domain=.eu.bmstu.ru; secure"
}
data = {
    "username": "shear23u671",
    "password": "k6hpn2pz",
    #"execution": "bcb73146-d1c1-4930-8c5d-77aae4dda0a3_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVTNWeFkxcHBaVXBaUjFZcmJISmFTMHA2T1hFME0zaHdiWGxCZW1neE9GaFdhMGR1SzFSMGN6WTFka1ZsVFhoc1IyVXhSV3hzVW1sV1VsWnpPVUYxVWxKeFdVMXlkVWhPZDNoclpEZFBSaXRPUmpCRmFIRmFaRlpLVDBKRGMxVXJiVFozWmxCak5XeFRhMmgwYUU5UVprSm9lRWhJYkcwNFRFUkVMemx3TjA5NldYZ3pVSHBtWWtWVldUQjNXakJXUVVadmVucFZhWGRrTTBGaFp6WnllbU5MWTI4eGJqbEZTVEZzTm5SMlRtdGFTMjgyYXpKTlVuTnBTRUZ3U25JNU9VVnphaTkwY1RJNVZYVlFhbVYyTkRsS1RqVTJRWGxCVkhKb2JESmxlRFF3Y0RsWVprUkVTRVIzZHpsSGRUWlVWMnhrUVhReGRIcHZOSEJsU0hsdVlsZEtkVzlyTkN0RE0ybEZPVGhIT0hoV1VEUlJOMmQ1Ykc5d2FFUk1kMjFyV0cxTFduUTFSRFpGUlRkeWRuaEhXakpRZVVwVVdUQnBkbEJYVm5aR1YwSTNjVlY2YlRWR1NteGtRM3BXUlM5SGJXOHJibkpCTmpOSWExZzRNVUZFVmtsQ2VqUndUSE5QVjJsUVVsQXJZazR6ZUZadmNHWjVWbEpHTVUxWk5sUnhXbmtyTTNBMWQzUkhiRXg2U1ZSSUszbDZWMUIwYldkWFlWUnFiRkU1YjFacWVGUXpVWGcwZERnclNYVkNRMU42WkU1MFNVdFdWM1ZVWkhOSmNVeG9TbU5pVDNGUGVHUTFVbFpvVTJoTk1YWnhUVmd4TVdZMFVHOXhjRXhUVG5FM2VuWXpiSEZRUkZSdVJFOUdTelJUZHl0bE5FSkhjWFEwSzA1UEszQm5ZazFYTVZkWFMzSndZM1o1VW5sRU1Xc3phSE5DWVRreFRGSmxkSEZVY1RCdWQybFVkUzlDYjA1TmVYUlNjRTh4U1hnMVNVNVBaMkpyWW5kNmFHdzRNWElyU25KRlNEWnpWVFZ6VnpWTWNFOVpWblpPYldjMWQyNDNVMmRNWmxwTlowZzVRamgzTDJ4U2IyWlZUVTlGYzJaM2FEQmtjVUp6TmxGUlFVMTRUM0U1VWpCU2FqSnROek51TnpneFYzaEthbmhaWVdKRVQwWXdURUZ5ZG01WVptUlVVakpWUjJ4bU0ySnNiMkZUWkU5TmRrTTJNV0ZuWlc0MmJUZDVXSEpUU1VOd01VNHlVR2huTkVGWFZFVnVkbmgyU0RSSldpdFBNVE16TVRsbmNYWTVTMEUyVTJoUVQyRkhSRzUyVHpGdVVqY3pWek5DTWtKV1pWQlZOV1ZwUTJFNWFsZEJlVFExTlZab1FVeGFXa3hSY1ZoamIwdHpTa1pLWTFscVVUbENWM3A1YUc1T2IwTm5kWHB3VjBSSWEwdDJkRU5GZVdSeVdqaG1TekJsUVhkRWEyaE1OelZWVDNFemVqbHlVV0ZWUW5kR1ZXSnVNelZvWTBad04yTktiVnByTkZZNWREQkpUVmRxV1dSeVJpczRLMmxJZDJOalIySnJXRkZzWjBweWVqUTFXbmhTU0daUGF6aFpjVEZhUldWR05HUXpUbWx1TTBST1J5dFBTMmhUYm1wcFluUTNNMnAyUzJ4aWMwVk9hVFJJUVhsWFRERjVUVUpYU0VoWVJURmFjR3BuYXk5UVluRjBSVll2WWxSeUswUjNaVFJaYjFBNUsyVTNVSFZ5YUhWMFpGaHVhRGRUVG1sMVowZENRVUZxTTBaemJsSjNaMWhtTmpKeGEwMUhPRE5UU200MGMwUXpXWEZVU1ZOMlVETjBkRFpIYW1rNVZYaHNjRFpPYURCdVFXcG5UM0Z4TWtrckwxcG1WalZYYm5nclRuQm9XWFYwVmtsMFoyWmlkbVJWV1hSbldrMTRiVzVIYTJWaFpqTnlWbWxKVGs1V1V6bHpiazVST1U1YVNUWkZWRE51Vlc1aVZFTkNMM1F5TTBsbFFXMHlhSFpMVWxCSlYybFZVRFpOZW1WcU4yWm5NSE14VEdNemFEUjVRV2QyU1VwUVRsZE1jRGREYlV4NlJHazJUMnMxZDI1WGF5ODJRUzlWYVhWV1VIaDZhbUZvY0dGbWNHbGtNVTV5YkdocFMyMU5RbTVtVlhSM2RGaGFkMlJMV1Vac2JEQTNiRFJxYUNzMVdYQnpNVzFtVW5oblpVbHZOQ3RJTlhCRU9IWmhZMVZuVm1WRlEzcHVNa3RDY0ZRMlNsVnFNamRvUjFGaFNrdHJUVFppWWxOQldqWndTbWxhUlhGSVFWTldjR0ppSzFGS2EwbDFNVzlZTnpac2NHbGhkMEpGUmpoV1RXRmlTWGxxVWtkbmVHMHhka3hCZW5CYU1rcG1OR1JMWkhOMFF5dHFUVFV5WlcxelJqQnhiR3AxZFUxc1UyMDJOMmRvZEhOMmQxUXpNRGhwU0VSbVJHWmxXR0UxVkU5QlMxaEhlR3M1WkhVd01rd3dTRGhETVhKdU9ISlpSVEYxV2tsVVF6ZFpVbFZ4VW5SemJGUkxSVFphWkZaRWMzQmhZMHhFWmxONWMwNXBiSE5aUXpKYVlrMVdabE55VlVKbFQwSkNRVFJtWjFOU2FrSXlUbXdyTVU0NWNXMTJPVFppWWtOS1pIRkVOUzlOU1ZOMGFpOWtXbXRVWTNsdU9XMDBPVGRTZDJGTmRXeGxlamREV25vek1ub3pNV1JZWjNvdmJtOXRNMFJXZDBzMmFtVndjVTF4YVdWVVowaFZlR1ZaVjI5WlZsTmxLMDQyT0V0VU9FcHBSemRoYUhreVUyMXdhM1pzVG0xUE9HaElURXd2Ylc1RlMzVkVaMGhrVUZoVGJ6TTRNRzlRVDJaVVRtNVRZakpqUVhkTFdpOHJiakJ0YkhCSlRqWkZZMlY2ZDFVMlVFVlVVMUJFYWxwMWFqRXZNVEJTZFVwdll6Uk1SWFF2ZVUxcmF6UmtURlZHVGl0bmJsZE9iVTlSUWs1NVQxZEZNREZRTTI1U1JsTjBiblJGT0Vjd1NDOVZiakJ6Y2pONlZHTk1XbVYwVkZKdFZ6VjVXRVZVV1VGVU9GRldia00wYkc5NFIxZHdWVGRtTUdNdk5pOXFTemhvTkRCa2RuQnlkMDFJZEdWeGNHVmpUMnRtTnpKUGRDOURXakpGWmt4dFJFeGFkMlV4U0U1aFkwMHhja2cwUm1STGVqa3hNbXRWZVhGYVNrbFlPVTFTZERWRFJIUnZiWHBxTTNVNU1tWkZVRlZtWTJFMFdESkNTMkZQYkZaSEwzQldjaTlyTTFwck9VWmpkMmR5Y2tneWN6VXZSV2xOVGtSR0x5OWxTMEpSUjBoTWEwSm1UVzlZTkZoUVZFUkpNbVJYTjNBdllqRlVjM0kzYWpoU1dHdzBZVXMzZUdkdVZtRkZZWGRqVVRoWlkwNUdhVEV3WW01cGNUQk5RWEZyV2pZeVZ6aFpVM3AwWlVSYU9FUnVlbE5hUkVKcVZsaDZPV3BuZFROelJtUnhTbUptZFhRdlNHTnRaa28zV0ZCWlJ6ZHRSVlF6TTBwTkwxaGhUV3BXT0dKQ1NsWkthVzR3S3pWTmNuZDVNbGhzTlhaUWRFTnpaME5UTDNCUk1VdG5SVUlyV2tVeFFuYzFUblZCU1ZWT2VEVlhkR05OT1VkeWNEUlZNMW94YURaNmJFVTJXbkZHVTNoWlNVaDVORkI1WldoMEszQkxjMU4xTm10aWJTdFFUVWxuTVUwcmNIRkVjeTlNSzFWeldsTnZia0U0VG1wR2QzRm1VbWhMTlRObVIzQnlSemxEUzNObE4xUTBlbWt2TmxOYWJreFdiR0pyVHk5UFR6WlFWSFEyVFZoS0wwWXpOMWM0TURWV1dYUlRRMVEzVERNck5rd3piR1pyYTBSVll6WmFVamx3WnpFMFJ6UlJXRVZDTldSQ1ZDczVObWQ0TDFnMWJIUk5NVGx2TTFBemVrdDNLM1phVm5FeE5tVklSakJGZGk5RGNXMHlZMHR4TkhZeGRGUmtaMmR2UzNkeFkyVndjV3RMWlRkRVpXMVFOa3BvWVcxQ2JIcFlNbkpDVWpkYWFWSjFTRlJuY0ZVNVdVaE5lRlp6YlVsVlRVMUJTbHA2YVRZM2JHTTBTbFJ3YTB4WFZTc3hZalJ1YlhwbVRreHRXRFJVU2psTE1VeGlRekJWYVdOR1kwbEZTbVJ5ZVRSdGREaEZlSG95ZERneWExaFJUazQyYkdZNFNVdzVRVTVvY0RaclNYcFZVazVCV0ROMk5YZzFaQzk2ZHpZd1pHRlFTSGgxYUd0bVUycHdaSFZtU2pZMlkyUldhVWhwTW1KbWJubFNXbWtyVm5oVWVtSjJlQzgxYUZSd2QxaENOM1pWVFc5M2RWSmtkME5pV1d0YVNHWTNRVEl2YzNVNFVqTm9jbVZrTVU5NmRrdE5iRzl4YUdWaVVDdExTMGhIT1V0R1MyTTRaV0pPT1UxR2JsRm9kRFppVXpaSWJUZHhXRk0zYld4dU1taFZPV2xOYjJ4NGNuaHNURzVMVUhCMGNHTkphVzVJU1VRMmMzSXlNVUpDZWxoWFRHZFJXamhZWlRrNVpXUTRlRFZCTlRWQmFreGlOa2M0ZURCU1pGUkJVVWxJVms1SVMzQkNibGxvUVRsc2FURnJWV2RhWW05R1EwWjVObHBOUkZVM01WUnlSRk5aUW5sS1ZqbFVPVWxVV1ZsMFJXd3lOV1ZKWlZkSE5HTlBXa2gwVm5SalYxbGhNR0ZVVGxWTVpVWlJTSFpyWW1Odk1tcG5kMUpUVVZSWlpERnpObVpuYjFOVlVHTTBjRk5oVkhkR0wyeEtXV2hJWjBVdlZFbzVOMFpCWWpGcFEyZ3dWRmhrU3pGM2FrOVdUVUZqY210VFoySm9iV3R2UjNCbVIweFFiMlprUVdaVU1ETXdjMkZXYld4U1ZFWjJkR3hRTmtWQlUxcEJLMU5VT0V4a1ZqSnhkSEp5UjBnd1FUTldjMnBYVTJ4b1QyMUJWVE5aWWxnM2FIRXJOVUp3U21aVUt6SmlhV0YzU0VKaVlrVklWRXM0YzI1RVlsQXphbk5oLlhsVW0zLTA5aE4yeVFnSFdYVTdSUFhuTnZhWC13dTR1RlR1dkJRTXMtZnY0dmxleGhoZC1sbXRJdjgtOUVzMUVvQWZVc0tiSkJXc0RKOGM4aDlKTjd3"
}
s = requests.Session()
p = s.post('https://eu.bmstu.ru', proxies=proxy)
r = s.post('https://proxy.bmstu.ru:8443/cas/oauth2.0/callbackAuthorize?client_name=CasOAuthClient&client_id=EU', data=data, headers=userAgent)
#r = s.post('https://eu.bmstu.ru', data=data, headers=userAgent)
print(r.text)
bs = BeautifulSoup(r.text, 'html.parser')
#print(bs)