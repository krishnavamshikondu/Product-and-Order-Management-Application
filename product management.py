from tkinter import *
import mysql.connector
from tkinter import messagebox

root=Tk()

root.title('product management')
root.geometry('900x600')

current=[]
def clear():
    global current
    for label in current:
        label.destroy()
    current=[]
    
curr=[]
def frame(a,b,c,d,e):
    global current
    clear()
    
    globals()['f']=LabelFrame(root,text='data',pady=10,padx=10,bg='white',width=850,height=400 )
    f.grid(row=1,columnspan=8,sticky="nw")
    f.grid_propagate(False)

    button5=Button(root,text=a,fg='red',padx=20,pady=20,command=lambda:add(a))
    button6=Button(root,text=b,fg='red',padx=20,pady=20,command=lambda:remove(b))
    button7=Button(root,text=c,fg='red',padx=20,pady=20,command=lambda:update(c))
    button8=Button(root,text=d,fg='red',padx=20,pady=20,command=lambda:refresh(d))

    button5.grid(row=200,column=4)
    button6.grid(row=200,column=5)
    button7.grid(row=200,column=6)
    button8.grid(row=200,column=7)

    current.append(button5)
    current.append(button6)
    current.append(button7)
    current.append(button8)

    if e=='menu':

        def z(a):
            x=Entry(f)
            x.insert(0,'customer_name')
            x.grid(row=1,column=0)
            current.append(x)

            x1=Entry(f)
            x1.insert(0,'quantity')
            x1.grid(row=1,column=1)
            current.append(x1)

            x2=Entry(f)
            x2.insert(0,'price')
            x2.grid(row=1,column=2)
            current.append(x2)

            x3=Entry(f)
            x3.insert(0,'customer_email')
            x3.grid(row=1,column=3)
            current.append(x3)
            
            m1=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n1=m1.cursor()
            n1.execute(f"select c_name,quantity,price,email from customer where p_name='{a}'")
            l1=[i for i in n1]
             
            if l1:
                for i in range(len(l1)):
                    for j in range(len(l1[0])):
                        x=Entry(f)
                        x.insert(0,l1[i][j])
                        x.grid(row=i+2,column=j)
                        current.append(x)
                        curr.append(x)
                
            else:
                for j in range(4):      
                    x=Entry(f)
                    x.insert(0,0)
                    x.grid(row=2,column=j)
                    current.append(x)
                    curr.append(x)
            
            def clean():
                global curr
                for i in curr:
                    i.destroy()
            clear=Button(f,text='clear data',command=clean)
            clear.grid(row=0,column=2)
            current.append(clear)
            
        m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
        n=m.cursor()
        n.execute(f'select distinct(name) from products')
        l1=[i[0] for i in n]
        print(l1)
        
        clicked=StringVar()
        clicked.set('select the product')
        option=[l2 for l2 in l1 ]
        x=OptionMenu(f,clicked,*option,command=z)
        x.grid(row=0,column=0)
        current.append(x)

        
    else:
        l1=[]
        
        #frame('add product','remove product','update product','refresh')
        m0=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
        n0=m0.cursor()
        n0.execute(f'desc {e}')
        l2=[i0 for i0 in n0]
        for i1 in range(len(l2)):
            x1=Entry(f)
            x1.insert(0,l2[i1][0])
            x1.grid(row=0,column=i1,sticky="nw")
            current.append(x1)
            
        
        m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
        n=m.cursor()
        n.execute(f'select * from {e}')
        for i in n:
            l1.append(i)
       # print(len(l1))
        #print(len(i))
        for j in range(len(l1)):
            for k in range(len(i)):
                x=Entry(f)
                x.insert(0,l1[j][k])
                x.grid(row=j+1,column=k,sticky="nw")
                current.append(x1)

def x():
    frame('add product','remove product','update product','refresh p','products')
 
def xx():
    frame(' add order ',' remove order ',' update order ','refresh o','customer')
 
def xxxx():
    frame('add supplier','remove supplier','update supplier','refresh s','supplier')

def xxx():
    frame('        -         ','         -         ','         -         ','          -      ','menu')

