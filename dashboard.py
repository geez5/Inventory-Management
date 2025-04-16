# creating the dashboard
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry




#functionality

def employee_form(window):
    global back_image
    employee_frame = Frame(window, width=1070, height=567,bg='white')
    employee_frame.place(x=200, y=100)
    heading_label = Label(employee_frame, text='Manage Employee Details', font=('times new roman', 16,'bold'),bg='#0f4d7d', fg='white')
    heading_label.place(x=0, y=0, relwidth=1)
    back_image=PhotoImage(file='back_button.png')
    back_button = Button(employee_frame, image=back_image, bd=0, cursor='hand2',bg='white', command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)

    top_frame=Frame(employee_frame, bg='white')
    top_frame.place(x=0,y=60,relwidth=1,height=235)
    search_frame=Frame(top_frame,bg='white')
    search_frame.pack()
    search_combobox=ttk.Combobox(search_frame,values=('Id','Name','Email'),font=('times new roman',12,'bold'),state='readonly')
    search_combobox.set('Search By')
    search_combobox.grid(row=0,column=0,padx=10,pady=10)
    search_entry=Entry(search_frame,font=('times new roman',12,'bold'),bg='lightyellow')
    search_entry.grid(row=0,column=1,padx=10,pady=10)
    search_button=Button(search_frame,text='Search',font=('times new roman',12,'bold'),width=10,bg='#0f4d7d',fg='white',cursor='hand2')
    search_button.grid(row=0,column=2,padx=10,pady=10)
    show_button=Button(search_frame,text='Show All',font=('times new roman',12,'bold'),width=10,bg='#0f4d7d',fg='white',cursor='hand2')
    show_button.grid(row=0,column=3,padx=10,pady=10)

    horizontal_scrollbar=Scrollbar(top_frame,orient='horizontal')
    vertical_scrollbar=Scrollbar(top_frame,orient='vertical')


    employee_treeview=ttk.Treeview(top_frame,columns=('empid','name','email','gender','dob','contact','employment_type','education','work_shift','address','doj','salary','usertype'), show='headings', yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side=BOTTOM,fill=X)
    vertical_scrollbar.config(command=employee_treeview.yview)
    vertical_scrollbar.pack(side=RIGHT,fill=Y)
    horizontal_scrollbar.config(command=employee_treeview.xview)
    employee_treeview.pack(pady=10)

    employee_treeview.heading('empid',text='Employee Id')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date of Birth')
    employee_treeview.heading('contact',text='Contact')
    employee_treeview.heading('employment_type',text='Employment Type')
    employee_treeview.heading('education',text='Education')
    employee_treeview.heading('work_shift',text='Work Shift')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('doj',text='Date of Joining')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='User Type')

    employee_treeview.column('empid',width=60)
    employee_treeview.column('name',width=140)
    employee_treeview.column('email',width=180)
    employee_treeview.column('gender',width=80)
    employee_treeview.column('dob',width=100)
    employee_treeview.column('contact',width=100)
    employee_treeview.column('employment_type',width=120)
    employee_treeview.column('education',width=120)
    employee_treeview.column('work_shift',width=100)
    employee_treeview.column('address',width=200)
    employee_treeview.column('doj',width=100)
    employee_treeview.column('salary',width=140)
    employee_treeview.column('usertype',width=120)

    detail_frame=Frame(employee_frame,bg='white')
    detail_frame.place(x=0,y=300)

    empid_label=Label(detail_frame,text='EmpId',font=('times new roman',12))
    empid_label.grid(row=0,column=0,padx=20,pady=10,sticky='w')
    empid_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,padx=20,pady=10)

    name_label=Label(detail_frame,text='Name',font=('times new roman',12))
    name_label.grid(row=0,column=2,padx=20,pady=10,sticky='w')
    name_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    name_entry.grid(row=0,column=3,padx=20,pady=10)

    email_label=Label(detail_frame,text='Email',font=('times new roman',12))
    email_label.grid(row=0,column=4,padx=20,pady=10,sticky='w')
    email_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    email_entry.grid(row=0,column=5,padx=20,pady=10)

    gender_label=Label(detail_frame,text='Gender',font=('times new roman',12))
    gender_label.grid(row=1,column=0,padx=20,pady=10,sticky='w')
    gender_combobox=ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1,column=1,padx=20,pady=10,sticky='w')

    dob_label=Label(detail_frame,text='Date of Birth',font=('times new roman',12))
    dob_label.grid(row=1,column=2,padx=20,pady=10,sticky='w')
    dob_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly',data_pattern='dd/mm/yyyy')
    dob_date_entry.grid(row=1,column=3,padx=20,pady=10)

    contact_label=Label(detail_frame,text='Contact',font=('times new roman',12))
    contact_label.grid(row=1,column=4,padx=20,pady=10,sticky='w')
    contact_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    contact_entry.grid(row=1,column=5,padx=20,pady=10)

    employment_type_label=Label(detail_frame,text='Employment Type',font=('times new roman',12))
    employment_type_label.grid(row=2,column=0,padx=20,pady=10,sticky='w')
    employment_type_combobox=ttk.Combobox(detail_frame,values=('Full Time','Part Time','Contractor','casual'),font=('times new roman',12),state='readonly')
    employment_type_combobox.set('Select Employment Type')
    employment_type_combobox.grid(row=2,column=1,padx=20,pady=10)

    education_label=Label(detail_frame,text='Education',font=('times new roman',12))
    education_label.grid(row=2,column=2,padx=20,pady=10,sticky='w')
    education_combobox=ttk.Combobox(detail_frame,values=('Bachelor','Master','PhD','Post Graduate'),font=('times new roman',12),state='readonly')
    education_combobox.set('Select Education')
    education_combobox.grid(row=2,column=3,padx=20,pady=10)
    work_shift_label=Label(detail_frame,text='Work Shift',font=('times new roman',12))
    work_shift_label.grid(row=2,column=4,padx=20,pady=10,sticky='w')
    work_shift_combobox=ttk.Combobox(detail_frame,values=('Morning','Afternoon','Evening'),font=('times new roman',12),state='readonly')
    work_shift_combobox.set('Select Work Shift')
    work_shift_combobox.grid(row=2,column=5,padx=20,pady=10)

    address_label=Label(detail_frame,text='Address',font=('times new roman',12))
    address_label.grid(row=3,column=0,padx=20,pady=10,sticky='w')
    address_text=Text(detail_frame,width=20,height=3,font=('times new roman',12),bg='lightyellow')
    address_text.grid(row=3,column=1,padx=20,pady=10,sticky='w')

    doj_label=Label(detail_frame,text='Date of Joining',font=('times new roman',12))
    doj_label.grid(row=3,column=2,padx=20,pady=10,sticky='w')
    doj_date_entry=DateEntry(detail_frame,width=18,font=('times new roman',12),state='readonly', date_pattern='dd/mm/yyyy')
    doj_date_entry.grid(row=3,column=3,padx=20,pady=10)

    salary_label=Label(detail_frame,text='Salary',font=('times new roman',12))
    salary_label.grid(row=11,column=0,padx=20,pady=10,sticky='w')
    salary_entry=Entry(detail_frame,font=('times new roman',12))
    salary_entry.grid(row=11,column=1,padx=20,pady=10)

    usertype_label=Label(detail_frame,text='User Type',font=('times new roman',12))
    usertype_label.grid(row=12,column=0,padx=20,pady=10,sticky='w')
    usertype_combobox=ttk.Combobox(detail_frame,values=('Admin','Employee','Supplier'),font=('times new roman',12),state='readonly')
    usertype_combobox.set('Select User Type')
    usertype_combobox.grid(row=12,column=1,padx=20,pady=10)

    password_label=Label(detail_frame,text='Password',font=('times new roman',12))
    password_label.grid(row=3,column=4,padx=20,pady=10,sticky='w')
    password_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow',show='*')
    password_entry.grid(row=3,column=5,padx=20,pady=10)

    button_frame=Frame(employee_frame)
    button_frame.place(x=200,y=530)




