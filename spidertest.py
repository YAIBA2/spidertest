__author__ = 'Administrator'
# coding=gbk
import urllib2,re,chardet

class Spider:

    def __init__(self,website):#初始化参数
        self.siteURL = website#定义要访问的链接
        self.dic={}#定义返回的字典｛网址->form表｝

    def getPage(self):#得到字符串网页信息
        kongbai=''
        url = self.siteURL
        str=''
        #print url
        request = urllib2.Request(url,headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        response = urllib2.urlopen(request)
        if 'html' not in response.info().get('content-type'):
            print('111111111111111111111111111111')
            return kongbai
        #return response.read().decode('gbk')
        '''while 1:
            data=response.read(2048)
            str+=data
            if not len(data):
                break'''
        data=response.read()
        encoding_dict = chardet.detect(data)
        #print encoding
        web_encoding = encoding_dict['encoding']
        if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
            html = data
        else :
            html = data.decode('gbk','ignore').encode('utf-8')
        str=html
        #print(str)
        str1=str.replace("\n","")
        return str1
    def getPage1(self,urll):#得到字符串网页信息
        kongbai=''
        url = urll
        str=''
        #print url
        request = urllib2.Request(url,headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        })
        try:
            response = urllib2.urlopen(request,timeout=3)
        except:
            return kongbai
        if 'html' not in response.info().get('content-type'):
            return kongbai
        #return response.read().decode('gbk')
        '''while 1:
            data=response.read(2048)
            str+=data
            if not len(data):
                break'''
        data=response.read()
        encoding_dict = chardet.detect(data)
        #print encoding
        web_encoding = encoding_dict['encoding']
        if web_encoding == 'utf-8' or web_encoding == 'UTF-8':
            html = data
        else :
            html = data.decode('gbk','ignore').encode('utf-8')
        str=html
        #print(str)
        str1=str.replace("\n","")
        return str1
    def matchform(self,str1):#输入网页字符串，得到form表
        str1=str1.replace("\t","")
        str1=str1.replace("\r","")
        pattern = re.compile(r"<form.*?</form>")
        return re.findall(pattern,str1)
    def getzidain(self,list):#输入form表，得到字典
        self.dic[self.siteURL]=list
        #print(self.dic)
        return self.dic
    def getwebsite(self,str):#输入网页字符串，得到所有网页链接表
        #str=self.getPage()
        kongbai=[]
        if len(str)==0:
            return kongbai
        pattern = re.compile('\.(.*?)\.com')
        goal=re.search(pattern,self.siteURL)
        try:
            haha=goal.group(1)
        except:
            haha='你'
        pattern = re.compile(r'href=\"(.+?)\"')
        #print len(re.findall(pattern,str))
        dict={}
        list=[]
        list1=[]
        list2=[]
        list3=[]
        for a in re.findall(pattern,str):
            if a.find(haha)!=-1:
                if a.find('http')==-1:
                    if a.find('/')==0:
                        if a.find('//')!=-1:
                            a='http:'+a
                        else:
                            a=self.siteURL+a
                    else:
                        a=self.siteURL+'/'+a
                b=[a,'']
                dict[b[0]] =b[1]
            else:
                if a.find('http')==-1:
                    if a.find('/')==0:
                        if a.find('//')!=-1:
                            a='http:'+a
                        else:
                            a=self.siteURL+a
                    else:
                        a=self.siteURL+'/'+a
                b=[a,'']
                dict[b[0]] =b[1]
        for e in dict.items():
                list1.append(e[0]+e[1])
        for c in list1[:]:
            match=re.search(r'.*\?.*?=',c)
            if match:
                k=match.group(0)
                if k not in list3:
                    list3.append(k)
                    list2.append(c)
                for d in list1[:]:
                    if d.find(k)!=-1:
                        list1.remove(d)
        list1.extend(list2)
        return list1
        #return re.findall(pattern,str)
    def getcanshu(self,dic):#输入字典，得到相应信息表单
        all=[]
        panduan=["checkbox","text","password","radio","hidden","select","textarea"]
        for a in dic.values()[0]:#[0]
            pattern = re.compile(r'<input.*?>|<textarea.*?>|<select.*?</select>',re.I)
            #print(re.findall(pattern,a))
            for b in re.findall(pattern,a):
                c=[]
                pattern = re.compile(r'type.*?=.*?\"(.+?)\"',re.I)
                if re.findall(pattern,b):
                    c.append(re.findall(pattern,b)[0])
                elif b.find("textarea")!=-1:
                    c.append("textarea")
                elif b.find("select"):
                    c.append("select")
                '''pattern = re.compile(r'name.*?=.*?\"(.+?)\"',re.I)
                if len(re.findall(pattern,b))!=0:
                    c.append(re.findall(pattern,b)[0])
                else:
                    c.append('')'''
                pattern = re.compile(r'name()*=()*"(.*?)"',re.I)
                if re.findall(pattern,b):
                    for g in re.findall(pattern,b):
                        c.append(g[2])
                else:
                    c.append('')
                pattern = re.compile(r'value()*=()*"(.*?)"',re.I)
                if re.findall(pattern,b):
                    guodu=[]
                    for g in re.findall(pattern,b):
                        guodu.append(g[2])
                    c.append(tuple(guodu))
                    #print(re.findall(pattern,b))
                else:
                    c.append(())
                all.append(c)
        #print(all)
        chuli=[]
        for d in all:
            if d[0] not in panduan:
                chuli.append(d)
        for k in chuli:
            all.remove(k)
        chuli1=[]
        for e in all:
	        for f in all:
		        if e!= f and e[0]==f[0] and e[1] ==f[1]:
			        e[2]=e[2]+f[2]
			        chuli1.append(f)
        for l in chuli1:
            all.remove(l)
        return all
    def getallform(self):#得到所有列表字典
        allform={}
        str1=self.getPage()
        list=self.getwebsite(str1)
        for a in list:
            wangye=self.getPage1(a)
            formlist=self.matchform(wangye)
            allform[a]=formlist
        for k, v in allform.items():
            if not v or k.find('?')==-1:
                allform.pop(k)
        return allform



spider = Spider("http://10.206.10.113/news.php")#初始化Spider类，并构造初始访问链接
str1=spider.getPage()#得到网页信息
print(str1)
list=spider.matchform(str1)#得到form
dictd=spider.getzidain(list)#得到字典
print(list)
print(dictd)
print(spider.getwebsite(str1))#输出网页链接
print(spider.getcanshu(dictd))#输出相关信息
#print(spider.getallform())
