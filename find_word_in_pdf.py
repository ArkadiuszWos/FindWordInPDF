# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 11:58:52 2017

@author: AW036048

Description:
Script to find string in .pdf files, before using be awere what folder you select if you don't want wait all day ;)

eg. of result window:

"""

import tkinter as tk
import tkinter.filedialog
import tkinter.simpledialog
import tkinter.scrolledtext as tkst
import PyPDF2
import os

root = tkinter.Tk()
root.withdraw() 


   

#selected folder by User
folder = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select folder with PDFs')
if not folder:
    tkinter.messagebox.showinfo("info", "Folder not selected!")
    folder = tkinter.filedialog.askdirectory(parent=root,initialdir="/",title='Please select folder with PDFs')

#searching string typed by User    
search_string = tkinter.simpledialog.askstring("Text prompt", "Enter search text")
if not search_string:
    tkinter.messagebox.showinfo("info", "Text not typed!")
    search_string = tkinter.simpledialog.askstring("Text prompt", "Enter search text")
    

#set vars
search_string = search_string.lower() 
counter_pdf_files = 0
how_many = 0 #how many times string accured in .pdf file 
result_list = []
search_to_print = search_string


#loop for interate in all .pfd in folders
for root, dirs, files in os.walk(folder):
    for file in files:
        
        if file.endswith(".pdf"):
            counter_pdf_files += 1
            
            #get count of page
            full_path = os.path.join(root, file)
            pdf_file = PyPDF2.PdfFileReader(full_path)
            pages = pdf_file.getNumPages()
  
            #loop for all page in .pdf
            for n in range(0, pages):
                page = pdf_file.getPage(n)
                text = page.extractText()
                text = text.lower()
                
                #append to results which page and file search test is
                if search_string in text:
                    page_no = str(n + 1)
                    count = text.count(search_string)
                    
					#for each row in report "PAGE No.: 2 Count: 10"
                    results = file + " PAGE No.:" + page_no  + " Count:" + str(count)
                    result_list.append(results)
                    
#if none .pdf            
if counter_pdf_files == 0:
    tkinter.messagebox.showinfo("info", "PDF not found!")

#print report
if result_list:
    #tkinter.messagebox.showinfo("info", result_list)
    win = tk.Tk()
    win.title("Your results")
    frame1 = tk.Frame(master = win, bg = '#9ACD32')
    frame1.pack(fill='both', expand='yes')
    editArea = tkst.ScrolledText(master = frame1, wrap = tk.WORD, width = 90, height = 50)
    editArea.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
	
	#print report
    editArea.insert(tk.INSERT, "RESULTS for "+ '"' + search_to_print +'":' + "\n" +"\n".join(result_list))
    win.mainloop()

#when text not found	
else:
    tkinter.messagebox.showinfo("info", "Text not found!")
    