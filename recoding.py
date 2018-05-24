import json
import re
import pandas as pd 
from collections import OrderedDict
import time


def replace_all(dic):
    words = OrderedDict()
    def write_json(words):
        file = open('re_'+ file_name,'w',encoding='utf-8')
        json.dump(words, file, ensure_ascii = False,indent = 1)
            

        
#     i = 1
    j = 1
    for a, b in jdata.items():
        for roof in range(3):
            text = jdata[a][roof]
            
            text = re.sub(r"['(']\w+[')']", "", text)
            text = re.sub(r"['(']\w+\W\w+[')']", "", text)
            text = re.sub(r"\d+[일]","",text)
            text = re.sub(r"['(']\d*\W\d+\W[')']", "", text)
            text = re.sub(r"['(']\W\d*\W\d+\W[')']", "", text)
                  
            for old, new in dic.items():
                if roof == 1:
                    break
                
                text = text.replace(old, new)
            
            if roof == 0:
                text1 = text
            elif roof == 1:
                text2 = text
            elif roof == 2:
                text3 = text
                     

            if roof == 2:
                words["news%d"%j] = {"press":text2,"contents":text1,"title":text3}
                write_json(words)
                j += 1
#         i += 1
#                 
#         if i == 50:
#             break
#                
if __name__ == '__main__':
    dic = {" 은산":" 산은","국토부":"국토교통부","과기부":"과학기술정보통신부","문체부":"문화체육관광부",
           "문광부":"문화체육관광부","산업부":"산업통상자원부","행안부":"행정안전부",
           "농림축산식품부":"농림부"," 식품부":" 농림축산식품부","중기부":"중소벤처기업부",
           "기재부":"기획재정부","복지부":"보건복지부","여가부":"여성가족부"," 권익위":" 국민권익위원회 ",
           "금감위":"금융감독위원회","알바":"아르바이트","시총":"시가총액",
           "한전":"한국전력","경총":"한국경영자총협회","전경련":"전국경제인연합회","애널리스트":"애널",
           " 산은":" 산업은행"," 한은":" 한국은행","앱":"어플","어플리케이션":"어플","빚":"부채",
           "인권위":"국가인권위원회","국가국가인권위원회원회":"국가인권위원회","日":"일본","中":"중국","韓":"한국","美":"미국","英":"영국","伊":"이탈리아","銀":"은행",
           "比 ":"비교","IKEA":"이케아","KOTRA":"코트라","KOEM":"해양환경관리공단","M&A":"인수합병","KIBO":"기보",
           "KIKO":"키코","R&D":"연구개발"," FTA":" 자유무역협정","NGO":"비정부기구","IOC":"국제올림픽위원회",
           "OPEC":"석유수출기구","CIO":"기금운용본부장","SNS":"소셜네트워크서비스","ROA":"총자산이익률",
           "총자산이익률d":"총자산이익률","식약처":"식품의약품안전처","방통위":"방송통신위원회","연준":"연방준비위원회",
           "국정원":"국가정보원","한·중·일":"한국 중국 일본","한·중·러":"한국 중국 러시아","한·일·러":"한국 일본 러시아",
           "남·북·러":"한국 북한 러시아", " 남·북":" 한국 북한","북·미":"북한 미국","한·미":"한국 미국","중·러":"중국 러시아",
           "한·일":"한국 일본", " 한·러":" 한국 러시아","중·일":"중국 일본", "중·미":"중국 미국","인수.합병":"인수합병",
           "M&A(인수합병)":"인수합병", " UN ":" 유엔 ", " AI ":" 인공지능 ", " EU ":" 유럽연합 "," ELS":" 주가연계증권",
           "ROE":"자기자본이익률"," MOU":" 업무협약", " HTS":" 홈트레이딩시스템", " THAAD":" 사드", " 고고도미사일방어체계":"사드",
           "TPP":"환태평양경제동반자협정"," ETF":"상장지수펀드", " DSR":" 총부채원리금상환비율", " APEC":" 아시아태평경제협력체",
           " GDP":" 국내총생상"," USTR":" 미국무역대표부", " KAI ":" 한국우주산업 "," NAFTA":" 북미자유무역협정"," VIX":"변동성지수",
           " FRB":" 연방준비제도이사회", " BEXCO":" 벡스코", " 빚 ":" 부채 "," 검 " : " 검찰 ", " 딜 ":" 협상 ", " KT":" 케이티",
           "케이티X":"KTX", " SK":" 에스케이","에스케이C":"SKC", " LG":" 엘지", "CJ":"씨제이","애널 리스트":"애널",
           }
    
    file_name = "news_20170405.json"
    jdata = pd.read_json('./'+ file_name, encoding='utf-8')
    start_time = time.time()
    print("Recoding 시작")
    replace_all(dic)
    end_time = time.time()
    print('Recoding 끝 - %s 초' % str(end_time - start_time) )



    