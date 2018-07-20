#!/usr/bin/env python2
from hashlib import sha256
from Cryptodome.Cipher import AES
BLOCK_SIZE=16
def unpad(p):
    return p[0:-ord(p[-1])]
def decrypt(msg,key):
    data = msg.decode('hex')
    IV, data = data[:BLOCK_SIZE], data[BLOCK_SIZE:]
    aes = AES.new(key, AES.MODE_CBC, IV)
    m = unpad(aes.decrypt(data))
    return m

p = 174807157365465092731323561678522236549173502913317875393564963123330281052524687450754910240009920154525635325209526987433833785499384204819179549544106498491589834195860008906875039418684191252537604123129659746721614402346449135195832955793815709136053198207712511838753919608894095907732099313139446299843
g = 41899070570517490692126143234857256603477072005476801644745865627893958675820606802876173648371028044404957307185876963051595214534530501331532626624926034521316281025445575243636197258111995884364277423716373007329751928366973332463469104730271236078593527144954324116802080620822212777139186990364810367977
A = 60599224471338675280892530751916349778515159413752423808328059701102187627870714718035966693602191072973114841123646111608872779841184094624255525186079109811898831481367089940015561846391171130215542875940992971840860585330764274682844976540740482087538338803018712681621346835893113300860496747212230173641
B = 41577936475113646062415839313533664222336390873095585592257233546410748309845182921273101711259044469844745154398797450729717767422505327649336923087518273833440859523881791932947163012973287757609314935398468435619627316484481259644562078527117416504710807415325721826304371028711933641605633408713301811494
a = 33657892424673

K = pow(B, a, p)
KEY = sha256(str(K)).digest()

messages = [
	"ffed2b87861bd6feab7b995c8bbc7c9af4a0e37e7ae8e861a3fc5fcd32aa10233f2195150f863349315a3fac7a56c54051c3714a38dc7c1014c6929c2027ecb9",
	"452d11ce48746b405ede2b3d460e508aae237618503cb6e524ba0cbc3d133753b96a07466d96cb02a08add58ba313c14",
	"b46607855c1ce5189a95dd2131208fc2777083baa40f488aa6f3056b9426ae569e71aaa91768ee0abff5556ee1d7d6f4",
	"698647ce3244f5a450bf7a80b6c7096bdf8320ee41e71d414da9cf7b7a37fde4",
	"62216d83b780e7d86a02333e68e09a93104725fa60e829a37b456b04749e883e",
]

for i,msg in enumerate(messages):
	print "[Message %d:%s]"%(i,decrypt(msg,KEY))