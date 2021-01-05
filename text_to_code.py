line_text=""
allsymbol=["⑴","⑵","⑶", "⑷","⑸","⑹","⑺","⑻","⑼","⑽","⑾","⑿","⒀","⒁","⒂","⒃","⒄","⒅","⒆","⒇"]

#generate number of tabs with given number
def tab_build(tab_num):
    head=""
    for i in range (0,tab_num):
        head = "    "+head
    return head

#check if the variable is a int
def isInt(var):
    try:
        int(var)
        return True
    except ValueError:
         return False

#replacing all items in old to new in the text
def allReplacing(old,new,text):
    for i in range(0,len(old)):
        text=text.replace(old[i],new[i])
    return text

#generate the text part of the web page with given texts, line will be the title and line 2 will be date, and add links for comments, separate paragraphs by the <p> tag
def texts(filename,writing_data,tab_num):
    data=open(file=filename,mode="r",encoding="UTF-8")
    count,new_str,herfname,name=1,"","",""
    chapter_name=data.readline().replace("\n","").replace(" ","")
    chapter_time=data.readline().replace("\n","").replace(" ","")
    head=tab_build(tab_num)
    writing_data.write(head+"<h1>"+chapter_name+"</h1>\n")
    writing_data.write(head+"<h2>"+chapter_time+"</h2>\n")
    writing_data.write(head+"<div class=text>"+"\n")
    head=tab_build(tab_num+1)
    for line in data.readlines():
        line=line.replace("\n","")
        line_text=head+"<p>"+line+"</p><br>\n"
        need_to_be_replaced=[]
        replacing_texts=[]
        #for comment tag that is in allsymbol
        for char in line_text:
            if char in allsymbol:
                #print(char)
                herfname="#note"+str(count)
                name="back"+str(count)
                count+=1
                new_str="<a href="+herfname+" name="+name+">"+char+"</a>"
                line_text=line_text.replace(char,new_str)
        #for comment tag that is over 20 but less than 100
        for i in range(0,len(line_text)):
            if (line_text[i]=="（" )& ((i+3)<len(line_text)):
                if (line_text[i+3]=="）" )&(isInt(line_text[i+1])==True)&(isInt(line_text[i+2])==True):
                    herfname="#note"+str(count)
                    name="back"+str(count)
                    count+=1
                    old_str=line_text[i]+line_text[i+1]+line_text[i+2]+line_text[i+3]
                    new_str="<a href="+herfname+" name="+name+">"+old_str+"</a>"
                    need_to_be_replaced.append(old_str)
                    replacing_texts.append(new_str)
        line_text=allReplacing(need_to_be_replaced,replacing_texts,line_text)
        writing_data.write(line_text)
    head=tab_build(tab_num)
    writing_data.write(head+"</div>"+"\n")
    data.close()


# combine the head and the text and the tail into a web. need to give the tab number needed to fit the format 
def main(head_part,result_file_name,tail_part,texts1,tab_num):
    head_data=open(file=head_part,mode="r",encoding="UTF-8")
    tail_data=open(file=tail_part,mode="r",encoding="UTF-8")
    writing_data=open(file=(result_file_name+".html"),mode="w",encoding="UTF-8")
    for line in head_data.readlines():
        writing_data.write(line)
    head_data.close()
    texts(texts1,writing_data,tab_num)
    for line in tail_data.readlines():
        writing_data.write(line)
    tail_data.close()
    writing_data.close()