window = Tk()



window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0, 0)
window.iconbitmap('logo.png')
window.config(bg='white')
bg_Image = PhotoImage(file='inventory (1).png')
titleLabel = Label(window, image=bg_Image, compound="left", text='Inventory Management System',
                   font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

logoutButton=Button(window, text='Logout', font=('times new roman', 20, 'bold'), fg='#010c48')
logoutButton.place(x=1100, y=10)

subtitleLabel=Label(window, text='Welcome Admin\t\t  Date:18/04/2025\t\t  Time:9:45:33 am', font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0,y=70,relwidth=1)
# building a sidebar
leftFrame=Frame(window)
leftFrame.place(x=0, y=102,width=200,height=555)

logoImage=PhotoImage(file='logo.png')
ImageLabel=Label(leftFrame, image=logoImage)
ImageLabel.pack()

menuLabel=Label(leftFrame, text='Menu', font=('times new roman', 20), bg='#009688')
menuLabel.pack(fill=X)

employee_icon=PhotoImage(file='employee.png')
employee_button=Button(leftFrame, image=employee_icon,compound=LEFT, text='Employees', font=('times new roman',20, 'bold'),anchor='w',padx=10, command=lambda: employee_form(window))
employee_button.pack(fill=X)

supplier_icon=PhotoImage(file='supplier.png')
supplier_button=Button(leftFrame, image=supplier_icon,compound=LEFT, text='Suppliers', font=('times new roman',20, 'bold'),anchor='w',padx=10)
supplier_button.pack(fill=X)

category_icon=PhotoImage(file='category.png')
category_button=Button(leftFrame, image=category_icon,compound=LEFT, text='Category', font=('times new roman',20, 'bold'),anchor='w',padx=10)
category_button.pack(fill=X)

product_icon=PhotoImage(file='product.png')
product_button=Button(leftFrame, image=product_icon,compound=LEFT, text='Products', font=('times new roman',20, 'bold'),anchor='w',padx=10)
product_button.pack(fill=X)

sales_icon=PhotoImage(file='sales.png')
sales_button=Button(leftFrame, image=sales_icon,compound=LEFT, text='Sales', font=('times new roman',20, 'bold'),anchor='w',padx=10)
sales_button.pack(fill=X)

exit_icon=PhotoImage(file='exit.png')
exit_button=Button(leftFrame, image=exit_icon,compound=LEFT, text='Exit', font=('times new roman',20, 'bold'),anchor='w',padx=10)
exit_button.pack(fill=X)

#creating frame cards

emp_frame=Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280)
total_emp_icon=PhotoImage(file='total_emp.png')
total_emp_icon_label=Label(emp_frame,image=total_emp_icon,bg='#2C3E50')
total_emp_icon_label.pack()

