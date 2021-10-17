import requests
#写的很随意，凑合用吧..
# 定时 0 * * * *
#填入你的cookie↓↓↓
num_list = ['','']

i = 0
url = 'https://m.jingxi.com/jxbfd/user/ExchangePearlHb?__t=1632107733456&strZone=jxbfd&dwLvl=10&dwIsRandHb=0&ddwVirHb=500&strPoolName=anhjZmQyX2V4Y2hhbmdlX2hjaGJfMjAyMTA5&dwExchangeType=0&_stk=__t%2CddwVirHb%2CdwExchangeType%2CdwIsRandHb%2CdwLvl%2CstrPoolName%2CstrZone&_ste=1&h5st=20210920111533457%3B3136282999556162%3B10032%3Btk01w6cc71aaf30nWiQ63gx5v2Y4lfuEDC6ElLDhj0c6sT9q10GDU4rOUKl0Gpy%2BuQ3uEb3%2FKjKb4MjF1aCtQukO4CLj%3B2ea9578edf0ef31ef3b14b30c6082367b3a16115d34756b0c6f27afe77a9a278&_=1632107733462&sceneval=2&g_login_type=1&callback=jsonpCBKH&g_ty=ls%0D%0A';
while i < len(num_list):
   if num_list[i] == 2:
       num_list.pop(i)
       i -= 1
   else:
       header = {
       'Host':'m.jingxi.com',
       'user-agent':'dpingou;android;5.3.0;11;65df54b15883bd4c;network/wifi;model/PEEM00;appBuild/18113;partner/meizu01;;session/230;aid/65df54b15883bd4c;oaid/;pap/JA2019_3111789;brand/OPPO;eu/9326666383335326;fv/1663738363236623;Mozilla/5.0 (Linux; Android 11; GM1910 Build/QKQ1.200223.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36',
       'accept':'*/*',
       'Referer':'https://st.jingxi.com/fortune_island/index2.html?ptag=7155.9.47&sceneval=2',
       'cookie':num_list[i]
          }
       print("正在执行")  
       print(i)  
       ret=requests.get(url=url,headers=header)
       print(ret.text)
       i += 1
