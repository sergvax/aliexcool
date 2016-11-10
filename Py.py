import re
text="""hi you hi Больше."""
hihi="""Делиться пока всем не буду, но обещаюсь на все сделать обзоры - как раз и п\
роверим в полной мере насколько изменится цена после распродажи. Полное содержание с фото и ссылками\ 
- в посте на itao. #1111 https://ru.itao.com/item/10244232681"""
import json
kk=json.dumps(hihi)
k0k=json.loads(kk)
rt=re.compile(r'Полное содержание с фото и ссылками - в посте на itao.')
uu=rt.sub(r'',k0k.encode('utf8'), re.UNICODE)
print uu
