import tkinter as tk
from tkinter import ttk
from tkinter import font,messagebox,colorchooser,filedialog
import os

main_app = tk.Tk()
main_app.geometry("1200x800")  #gives the window size which will apear
main_app.title("KushPAD")

#-----------------------------------------------------main menu-------------------------------------------------------------------------------
main_menu = tk.Menu(main_app)


#include file icons
new_icon = tk.PhotoImage(file= "icons2/new.png")
open_icon = tk.PhotoImage(file= "icons2/open.png")
save_icon = tk.PhotoImage(file= "icons2/save.png")
save_as_icon = tk.PhotoImage(file= "icons2/save_as.png")
exit_icon = tk.PhotoImage(file= "icons2/exit.png")

file_menu = tk.Menu(main_menu,tearoff= False)


#include edit icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu,tearoff= False)

######## view icons 
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu,tearoff= False)


######## color theme 
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png') 
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2')
}

color = tk.Menu(main_menu,tearoff= False)

 


#cascading these menus inside main menu
main_menu.add_cascade(label="File",menu= file_menu ) 
main_menu.add_cascade(label="Edit",menu= edit )
main_menu.add_cascade(label="View",menu= view )
main_menu.add_cascade(label="Color-Theme",menu= color )



#remember to place the menu bar by writing this
main_app.config(menu = main_menu)

#-----------------------------------------------------end main menu--------------------------------------------------------------------------


#-----------------------------------------------------toolbar-------------------------------------------------------------------------------
toolbar = ttk.Label(main_app)
toolbar.pack(side= tk.TOP, fill= tk.X)