def refresh(d):
    if d=='refresh p':
        x()
    elif d=='refresh o':
        xx()
    elif d=='refresh s':
        xxxx()
    else:
        pass
        
def add(a):
    if a=='add product':
        
        win=Tk()
        win.geometry('300x200')
        x1=Label(win,text='product_name',font=14)
        x1.grid(row=2,column=0)
        x2=Label(win,text='price',font=14)
        x2.grid(row=3,column=0)
        x3=Label(win,text='quantity',font=14)
        x3.grid(row=4,column=0)
        x4=Label(win,text='supplier_id',font=14)
        x4.grid(row=5,column=0)

        y1=Entry(win,width=20)
        y1.grid(row=2,column=2)
        y2=Entry(win,width=20)
        y2.grid(row=3,column=2)
        y3=Entry(win,width=20)
        y3.grid(row=4,column=2)
        y4=Entry(win,width=20)
        y4.grid(row=5,column=2)
        
        y=0
        def ok():
            l1=[]
            l=[y,y1,y2,y3,y4]
            for x in range(5):
                if x ==0:
                    m0=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
                    n0=m0.cursor()
                    n0.execute(f'select max(sno) from products')
                    for i in n0:
                        l1.append(str(i[0]+1))
                else:   
                    l1.append(l[x].get())
            print(l1)
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            a=f'insert into products (sno,name,price,quantity,supplierid) values(%s,%s,%s,%s,%s)'
            b=[int(x) if x.isdigit() else x for x in l1]
            n.execute(a,b)
            m.commit()
            n.close()
            messagebox.showinfo('','successfully added the product')
            

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
        
    elif a==' add order ':
        win=Tk()
        win.geometry('300x200')
 
        x2=Label(win,text='quantity',font=14)
        x2.grid(row=5,column=0)
        x4=Label(win,text='product_name',font=14)
        x4.grid(row=3,column=0)
        x5=Label(win,text='customer_name',font=14)
        x5.grid(row=6,column=0)
        x6=Label(win,text='customer_email',font=14)
        x6.grid(row=7,column=0)

        y2=Entry(win,width=20)
        y2.grid(row=5,column=2)
        y4=Entry(win,width=20)
        y4.grid(row=3,column=2)
        y5=Entry(win,width=20)
        y5.grid(row=6,column=2)
        y6=Entry(win,width=20)
        y6.grid(row=7,column=2)

        y=0
        y1=0
        y3=0
        def ok():
            l1=[]
            l=[y,y1,y2,y3,y4,y5,y6]
            for x in range(7):
                if x ==0:
                    m0=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
                    n0=m0.cursor()
                    n0.execute(f'select max(sno) from customer')
                    for i in n0:
                        l1.append(str(i[0]+1))
                elif x==1:
                    m2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
                    n2=m2.cursor()
                    n2.execute(f"select price from products where name='{y4.get()}'")
                    for i in n2:
                        l1.append(str(i[0]))
                elif x==3:
                    l1.append(str(int(l1[1]) * int(y2.get())))
                else:
                    l1.append(l[x].get())
            print(l1)
            
            m1=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n1=m1.cursor()
            n1.execute(f"select quantity,name from products")
            b1=[ xx for xx in n1]
            print(b1)
            b2=[int(x) if x.isdigit() else x for x in l1]
            for i in range(len(b1)):
                if b1[i][1]==b2[4] and b2[2]< b1[i][0]:
                    m2=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
                    n2=m2.cursor()
                   # v1=[int(x) if x.isdigit() else x for x in l1]
                    print(b1[i][0]-b2[2]) 
                    print(b2[4])
                    n2.execute(f"update products set quantity= {b1[i][0]-b2[2]} where name='{b2[4]}'")
                    m2.commit()
                    n2.close()
            
                    m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
                    n=m.cursor()
                    a=f'insert into customer (sno,price,quantity,amount,p_name,c_name,email) values(%s,%s,%s,%s,%s,%s,%s)'
                    b=[int(x) if x.isdigit() else x for x in l1]
                    print(b)
                    n.execute(a,b)
                    m.commit()
                    n.close()
                    messagebox.showinfo('','successfully added the order')
                    break
            #else:
                
            
            

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
        
    elif a=='add supplier':
        win=Tk()
        win.geometry('300x200') 
        x1=Label(win,text='supplier_id',font=14)
        x1.grid(row=2,column=0)
        x2=Label(win,text='supplier_name',font=14)
        x2.grid(row=3,column=0)
        x3=Label(win,text='supplier_email',font=14)
        x3.grid(row=4,column=0)
        x4=Label(win,text='supplier_number',font=14)
        x4.grid(row=5,column=0)

        y1=Entry(win,width=20)
        y1.grid(row=2,column=2)
        y2=Entry(win,width=20)
        y2.grid(row=3,column=2)
        y3=Entry(win,width=20)
        y3.grid(row=4,column=2)
        y4=Entry(win,width=20)
        y4.grid(row=5,column=2)
        y=0

        def ok():
            l1=[]
            l=[y,y1,y2,y3,y4]
            for x in range(5):
                if x ==0:
                    m0=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
                    n0=m0.cursor()
                    n0.execute(f'select max(sno) from supplier')
                    for i in n0:
                        l1.append(str(i[0]+1))
                else:
                    l1.append(l[x].get())
            print(l1)
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            a=f'insert into supplier (sno,supplier_id,supplier_name,supplier_email,supplier_no) values(%s,%s,%s,%s,%s)'
            b=[int(x) if x.isdigit() else x for x in l1]
            n.execute(a,b)
            m.commit()
            n.close()
            messagebox.showinfo('','successfully added the supllier details')
            

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
def remove(b):
    if b=='remove product':
        win=Tk()
        win.geometry('300x200')
        x=Label(win,text='product_name',font=14)
        x.grid(row=1,column=0)

        y=Entry(win,width=20)
        y.grid(row=1,column=2)

        def ok():
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            n.execute(f"delete from products where name='{y.get()}'")
            #print('helllo')
            m.commit()
            n.close()
            messagebox.showinfo('','successfully removed the product')

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
    elif b==' remove order ':
        win=Tk()
        win.geometry('300x200')
        x=Label(win,text='customer_name',font=14)
        x.grid(row=1,column=0)

        y=Entry(win,width=20)
        y.grid(row=1,column=2)

        def ok():
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            n.execute(f"delete from customer where c_name='{y.get()}'")
            #print('helllo')
            m.commit()
            n.close()
            messagebox.showinfo('','successfully removed the order')

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)

    elif b=='remove supplier':
        win=Tk()
        win.geometry('300x200')
        x=Label(win,text='product_name',font=14)
        x.grid(row=1,column=0)

        y=Entry(win,width=20)
        y.grid(row=1,column=2)

        def ok():
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            n.execute(f"delete from supplier where supplier_name='{y.get()}'")
            #print('helllo')
            m.commit()
            n.close()
            messagebox.showinfo('','successfully removed the supllier details')

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
    else:
        pass

