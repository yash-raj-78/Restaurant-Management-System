from tkinter import *
from tkinter import ttk   
from tkinter import messagebox

class login_window:
    def __init__ (self,root):
      self.root=root
      self.root.title("login")
      self.root.geometry("1550x800+0+0")
       
    
      frame=Frame(self.root,bg="black")
      frame.place(x=500,y=250,width=450,height=300)
      
      get_str=Label(frame,text="Restaurant Login Page",font=("times new roman",20,"bold"),fg="red",bg="black")
      get_str.place(x=90,y=10)
      
      #label
      
      Username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
      Username.place(x=10,y=70)
      
      self.txtadmin=ttk.Entry(frame,font=("times new roman",15,"bold"))
      self.txtadmin.place(x=60,y=100,width=270)
      
      Password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
      Password.place(x=10,y=170)
      
      self.txtpass=ttk.Entry(frame,show="*",font=("times new roman",15,"bold"))
      self.txtpass.place(x=60,y=200,width=270)
      
      
      loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
      loginbtn.place(x=300,y=250,width=120,height=35)
      
    
      
      
      
    def login(self):
        if self.txtadmin.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtadmin.get()=="yash" and self.txtpass.get()=="raj":
            messagebox.showinfo("Success","click ok to enter the resturant ")
            root.destroy()
            import proj1
        else:
          messagebox.showerror("Invalid","Invalid username&password")    
          
          
          
    
if __name__=="__main__" :
    root=Tk()
    app=login_window(root)
    root.mainloop()
       
    

