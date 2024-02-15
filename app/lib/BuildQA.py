from config import QA_CONTENT, QA_FIG_DIR


def buildQA():
    all_qa=[] ## QA 資料

    with open(QA_CONTENT,"r",encoding="utf-8") as qa:
        id=1 ## QA 的編號


        for line in qa:
            
            load_line=line.replace("\n", "").split(',')
            print (load_line)
            
            ## 單個 QA 資料
            question={'id':id,
                'question':load_line[0],
                'answer':load_line[1],
                'fig':QA_FIG_DIR+load_line[2]}
            

            all_qa.append(question)
            id+=1

        n2=int(len(all_qa)/2) ## 分兩欄的位置
        all_qa={'l':all_qa[:n2],'r':all_qa[n2:]} ## 兩欄
    
    return all_qa
