import os
import sys
import binascii
import socket
import struct
import multiprocessing, tempfile
from queue import Queue
from collections import deque
import csv
import time
#import thread
import threading
import socket,threading
from collections import OrderedDict
class myThread(threading.Thread):
    def __init__(self, threadID, name, filename):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.filename=filename
        self._return=None
    def run(self):
       #if self.Thread is not None:
            print ("Starting " + self.name)
            self._return=FileRead(self.name,self.filename)
            
            print ("Exiting " + self.name)
    def join(self):
        threading.Thread.join(self)
        return self._return
    
class Router:
            """ This is the class for the router object.
                Functions in this class - connect, receive, forward
            """

            def __init__(self, name, address):
                ''' Assigns the hostname and IP address to the router
                '''
                self.name = name
                self.address = address

            def connect(self, device):
                """ This function takes the device connecting to the switch and adds it
                    to a list of connected devices. This function also maintains a
                    dictionary of devices and the ports to which they are connected.
                """
                print('Connecting %s to %s' % (device.name, self.name))

                self.device = device
                self.hostnames = []

            def input1(self,packet):
                self.packet=packet
                

            def input2(self, packet):
                self.packet = packet
                

            def input3(self, packet):
                self.packet = packet
        
class ProcessClass(multiprocessing.Process):
    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.func = func
    def run(self):
        for arg in iter(self.in_queue.get, None):  # None is the sentinel
            self.func(arg, self.out_queue)
            self.in_queue.task_done()   
        self.in_queue.task_done()


  
queue11 = multiprocessing.Queue()
queue12 = multiprocessing.Queue()
q12b=multiprocessing.Queue()
q12bb=multiprocessing.Queue()
queue121=multiprocessing.Queue()
queue13 = multiprocessing.Queue()
q13b=multiprocessing.Queue()
q11b=multiprocessing.Queue()
queue21 = multiprocessing.Queue()
q21b=multiprocessing.Queue()
q21bb=multiprocessing.Queue()
queue22 = multiprocessing.Queue()
q22b=multiprocessing.Queue()


queue23 = multiprocessing.Queue()
q23b=multiprocessing.Queue()
q23bb=multiprocessing.Queue()
q231b=multiprocessing.Queue()
queue231 = multiprocessing.Queue()

queue31 = multiprocessing.Queue()
queue32 = multiprocessing.Queue()
queue33 = multiprocessing.Queue()
q32b=multiprocessing.Queue()
q33b=multiprocessing.Queue()





#minPackLeng=min(PacketLength1,PacketLength2,PacketLength3,PacketLength4, PacketLength5,PacketLength5,PacketLength6)


def readforword():
    #speed= input("Enter the mean arrivate rate if in packets/ second ")
    fwd_table = 'E:/Ph4ForwardingTable'
    with open(fwd_table,'rb') as f:
        #print ("Reading Forwarding Table")
        content=f.read()
        global k
        k=[]
        v1=[]
        v2=[]
        v3=[]
        v4=[]

        try:
            i=0
            for line in content:
               
            
                hex_content=(binascii.hexlify(content))
                
                r1=8+(i*44)
                r2=16+(i*44)
                r6=16+(i*44)
                r7=24+(i*44)
                r3=33+(i*44)
                r4=34+(i*44)
                r5=35+(i*44)
                r8=36+(i*44)
                r9=36+(i*44)
                r10=38+(i*44)
                #print ("hi")
               
                i=i+1
                d1=hex_content[r1:r2]
                hex2dec=int(d1,16)
                hex2decstr=str(hex2dec)
                '''
                print (hex2decstr)
                print ("H")
                '''

                
                dest_mask=hex_content[r6:r7]
                #print (dest_mask)
                hex2desmask=int(dest_mask,16)
                #print (hex2desmask)
                #print ("hello")
                hex2decmaskstr=str(hex2desmask)
                
                p1=hex_content[r3:r4]
                hex2dec1=int(p1,16)

                

                pQ=hex_content[r5:r8]
                hex2decportQueue=int(pQ,16)
                #hex2decportQueuestr=str(hex2decportQueue)
                Dscp = hex_content[r9:r10]
                hex2decdscp = int(Dscp, 16)

                dest_address= hex2decstr.ljust(8,"0")
                dest_add_int= int(dest_address)
                packed_dest=struct.pack("!L",dest_add_int)
                dest_final_add=socket.inet_ntoa(packed_dest)
                dest_f= dest_final_add
              

                dest_mask_addr=hex2decmaskstr.ljust(8,"0")
                dest_mask_int=int(dest_mask_addr)
                packed_dest_maddr=struct.pack("!L",dest_mask_int)
                packed_final_dma=socket.inet_ntoa(packed_dest_maddr)
                dest_dma=packed_final_dma
               
                
                
                k.append(dest_f)
                v1.append(dest_dma)
                v2.append(hex2dec1)
                v3.append(hex2decportQueue)
                v4.append(hex2decdscp)
                
                
            
                '''
                print ("k",k)
                print (v3)
                print (v)
                print (v2)
                print (v4)
                '''

               
            
        except:
            print ("Forwarding Table read \n ")
    '''    
    print("start")
    print (k)
    '''
    global add_mask
    global add_port
    global add_portqueue
    add_mask=OrderedDict(zip(k,v1))
    add_port=OrderedDict(zip(k,v2))
    add_portqueue=OrderedDict(zip(k,v3))


