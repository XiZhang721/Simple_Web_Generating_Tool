line_text=""
allsymbol=["⑴","⑵","⑶", "⑷","⑸","⑹","⑺","⑻","⑼","⑽","⑾","⑿","⒀","⒁","⒂","⒃","⒄","⒅","⒆","⒇"]
#count=1
def tab_build(tab_num):
    head=""
    for i in range (0,tab_num):
        head = "    "+head
    return head


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
        for char in line_text:
            if char in allsymbol:
                #print(char)
                herfname="#note"+str(count)
                name="back"+str(count)
                count+=1
                new_str="<a href="+herfname+" name="+name+">"+char+"</a>"
                line_text=line_text.replace(char,new_str)
        writing_data.write(line_text)
    head=tab_build(tab_num)
    writing_data.write(head+"</div>"+"\n")
    data.close()



def main(head_part,result_file_name,tail_part,texts1,tab_num):
    head_data=open(file=head_part,mode="r",encoding="UTF-8")
    tail_data=open(file=tail_part,mode="r",encoding="UTF-8")
    writing_data=open(file=(result_file_name+".html"),mode="w",encoding="UTF-8")
    for line in head_data.readlines():
        writing_data.write(line)
    head_data.close()
    #writing_data.close()
    texts(texts1,writing_data,tab_num)

    for line in tail_data.readlines():
        writing_data.write(line)
    tail_data.close()
    writing_data.close()