#font-box
font_tuple = tk.font.families()
font_family = tk.StringVar()  #font variable
font_box = ttk.Combobox(toolbar, width= 30,textvariable= font_family,state= "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0,padx=5)

## size box 
size_var = tk.IntVar()  #size variable
font_size = ttk.Combobox(toolbar, width=14, textvariable = size_var, state='readonly')
font_size['values'] = tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

## bold button 
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(toolbar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

## italic button 
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(toolbar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

## underline button 
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(toolbar, image = underline_icon)
underline_btn.grid(row = 0, column=4, padx=5)

## font color button 
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(toolbar, image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

## align left 
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(toolbar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

## align center 
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(toolbar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, padx=5)

## align right 
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(toolbar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, padx=5)

#-----------------------------------------------------end toolbar--------------------------------------------------------------------------


#-----------------------------------------------------editor-------------------------------------------------------------------------------4
texteditor = tk.Text(main_app)
texteditor.config(wrap= "word", relief= tk.FLAT)
texteditor.focus_set()
scrollbar = tk.Scrollbar(main_app)
scrollbar.pack(side= tk.RIGHT, fill= tk.Y)
texteditor.pack(expand= True,fill= tk.BOTH)
scrollbar.config(command= texteditor.yview)  #for scrollbar to move when dow key reaches at last
texteditor.config(yscrollcommand= scrollbar.set)  #to tell editor that scrollbar shld be vertical not horizontal


#font family and size functionality
current_font_family = 'Arial'
current_font_size = 12

def change_font(main_app):
    global current_font_family
    current_font_family = font_family.get()
    texteditor.configure(font=(current_font_family, current_font_size))

def change_fontsize(main_app):
    global current_font_size
    current_font_size = size_var.get()
    texteditor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

#buttons functionality

# bold button functionality
def change_bold():
    text_property = tk.font.Font(font=texteditor['font'])
    if text_property.actual()['weight'] == 'normal':
        texteditor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        texteditor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

# italic functionlaity
def change_italic():
    text_property = tk.font.Font(font=texteditor['font'])
    if text_property.actual()['slant'] == 'roman':
        texteditor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        texteditor.configure(font=(current_font_family, current_font_size, 'normal'))
    
italic_btn.configure(command=change_italic)

# underline functionality 
def change_underline():
    text_property = tk.font.Font(font=texteditor['font'])
    if text_property.actual()['underline'] == 0:
        texteditor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        texteditor.configure(font=(current_font_family, current_font_size, 'normal'))
    
underline_btn.configure(command=change_underline)

## font color functionality 
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    texteditor.configure(foreground=color_var[1])


font_color_btn.configure(command=change_font_color)

### align functionality 

def align_left():
    text_content = texteditor.get(1.0, 'end')
    texteditor.tag_config('left', justify=tk.LEFT)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, text_content, 'left')

align_left_btn.configure(command=align_left)

## center 
def align_center():
    text_content = texteditor.get(1.0, 'end')
    texteditor.tag_config('center', justify=tk.CENTER)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, text_content, 'center')

align_center_btn.configure(command=align_center)

## right 
def align_right():
    text_content = texteditor.get(1.0, 'end')
    texteditor.tag_config('right', justify=tk.RIGHT)
    texteditor.delete(1.0, tk.END)
    texteditor.insert(tk.INSERT, text_content, 'right')

align_right_btn.configure(command=align_right)


texteditor.configure(font= ('Arial',12))


#-----------------------------------------------------end editor--------------------------------------------------------------------------


#-----------------------------------------------------status bar-------------------------------------------------------------------------------
statusbar = ttk.Label(main_app,text= "Status Bar")
statusbar.pack(side= tk.BOTTOM)

text_changed = False 
def changed(main_app):
    global text_changed
    if texteditor.edit_modified():
        text_changed = True 
        words = len(texteditor.get(1.0, 'end-1c').split())  #1c helps to ignore the last character 
        characters = len(texteditor.get(1.0, 'end-1c').replace(" ",""))
        statusbar.config(text=f'Characters : {characters} Words : {words}')
    texteditor.edit_modified(False)

texteditor.bind('<<Modified>>', changed)


#-----------------------------------------------------end status bar--------------------------------------------------------------------------


#-----------------------------------------------------main menu functionality-------------------------------------------------------------------------------

#new 
url = ""
def new_file(event=None):
    global url
    url= ""
    texteditor.delete(1.0, tk.END)

#file cmds
file_menu.add_command(label= "New", image= new_icon, compound= tk.LEFT, accelerator= "Ctrl+N",command= new_file)  #if u want to use icons use this line always


#open
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            texteditor.delete(1.0, tk.END)
            texteditor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    main_app.title(os.path.basename(url))

file_menu.add_command(label= "Open", image= open_icon, compound= tk.LEFT, accelerator= "Ctrl+O",command= open_file)  #if u want to use icons use this line always

#save
def save_file(event=None):  #this argument is imp for shortcut keys which we will define afterwards
    global url 
    try:
        if url:
            content = str(texteditor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = texteditor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 
    
file_menu.add_command(label= "Save", image= save_icon, compound= tk.LEFT, accelerator= "Ctrl+S",command= save_file)  #if u want to use icons use this line always


## save as functionality 
def save_as(event=None):
    global url 
    try:
        content = texteditor.get(1.0, tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

file_menu.add_command(label= "Save As", image= save_as_icon, compound= tk.LEFT, accelerator= "Ctrl+Alt+S",command= save_as)  #if u want to use icons use this line always


#exit
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = texteditor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content2 = str(texteditor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return 

file_menu.add_command(label= "Exit", image= exit_icon, compound= tk.LEFT, accelerator= "Ctrl+Q",command= exit_func)  #if u want to use icons use this line always

#-------------------------------------------------------------------------------------------------------------file opt end-----------------------------


#edit cmds
edit.add_command(label= "Copy", image= copy_icon, compound= tk.LEFT, accelerator= "Ctrl+C", command=lambda:texteditor.event_generate("<Control c>"))  #if u want to use icons use this line always
edit.add_command(label= "Paste", image= paste_icon, compound= tk.LEFT, accelerator= "Ctrl+V",command=lambda:texteditor.event_generate("<Control v>"))  #if u want to use icons use this line always
edit.add_command(label= "Cut", image= cut_icon, compound= tk.LEFT, accelerator= "Ctrl+X",command=lambda:texteditor.event_generate("<Control x>"))  #if u want to use icons use this line always
edit.add_command(label= "Clear All", image= clear_all_icon, compound= tk.LEFT, accelerator= "Ctrl+Alt+X",command=lambda:texteditor.delete(1.0, tk.END))  #if u want to use icons use this line always


#find 
def find_word(event=None):

    def find():
        word = find_input.get()
        texteditor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = texteditor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                texteditor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                texteditor.tag_config('match', foreground='red', background='lightblue')


    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = texteditor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        texteditor.delete(1.0, tk.END)
        texteditor.insert(1.0, new_content)


    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    #Find label frame
    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    
    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    
    ## griding widgets 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

edit.add_command(label= "Find", image= find_icon, compound= tk.LEFT, accelerator= "Ctrl+F", command= find_word)  #if u want to use icons use this line always


#view cmds
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False 
    else :
        texteditor.pack_forget()
        statusbar.pack_forget()
        toolbar.pack(side=tk.TOP, fill=tk.X)
        texteditor.pack(fill=tk.BOTH, expand=True)
        statusbar.pack(side=tk.BOTTOM)
        show_toolbar = True 

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        statusbar.pack_forget()
        show_statusbar = False 
    else :
        statusbar.pack(side=tk.BOTTOM)
        show_statusbar = True 


view.add_checkbutton(label= "Tool Bar",onvalue=True, offvalue=0,variable = show_toolbar, image=tool_bar_icon, compound=tk.LEFT, command=hide_toolbar) #if u want to use icons use this line always
view.add_checkbutton(label= "Status Bar", onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)
 #since they have checkbuttons at side


#color cmds

## color theme 
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    texteditor.config(background=bg_color, fg=fg_color)


count=0
for i in color_dict:
    color.add_radiobutton(label= i, image= color_icons[count],variable= theme_choice,compound= tk.LEFT,command= change_theme)
    count+=1

#-----------------------------------------------------end main menu functionality--------------------------------------------------------------------------
#### bind shortcut keys 
main_app.bind("<Control-n>", new_file)
main_app.bind("<Control-o>", open_file)
main_app.bind("<Control-s>", save_file)
main_app.bind("<Control-Alt-s>", save_as)
main_app.bind("<Control-q>", exit_func)
main_app.bind("<Control-f>", find_word)


main_app.mainloop()