total_emp_label=Label(emp_frame,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()

total_emp_count_label=Label(emp_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
total_emp_count_label.pack()

sup_frame=Frame(window,bg='#8E44AD',bd=3,relief=RIDGE)
sup_frame.place(x=800,y=125,height=170,width=280)
total_sup_icon=PhotoImage(file='total_sup.png')
total_sup_icon_label=Label(sup_frame,image=total_sup_icon,bg='#8E44AD')
total_sup_icon_label.pack()

total_sup_label=Label(sup_frame,text='Total Suppliers',bg='#8E44AD',fg='white',font=('times new roman',15,'bold'))
total_sup_label.pack()

total_sup_count_label=Label(sup_frame,text='0',bg='#8E44AD',fg='white',font=('times new roman',30,'bold'))
total_sup_count_label.pack()

cat_frame=Frame(window,bg='green',bd=3,relief=RIDGE)
cat_frame.place(x=400,y=310,height=170,width=280)
total_cat_icon=PhotoImage(file='total_cat.png')
total_cat_icon_label=Label(cat_frame,image=total_cat_icon,bg='green')
total_cat_icon_label.pack()

total_emp_label=Label(cat_frame,text='Categories',bg='green',fg='white',font=('times new roman',15,'bold'))
total_emp_label.pack()

total_cat_count_label=Label(cat_frame,text='0',bg='green',fg='white',font=('times new roman',30,'bold'))
total_cat_count_label.pack()

prod_frame=Frame(window,bg='#C11C84',bd=3,relief=RIDGE)
prod_frame.place(x=800,y=310,height=170,width=280)
total_prod_icon=PhotoImage(file='total_prod.png')
total_prod_icon_label=Label(prod_frame,image=total_prod_icon,bg='#C11C84')
total_prod_icon_label.pack()

total_prod_label=Label(prod_frame,text='Total Products',bg='#C11C84',fg='white',font=('times new roman',15,'bold'))
total_prod_label.pack()

total_prod_count_label=Label(prod_frame,text='0',bg='#C11C84',fg='white',font=('times new roman',30,'bold'))
total_prod_count_label.pack()

sales_frame=Frame(window,bg='orange',bd=3,relief=RIDGE)
sales_frame.place(x=600,y=495,height=170,width=280)
total_sales_icon=PhotoImage(file='total_sales.png')
total_sales_icon_label=Label(sales_frame,image=total_sales_icon,bg='orange')
total_sales_icon_label.pack()

total_sales_label=Label(sales_frame,text='Total Sales',bg='orange',fg='white',font=('times new roman',15,'bold'))
total_sales_label.pack()

total_sales_count_label=Label(sales_frame,text='0',bg='orange',fg='white',font=('times new roman',30,'bold'))
total_sales_count_label.pack()

window.mainloop()