def update(c):
    if c=='update product':
        win=Tk()
        win.geometry('300x200')
        x=Label(win,text='sno',font=14)
        x.grid(row=1,column=0)
        x1=Label(win,text='product_name',font=14)
        x1.grid(row=2,column=0)
        x2=Label(win,text='price',font=14)
        x2.grid(row=3,column=0)
        x3=Label(win,text='quantity',font=14)
        x3.grid(row=4,column=0)
        x4=Label(win,text='supplier_id',font=14)
        x4.grid(row=5,column=0)

        y=Entry(win,width=20)
        y.grid(row=1,column=2)
        y1=Entry(win,width=20)
        y1.grid(row=2,column=2)
        y2=Entry(win,width=20)
        y2.grid(row=3,column=2)
        y3=Entry(win,width=20)
        y3.grid(row=4,column=2)
        y4=Entry(win,width=20)
        y4.grid(row=5,column=2)

        def ok():
            l1=[]
            l=[y,y1,y2,y3,y4]
            for x in range(5):
                l1.append(l[x].get())
            print(l1)
            v1=[int(x) if x.isdigit() else x for x in l1]
            print(v1)
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor() 
            n.execute(f"update products set name='{v1[1]}',price={v1[2]},quantity={v1[3]},supplierid={v1[4]} where sno={v1[0]}")
            m.commit()
            n.close()
            messagebox.showinfo('','successfully updated the product')

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
    elif c==' update order ':
        win=Tk()
        win.geometry('300x200')
        x=Label(win,text='sno',font=14)
        x.grid(row=1,column=0)
        x1=Label(win,text='price',font=14)
        x1.grid(row=2,column=0)
        x2=Label(win,text='quantity',font=14)
        x2.grid(row=3,column=0)
        x4=Label(win,text='product_name',font=14)
        x4.grid(row=5,column=0)
        x5=Label(win,text='customer_name',font=14)
        x5.grid(row=6,column=0)
        x6=Label(win,text='customer_email',font=14)
        x6.grid(row=7,column=0)

        y=Entry(win,width=20)
        y.grid(row=1,column=2)
        y1=Entry(win,width=20)
        y1.grid(row=2,column=2)
        y2=Entry(win,width=20)
        y2.grid(row=3,column=2)
        y4=Entry(win,width=20)
        y4.grid(row=5,column=2)
        y5=Entry(win,width=20)
        y5.grid(row=6,column=2)
        y6=Entry(win,width=20)
        y6.grid(row=7,column=2)
        
        y3=0
        def ok():
            l1=[]
            l=[y,y1,y2,y3,y4,y5,y6]
            for x in range(7):
                if x==3:
                    l1.append(str(int(y1.get()) * int(y2.get())))
                else:
                    l1.append(l[x].get())
            print(l1)
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            v1=[int(x) if x.isdigit() else x for x in l1]
            print(v1)
            n.execute(f"update customer set p_name='{v1[4]}',price={v1[1]},quantity={v1[2]},amount={v1[3]},c_name='{v1[5]}',email='{v1[6]}' where sno={v1[0]}")
            m.commit()
            n.close()
            messagebox.showinfo('','successfully updated the order')
            

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)

    elif c=='update supplier':
        win=Tk()
        win.geometry('300x200')
        x=Label(win,text='sno',font=14)
        x.grid(row=1,column=0)
        x1=Label(win,text='supplier_id',font=14)
        x1.grid(row=2,column=0)
        x2=Label(win,text='supplier_name',font=14)
        x2.grid(row=3,column=0)
        x3=Label(win,text='supplier_email',font=14)
        x3.grid(row=4,column=0)
        x4=Label(win,text='supplier_number',font=14)
        x4.grid(row=5,column=0)

        y=Entry(win,width=20)
        y.grid(row=1,column=2)
        y1=Entry(win,width=20)
        y1.grid(row=2,column=2)
        y2=Entry(win,width=20)
        y2.grid(row=3,column=2)
        y3=Entry(win,width=20)
        y3.grid(row=4,column=2)
        y4=Entry(win,width=20)
        y4.grid(row=5,column=2)

        def ok():
            l1=[]
            l=[y,y1,y2,y3,y4]
            for x in range(5):
                l1.append(l[x].get())
            print(l1)
            m=mysql.connector.connect(host='localhost',user='root',passwd='2000',database='manage')
            n=m.cursor()
            v1=[int(x) if x.isdigit() else x for x in l1]
            print(v1)
            n.execute(f"update supplier set supplier_id='{v1[1]}',supplier_name='{v1[2]}',supplier_email='{v1[3]}',supplier_no={v1[4]} where sno={v1[0]}")
            m.commit()
            n.close()
            messagebox.showinfo('','successfully updated the supplier details')
            

        button=Button(win,text='ok',command=ok)
        button.grid(row=10,column=2)
    else:
        pass
        
button1=Button(root,text='store',fg='blue',padx=20,pady=20,command=x)
button2=Button(root,text='customer',fg='blue',padx=20,pady=20,command=xx)
button3=Button(root,text='track customer order',fg='blue',padx=10,pady=20,command=xxx)
button4=Button(root,text='supplier',fg='blue',padx=20,pady=20,command=xxxx)

button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2)
button4.grid(row=0,column=3)

root.mainloop()
