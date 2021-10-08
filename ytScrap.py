from googleapiclient.discovery import build
from openpyxl import Workbook

wb=Workbook()

sh1= wb.active

youTubeApiKey="your API Key" #Input your youTubeApiKey
youtube=build('youtube','v3',developerKey=youTubeApiKey)

channelId=['UCmxp1KvhefCnc1s2L6SCEJg','UCEg3PHVR0vt3azbs_Qk_6cw','UCM75YqEHqzuFHPmLVMdzNDQ','UCqaq3Cwa7m_EsqlvfZh6uyw','UCkTXMfsPsnOCg7D9lR_PLxw','UCiGyWN6DEbnj2alu7iapuKQ','UCZJMKAMHuMy7FYvYDWF5D8A','UC1RLXeKkSJZqfrPoQTDLY3A','UCDG_YP69cl42ly3pPy8-Liw','UCF7BExjT2zH_mmyqOB139Dg','UC4M31l-PzsdqmZJ0D5GTlIA','UCv06iqIq-K7HyST9hy5-n7w','UCE1zr1ZeBJrVJX3SMxaFafA','UCW1JJIpmA4z4EyIUllxwKEQ','UCplMtixZJ6pRcrMogBSYvuQ','UC3HS6gQ79jjn4xHxogw0HiA','UCswldWR9-svuCV0lBgHhDcQ','UC8zCnnfhz-dvIpVdZ1CheuA','UCD16eo98AXl-9T61Xd711kQ','UClaQJq84XMtMkL44zDmL-Tg','UCZNNx4KYmCkwxCLdsHyWqQA',
'UCck8RejS9Ug2fbTYcGVBwjA','UCgBmfNILAlXmGv3CsJ8oFJA','UCRXKFHtNEIW_1l2-DarXkwg','UCeIGz7wYzCSc1ysX6s4j0Vg','UCNAgR0h4qsEecj3SMMxkNWg','UCL2n1iNbGv2DioRdL6R8JPw','UC34qgLijjhpbpFiorTopc-A','UCYIP22_9qalMrddUQAM_uQQ','UCmXZxX_qexEZxhb5_vQKPCw','UC1-ZdFLBukC6fTZ8QRWvpDw','UCcv7pspGHmM7AOywuLM1ufA','UCci7QVXlrky8ADCm0rU_bUg','UCp1T3Oi6gaNy7cngeEfQ09g','UCwdvPgmU5qHPB2NsDLAmS1g','UCQiiN7IuRQlyHJ_MYMhf-Fw','UCVUjsfIErUfWI57ep1L7B6Q','UCfSUSGxsZBBE3o8bCQpqYgw','UC3VBTDYqrPTUNmXb1LU11cw','UC91RZv71f8p0VV2gaFI07pg','UCxDZB1i0azOgHUiPOTUSzhA','UCPp_JZZBXm5vNKymdBPcutg','UCszBOnGoy1kOYEA9O032VXg','UCLJInIQjBs8VBHFNkpdAzYA','UCq9ZY6x66tyPTAYF0GaXVow','UCan6AI1ASU12XvVTom1WglQ','UCVJU_IChPMOe8RWkdVQjtfQ','UCYIET4VzyU9-vIJhDYNzHPg','UCqG4kKcytk7w90rl9Oia8Tg','UC6WeBGasfkDuIhuLFE8cq4g','UC08KXHLH9REGAP20xdhCmAA','UCD9gJ0CoGT4TFk3qQsdyNyg','UCAuzWUDsz28MDsv2yUgkuCw','UConPUBSiB7UkdMH2nkYzxAA','UCAsfTWBy1A29Uh8mUzqbb3A','UCbVus-Tz4pL8j7zPoQ--amA','UCn8mnhabljpjSwk0e08DhDA','UCvjRa2jVhKVSbVDG85vKGww','UCIForhLpzvRTVFP1ZUy-qJw','UCABe2FgVNv2hgBeMu2mySVg','UCddnJhXMUxzHoH8AZkZSd8w','UCHnj59g7jezwTy5GeL8EA_g','UCNn75PJi2J5OmZGuLCZGJPg','UCpyc1eTpM1cA3P0ZWym4clw','UC4iQ2IOqg5dKbnzsAxRyKWQ','UC54_FxusAgaXzFXp4udeJNg','UCDkVt3Wrl_I_E2wXNmQjZOA','UC82ObtDCmUuWwrWhpQsX-HQ','UCiGxYawhEp4QyFcX0R60YdQ','UCI3WTQ69lNt0_3FbyWKkLlw','UC7px6OmooQLmsJlYACR_n-A','UC2R0nGlj407CXb6nQYyDfRw','UCDxJZ_KbL6n_hhHScI6LQQw','UCQiHxih_RTETf4YHgpoTuAw','UC52kszkc08-acFOuogFl5jw','UCLGy-hNHishDHm1-ZTReepA','UCdQwYksctqqiRwqp3PiJMWA','UCtKAQhsa1D_zKbc3yZmwARQ','UCLoSA4APnVIgkMSCvUq0PBQ','UC8jD2MO_NUnI-TASWQp-7NQ','UCsc28TBbgs_HB86DQQD9nSw','UCYbFCdcMfA68ZvJO__zTUjg','UCC_xseF88QUPlQa5baYeoVw','UCcxP3vMEVVFafLBasCHcjCg','UCVSGbBg_gMwr4QpeRHMgyGg','UCe5YkOlh2sy_JdRUDfge-lQ','UC24K8-tMIa04qt61Npiv5KQ','UC67MIt3dUCKlyMnN7GP9PPQ','UCgVg6dmZHCxze_ay0bolPew','UCjchmjvdJYNJggu0xsLESWA','UCyCOVQyFKMYGzCGDdpEw0eg','UCG6JaN60ZwTEPk3rE8Sjq_w','UCS1L9B6Swy1WVXOMWgJuMuw','UCJo3pC-Qc6ixLnyKyPr0xUg','UCGG5KRz0zakIC79AR2XeN0g','UC2kmtc7dn67YVmQypoysSHw','UC3wQ-HF4qpZVEUwWAzgRySw','UC3jRLEhGmwGihgNRkp8-a9Q','UCszNnMo0djZHNnldrbo-u4w','UC4SUQzurYVmGwgmfdn0yEVg','UCUX2NIPzZXT87MI7zLm5vQg','UCewX35iliR0kxNukRJBvbSw','UC-e7hYodxRznN2WhtXG9oDw','UCV0EFgPoRPrD2Vuoob4B6Cw','UCf3LwfCIZk1UOt3AHu4hMtg','UCt8OFYyeXWmu8jiLU3hUwjw','UCLsKmd5ECiJNLeXYRtsvwFA','UCrO9fUHE3gjlBc0Gv0EMKQg','UC6CmRw2o140-8po9z_m_6vg','UCwMNVCXcSWNMS0C8rcRCWxA','UCRL9A_CZEdusNZ6v3nCAu7Q','UCGbQ1bYN0TcYzSc5rMp37Jg','UCrSfTMiVxoPp_WbekiNAtXg','UC71BmRUuyTDNy06AZIy0K4A','UCObWXIaGPPVjX_RJgYDbB1w','UCamq_hyE57q7nWbr4pAH-wg','UChnGh24uXqSBwuh-HtnOHvw','UC-OcwSgK1K7jh1OvRuqcXpA','UCpjUOovOjTMeLVx92bbdO8A','UCsbgKSfetDwnD9XR7T-Sk5g','UC9jUBgBdkkAOXmvQ9kKHj0w','UC04e1vy95lGjggcYbwgbOfw','UCfl4OhoOv8xF64D5KzJinnA','UCSi6Aa72Rxx-ZLiiUVfO_6A','UCPY1eI0L1MZVFUjE11BBvGA','UCrC8mOqJQpoB7NuIMKIS6rQ','UCwBfgxcxKUzlhpEMJxWEmdg','UCBhb6moazTePlPpDj07H0jg','UCcErZD9wUPQONYaoRXWX-hw','UC4a-Gbdw7vOaccHmFo40b9g','UCDOAygE2Smt9jWB7xpQo6iQ','UCOO6eNPW21LZP7IlaRJQB7Q','UC4wKhLjYfMFPEYI1D5Erc-Q','UC8Z_fpEYLtBu3-OuhJGqLZg','UCeAnrUKcxFGrMXfHgj0eMjg','UCR3F3TPXHqXpotvmpyqXeQg','UCXqz2Af0OZMGG3pTxbEXZ8A']

l1=[("Channel Id","View Count","Subscriber Count","Video Count")]

l1=[("Channel Id","View Count","Video Count","Subscriber Count")]
for i in channelId:
    snippetdata=youtube.channels().list(part='statistics',id=i).execute()
    stats= snippetdata['items'][0]["statistics"]
    temp1=[]

    temp1.append(i)

    viewCount=stats['viewCount'] 
    temp1.append(viewCount)


    videoCount=stats['videoCount']
    temp1.append(videoCount)

    try:
        subsCount=stats['subscriberCount']
        temp1.append(subsCount)
    except:
        temp1.append("Not Available")

    tup1=tuple(temp1)

    l1.append(tup1)


for i in l1:
    sh1.append(i)

wb.save("Report.xlsx")