def CommonPrefix(s1, s2):
    out = ''
    for i, j in zip(s1, s2):
        if i != j:
            break
        out += i
    return out

def FileRead(threadName,filename):
        #file= 'E:/Ph3Link1_MM1'
        pks=0
        j=0
        tot_length=0
        offset=0
        s1=0
        s2=0
        s3=0
        global q11
        global q12
        global q13
        global q21
        global q22
        global q23
        global q31
        global q32
        global q33
        global q12a
        global q12aa
        global q13a
        global q21a
        global q21aa
        global q22a
        
        global q23a
        global q23aa
        global q231
        global q231a
        
        global q32a
        global q33a
        
        q11=0
        q12=0
        q12a=0
        q12aa=0
        q13=0
        q13a=0
        q21a=0
        q21aa=0
        q22a=0
        q23a=0
        q23aa=0
        q231a=0
        q32a=0
        q33a=0
        
        q21=0
        q22=0
        q23=0
     
        q31=0
        q32=0
        q33=0
        q231=0
        global sum_q11
        sum_q11=0
        global sum_q12
        sum_q12=0
        global sum_q121
        sum_q121=0
        global sum_q13
        sum_q13=0
        global sum_q11b
        sum_q11b=0
        global sum_q21
        sum_q21=0
        global sum_q22
        sum_q22=0
        global sum_q23
        sum_q23=0
        global sum_q231
        sum_q231=0
        
        global sum_q31
        sum_q31=0
        global sum_q32
        sum_q32=0
        global sum_q33
        sum_q33=0
        
                
       
        
        #return (v1)
        with open (filename,'rb') as f:
                #content=f.read()
                
                #packet=content
            try:
                for packets in range(0,65555):#this will be the no of time the loop would run ,i.e number of packet
                    #f.seek(offset)
                    packet=f.read()
                    #packet=packet[0]
                    
                    eth_length=14
                    
                    ip_header = packet[0:20]
                    #print ("New")
                    #print (ip_header)
                    iph = struct.unpack('!BBHHHBBH4s4s' , ip_header)
                    version_ihl = iph[0]
                    #print("version")
                    #print (version_ihl)
                    version = version_ihl >> 4
                    ihl = version_ihl & 0xF
                    iph_length = ihl * 4
                    tot_length=iph[2]
                    #print("Length")
                    #print (tot_length)
                    ttl = iph[5]
                    protocol = iph[6]
                    s_addr = socket.inet_ntoa(iph[8]);
                    d_addr = socket.inet_ntoa(iph[9]);
                    dest=[]

                    #print ('#IPHEADER# ' + 'Version : ' + str(version) + ' IP Header Length : 20 bytes' + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr))
                    offset=tot_length+offset
                    f.seek(offset)
                    pks=pks+1
                    
                   
                    subnet_add=list()
                    for destadd,destmasks in add_mask.items():
                      anded = list()
                      for ip, m in zip(d_addr.split('.'),destmasks.split('.')):
                           anded.append(str(int(ip) & int(m)))
                      subnet = '.'.join(anded)
                      subnet_add.append(subnet)
                      #print ("Subnet:")
                      #print (subnet)    #this is and of destination IP of pack and subnetmask
                      
                    temp_dic_key = {}
                    temp_dic_value = {}
                    for subnt in subnet_add:
                      temp_dic_1 = {}
                      for ip_ori in k:
                        temp_dic_1[ip_ori]=len(CommonPrefix(subnt,ip_ori))
                      # print (temp_dic_1)
                      temp_dic_key[subnt] = max(temp_dic_1, key=temp_dic_1.get)  #highest ip match
                      temp_dic_value[subnt] = temp_dic_1[max(temp_dic_1, key=temp_dic_1.get)]   #highest value
                    got_it = temp_dic_key[max(temp_dic_value, key=temp_dic_value.get)]
                    #print (got_it)
                    if(got_it in k):
                      #print("Presetnt")
                      value=add_port[str(got_it)]
                      value1=add_portqueue[str(got_it)]
                      #print (value,value1)
                      
                      if(value==1):
                          s1=s1+1
                          if(value1 == 1):
                              if(got_it=='177.215.64.0'):
                                  q11+=1
                                  queue11.put(packet)
                                  #print (tot_length)
                                  sum_q11+= tot_length
                              else:
                                  q11b.put(packet)
                                  sum_q11b+=tot_length
                                  
                             # time.sleep(PL1)
                          elif (value1 ==2):
                                #r2-r4-r7-out
                                if (got_it=='183.216.160.0'):
                                    q12+=1
                                    queue12.put(packet)#r2-queue
                                    q12a=queue12.get()
                                    q12b.put(q12a)#r4-queue
                                    q12aa=q12b.get()
                                    q12bb.put(q12aa)#r7-queue-> write q12bb to link
                                    sum_q12+=tot_length
                                else:
                                    queue121.put(packet)#r2-queue
                                    sum_q121+=tot_length
                                    
                          
                          else: 
                              q13+=1
                              queue13.put(packet)#r2-queueu
                              q13a=queue13.get()
                              q13b.put(q13a)#r4->write q13a to link
                              sum_q13+=tot_length
                            
                      if(value==2):
                          s2=s2+1
                          if(value1 == 1):
                              q21+=1
                              queue21.put(packet)#r3
                              q21a=queue21.get()
                              q21b.put(q21a)#r2-queue
                              q21aa=q21b.get()
                              q21bb.put(q21aa)#r4-queue write out to link
                              sum_q21+= tot_length
                            #  time.sleep(PL3)
                             
                              
                          elif (value1 == 2):
                              q22+=1
                              queue22.put(packet)#R3
                              q22a=queue22.get()
                              q22b.put(q22a)#r5-queue write out to link
                              sum_q22+= tot_length
                              
                             # time.sleep(PL4)
                              
                          elif (value1 == 3) :
                              
                              if (got_it=='200.177.144.0'):
                                  q23+=1
                                  queue23.put(packet)#r3
                                  q23a=queue23.get()
                                  q23b.put(q23a)#r5
                                  q23aa=q23b.get()
                                  q23bb.put(q23aa)
                                  
                                  sum_q23+= tot_length
                                  
                              else :
                                  q231+=1
                                  queue231.put(packet)#r3
                                  q231a=queue231.get()
                                  q231b.put(q231a)#r7-->write out
                                  
                                  sum_q231+= tot_length
                                  
                                  
                              

                      if(value==3):
                          s3=s3+1
                          if(value1 == 1):
                              q31+=1
                              queue31.put(packet)#r5-> write out
                              sum_q31+= tot_length
                            #  time.sleep(PL5)
                              
                              
                          elif (value1==2):
                              q32+=1
                              queue32.put(packet)#r5
                              q32a=queue32.get()
                              q32b.put(q32a)#r6->write out
                              sum_q32+= tot_length
                           #   time.sleep(PL6)
                               
                          else :
                              q33+=1
                              queue33.put(packet)#r5
                              q33a=queue33.get()
                              q33b.put(q33a)#r6
                              
                              sum_q33+=tot_length


            except Exception as ex:
                    print (ex)
                    print ("End of file")
                    #print "i"
        print ('\n')    
        print (' Packets out from router 1 from each file  '+ str(pks)+ "Port 1:" + str(s1)+ ' Port 2:' +str(s2)+ ' Port 3 :' +str(s3)+'\n')
        #print ('Queue Depth=>'+'Q11 : ' +str(q11) +' Q12 : ' +str(q12)+  'Q13:' +str(q13) +' Q21 : ' +str(q21) + ' Q22 : ' +str(q22) +' Q23 : ' +str(q23) +' Q31 : '+str(q31)+'\n')

   
        
              
        

        
