import json

class HttpPars:

    def __init__(self,xxx):
        self.data=xxx

    def Pars (self):
        a=self.data
        a=a.replace('\r','')
        list=a.split('\n')
        li_d=[]
        for i in list[1::]:
           if i == '':
               break
           li_d.append(i.split(': '))
        dict={}
        for o in li_d:
           dict[o[0]]=o[1]
        ty=list[0].split(' ')
        dict_z={'url': 'http://'+dict['Host']+ty[1],
                'fk': ty[0],
                'header': dict,
                'data': list[-1]
                }
        return dict_z