if __name__ == "__main__":

    router1 = Router('r1', '01')
    router2 = Router('r2', '02')
    router3 = Router('r3', '03')
    router4 = Router('r4', '04')
    router5 = Router('r5', '05')
    router6 = Router('r6', '06')
    router7 = Router('r7', '07')
    router1.connect(router2)
    router1.connect(router3)
    router1.connect(router5)
    router2.connect(router4)
    router3.connect(router7)
    router5.connect(router6)
    router4.connect(router7)
    router7.connect(router6)


    
    
    readforword()

    add_mask['212.18.32.0'] = '255.255.224.0'

    print (k)
    print (add_mask)
    print (add_port)
    print (add_portqueue)
    
    #filename= 'E:/Ph3Link1_MM1'
    file1=str(input("Enter the path for the File 1 : "))
    print ("\n")
    file2=str(input("Enter the path for the file 2: "))
    print ("\n")
    file3=str(input("Enter the path for the file 3: "))
    print ("\n")
    
    
    thread1=myThread(1,"Thread1",file1)
    thread2=myThread(2,"Thread2",file2)
    thread3=myThread(3,"Thread3",file3)
    
    print ("Enter")
    thread1.start()
    thread2.start()
    thread3.start()
    list1=[]
    list2=[]
    list3=[]
    print (" Exit!")
    a1=thread1.join()
    list1.append(a1)
    a2=thread2.join()
    list1.append(a2)
    a3=thread3.join()
    list1.append(a3)
    # TimeQ11=0
    # timmeq12=0
    

    #a=thread1.join()+ thread2.join()+thread3.join()
   

    

   
    print ('---------------------------------------------------')
    print ('Mean Packet Size Entering Routers per destination address')
    print (sum_q11/(q11))
    print (sum_q12/(q12))
    if(q13 != 0):
        print (sum_q13/(q13))
    else:
        print ('0')
    
    print (sum_q21/(q21))
    if(q22 != 0):
        print (sum_q22/(q22))
    else:
        print ('0')
    if(q23 != 0):
        print (sum_q23/(q23))
    else:
        print ('0')

    
    print (sum_q31/(q31))
    if(q32 != 0):
        print (sum_q32/(q32))
    else:
        print ('0')
    if(q33 != 0):
         q33s=sum_q33/(q33)
         print (q33s)
    else:
        q33s=0
        

    print ("-----------------------------------------------------")
   
    #filename= 'E:/Ph3Link1_MM1'
    link1 = open('abc1', 'ab+')
    link2 = open('abc2', 'ab+')
    link3 = open('abc3', 'ab+')
    link102=open('abc4', 'ab+')
    link107=open('abc5', 'ab+')
    link104=open('abc6', 'ab+')
    link105=open('abc7', 'ab+')
    link106=open('abc8', 'ab+')
    link1021=open('abc8', 'ab+')

    print (" Priority Scheduling based on class for different DSCP : \n")
     
   

    t11=0
    t12=0
    t13=0
    t21=0
    t22=0
    t23=0
    t31=0
    t32=0
    t33=0
    t331=0
    t3311=0
    
    t1i=time.time()
    t2i=time.time()
    t3i=time.time()
   
   
    
        
            
    while (((q33b.qsize())>0)):
        
            a=q33b.get()
            link3.write(a)
            if q33b.empty():
                break
            t11+=(time.time())-t1i
    

    while (((q23bb.qsize())>0)):
    
      #for k in range(0,wt2):
       
        b=q23bb.get()
        link106.write(b)
        #print ((queue12).qsize())
        if q23bb.empty():
            break
        t12 += (time.time())-t1i
      #time.sleep(PL2)
       
    
    while (((q231b.qsize())>0)):
      #for p in range(0,wt7):
        g=q231b.get()
        link2.write(g)
        #print ((queue13).qsize())
        if q231b.empty():
                    break
        t13 += (time.time())-t1i
      #time.sleep(PL3)
        
   
    
    while (((q21bb.qsize())>0)):
     #for l in range(0,wt3):
        c=q21bb.get()
        link104.write(c)
        #print ((queue21).qsize())
        if q12bb.empty():
                    break
        t21 +=  (time.time())-t2i
     #time.sleep(PL4)

    while (((q32b.qsize())>0)):
     #for m in range(0,wt4):
        d=q32b.get()
        link106.write(d)
        #print ((queue22).qsize())
        if q32b.empty():
                    break
        t22 += (time.time())-t2i
     #time.sleep(PL5)
   
    while (((q22b.qsize())>0)):
      #for q in range(0,wt8):
        h=q22b.get()
        link105.write(h)
        #print ((queue23).qsize())
        if q22b.empty():
                    break
        t23 +=  (time.time())-t2i
      #time.sleep(PL6)
        
        
    
    while (((queue121.qsize())>0)):
     #for n in range(0,wt5):
        e=queue121.get()
        link102.write(e)
        #print ((queue31).qsize())
        if queue121.empty():
                    break
        t31 += (time.time())-t3i
     #time.sleep(PL7)
        
    
    while (((q12bb.qsize())>0)):
     #for o in range(0,wt6):
        f=q12bb.get()
        link107.write(f)
        #print ((queue32).qsize())
        if q12bb.empty():
                        break
        t32 +=  (time.time())-t3i
     #time.sleep(PL8)

        
    while (((queue11.qsize())>0)):
     #for r in range(0,wt9):    
    
        v=queue11.get()
        link1.write(v)
        #print ((queue33).qsize())
        if queue11.empty():
                        break
        t33 +=time.time()-t3i
        
     #time.sleep(PL9)
    while (((queue31.qsize())>0)):
     #for r in range(0,wt9):    
    
        w=queue31.get()
        link105.write(w)
        #print ((queue33).qsize())
        if queue31.empty():
                        break
        t331 +=time.time()-t3i
        
    while (((q11b.qsize())>0)):
     #for r in range(0,wt9):    
    
        x=q11b.get()
        link1021.write(x)
        #print ((queue33).qsize())
        if q11b.empty():
                        break
        t3311 +=time.time()-t3i

    
    '''The above time will give time for which the packet stays in Output queue'''
    
    link1.close()
    link2.close()
    link3.close()
    link102.close()
    link107.close()
    link104.close()
    link105.close()
    link106.close()
    

    print ("Packets sent to the destinations based on highest class of service!!!!")
    print ("--------------------------------------------------------------------")
    print ("Mean Time in Residence for each destination based on the highest class of service being served first :")

    if(q33 !=0):
        print (str((t11)/q33))
    else:
        print (str(t11)/q231b)
    
    
    
    if(q231b != 0):
        print (str((t13)/(q231)))
    else:
        print ('0')

        
    if(q21bb!=0):
        print (str((t21)/(q21)))
    else:
        print ('0')

        
    if(q32b != 0):
        print (str((t22)/(q32)))
    else:
        print ('0')
        
    if(q22b != 0):
        print (str((t22)/(q22)))
    else:
        print ('0')
        
    if(q13 != 0):
        print (str((t31)/(q13)))
    else:
        print ('0')
   
    if(q32 != 0):
        print (str(((t32)/(q12))))
    else:
        print ('0')
        
    if(q33 != 0):
        print (str(((t33)/(q11))))
    else:
        print ('0')
        
    if(q33 != 0):
        print (str(((t33)/(q11))))
    else:
        print ('0')
        

    '''
        
    print('Time=>' + 'Q11 : ' + str(t11)/q11 + ' Q12 : ' + str(t12) + 'Q13:' + str(t13) + ' Q21 : ' + str(t21) + ' Q22 : ' + str(t22) + ' Q23 : ' + str(t23) + ' Q31 : ' + str(
        t31) + ' Q32 : ' + str(t32) + ' Q33 : ' + str(t33))

    '''

    

    
