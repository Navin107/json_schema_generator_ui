from tkinter import *
import tkinter
from tkinter import font
from tkinter import ttk
from tkinter.tix import Tree
from PIL import ImageTk, Image
from tkinter import filedialog
import json
import requests
from tkinter import messagebox


class json_schema_generator_ui:

    def __init__(self,root):
        
        self.root=root
        self.root.title("JSON SCHEMA GENERATOR")
        self.root.geometry('1640x800+0+0')

        self.bg = ImageTk.PhotoImage(file="D:/json_schema_generator_ui/icons/bg_converted.png") 
        self.img_bg = ImageTk.PhotoImage(file="D:/iudx_logo.jpg")       

        self.canvas = Canvas(root, width=1550, height=800)
        self.canvas.create_image(0, 0, image = self.bg, anchor = NW)        
        self.my_rectangle = self.round_rectangle(30, 30, 1500, 770,  radius=45, fill="white")
        Label(self.canvas, text="JSON Schema Generator",fg="black", font=("Helvetica", "28", "bold"), bg="white").place(x=600,y=70)
        Label(self.canvas,  image=self.img_bg, bg="white").place(x=45,y=40)      
        self.canvas.pack()  

        self.first_frame()
        self.second_frame()
        self.third_frame()
        self.fourth_frame()
        self.table_frame()

    def first_frame(self):

        self.file_name = StringVar()
        self.url = StringVar()

        self.frame1 = LabelFrame(self.canvas, text= "Upload Options", bg="white", font=("Times","15") )
        self.frame1.place(x=40,y=290, width=600, height=360)    
    
        Label(self.frame1, text="File Upload", fg="#383838", font=("Century", "11"), bg="white").place(x=30,y=30)
        self.file_upload = Entry(self.frame1, fg="#383838", font=("Century", "11"), bg="white", textvariable=self.file_name)
        self.file_upload.place(x=30,y=60, width=500)
        
        self.button1_bg = ImageTk.PhotoImage(file="D:/json_schema_generator_ui/icons/button_upload-file-files.png")
        Button(self.frame1,  image=self.button1_bg, borderwidth=0, bg="white",  command=lambda:self.open_file(), state=DISABLED).place(x=30, y=110)  

        Label(self.frame1, text="URL Upload", fg="#383838", font=("Century", "11"), bg="white").place(x=30,y=190)
        self.url_upload = Entry(self.frame1, fg="#383838", font=("Century", "11"), bg="white", textvariable=self.url)
        self.url_upload.place(x=30,y=220, width=500)

        self.button2_bg = ImageTk.PhotoImage(file="D:/json_schema_generator_ui/icons/button_upload-url-urls.png")
        Button(self.frame1,  image=self.button2_bg, borderwidth=0, bg="white",  command=lambda:self.open_file(), state=DISABLED).place(x=30, y=260)  

    def second_frame(self):
        
        self.frame2 = LabelFrame(self.canvas, text= "JSON Schema Viewer",  bg="white", font=("Times","15") )
        self.frame2.place(x=650,y=290, width=840, height=460)  
    
    def third_frame(self):
        
        self.frame3 = LabelFrame(self.canvas, text= "Input Options",  bg="white", font=("Century","15") )
        self.frame3.place(x=40,y=150, width=1450, height=130)    
        Label(self.frame3, text="Input Format",fg="#292626", bg="white",font=("Century", "13")).place(x=10,y=30)

        self.values = ["Select", "upload a file of resource item", "upload files of resource item", "upload a URL of resource item", "upload URL of resource items"]
        self.cmb_box = ttk.Combobox(self.frame3, value=self.values, state="readonly", font=("times new roman", "10"), justify=CENTER)
        self.cmb_box .current(0)
        self.cmb_box .bind("<<ComboboxSelected>>", self.selected)
        self.cmb_box .place(x=155, y=35, width=400) 
        
        Label(self.frame3, text="1. Upload a single file of resource item for any city", fg="#383838", font=("Century", "12"), bg="white").place(x=600,y=7)
        Label(self.frame3, text="2. Upload multiple files of resource item for any city", fg="#383838", font=("Century", "12"), bg="white").place(x=600,y=52)
        Label(self.frame3, text="3. Upload a URL of resource item for any city", fg="#383838", font=("Century", "12"), bg="white").place(x=1050,y=5)
        Label(self.frame3, text="4. Upload URLs of resource item for any city", fg="#383838", font=("Century", "12"), bg="white").place(x=1050,y=52)

    def fourth_frame(self):
    
        self.frame4 = LabelFrame(self.canvas, text= "Submit Options", bg="white", font=("Times","15") )
        self.frame4.place(x=40,y=650, width=600, height=100)    

        self.submit_button_file = ImageTk.PhotoImage(file="D:/json_schema_generator_ui/icons/button_generate.png")
        Button(self.frame4, image=self.submit_button_file, borderwidth=0, bg="white", command=self.execute_file, state=DISABLED).place(x=150,y=15)

        self.download_button = ImageTk.PhotoImage(file="D:/json_schema_generator_ui/icons/button_save.png")
        Button(self.frame4, image=self.download_button, borderwidth=0, bg="white", command=self.saveFile, state=DISABLED).place(x=300,y=15)

    def table_frame(self):

        self.table_frame = Frame(self.frame2, bg="white", relief=RIDGE, bd=4)
        self.table_frame.place(x=20,y=20, width=800, height=400)  

        sb = Scrollbar(self.table_frame)
        sb.pack(side='right', fill='y')

        self.txt = Text(self.table_frame,bd=0, font=("Century",10))
        self.txt.pack()

        self.txt.config(yscrollcommand=sb.set)
        sb.config(command=self.txt.yview)

    def round_rectangle(self, x1, y1, x2, y2, radius=25, **kwargs):
            
        points = [x1+radius, y1,
                x1+radius, y1,
                x2-radius, y1,
                x2-radius, y1,  
                x2, y1,
                x2, y1+radius,
                x2, y1+radius,
                x2, y2-radius,
                x2, y2-radius,
                x2, y2,
                x2-radius, y2,
                x2-radius, y2,
                x1+radius, y2,
                x1+radius, y2,
                x1, y2,
                x1, y2-radius,
                x1, y2-radius,
                x1, y1+radius,
                x1, y1+radius,
                x1, y1]
                
        return self.canvas.create_polygon(points, **kwargs, smooth=True)

    def selected(self, event):

        self.file_name.set("")
        self.url.set("")
        self.txt.delete("1.0","end")
        self.url_list=[]
        self.new_set=[]
        self.filepath = None
            
        if self.cmb_box.get() == self.values[0]:
 
            Button(self.frame1,  image=self.button1_bg, borderwidth=0, bg="white",  command=lambda:self.open_file(), state=DISABLED).place(x=30, y=110)  
            Button(self.frame1,  image=self.button2_bg, borderwidth=0, bg="white",  command=lambda:self.url_file(), state=DISABLED).place(x=30, y=260)  
            Button(self.frame4, image=self.submit_button_file, borderwidth=0, bg="white", command=self.execute_file, state=DISABLED).place(x=150,y=15)
            Button(self.frame4, image=self.download_button, borderwidth=0, bg="white", command=self.saveFile, state=DISABLED).place(x=300,y=15)

        elif self.cmb_box.get() == self.values[1]:

            Button(self.frame1,  image=self.button1_bg, borderwidth=0, bg="white",  command=lambda:self.open_file()).place(x=30, y=110)  
            Button(self.frame1,  image=self.button2_bg, borderwidth=0, bg="white",  command=lambda:self.url_file(), state=DISABLED).place(x=30, y=260)  
            Button(self.frame4, image=self.submit_button_file, borderwidth=0, bg="white", command=self.execute_file).place(x=150,y=15)
            Button(self.frame4, image=self.download_button, borderwidth=0, bg="white", command=self.saveFile).place(x=300,y=15)

        elif self.cmb_box.get() == self.values[2]:
            
            Button(self.frame1,  image=self.button1_bg, borderwidth=0, bg="white",  command=lambda:self.open_file(multiple_file=True)).place(x=30, y=110)  
            Button(self.frame1,  image=self.button2_bg, borderwidth=0, bg="white",  command=lambda:self.url_file(), state=DISABLED).place(x=30, y=260)  
            Button(self.frame4, image=self.submit_button_file, borderwidth=0, bg="white", command=self.execute_file).place(x=150,y=15)
            Button(self.frame4, image=self.download_button, borderwidth=0, bg="white", command=self.saveFile).place(x=300,y=15)

        elif self.cmb_box.get() == self.values[3]:

            Button(self.frame1,  image=self.button1_bg, borderwidth=0, bg="white",  command=lambda:self.open_file(), state=DISABLED).place(x=30, y=110)  
            Button(self.frame1,  image=self.button2_bg, borderwidth=0, bg="white",  command=lambda:self.url_file()).place(x=30, y=260)  
            Button(self.frame4, image=self.submit_button_file, borderwidth=0, bg="white", command=self.execute_url).place(x=150,y=15)
            Button(self.frame4, image=self.download_button, borderwidth=0, bg="white", command=self.saveFile).place(x=300,y=15)

        elif self.cmb_box.get() == self.values[4]:

            Button(self.frame1,  image=self.button1_bg, borderwidth=0, bg="white",  command=lambda:self.open_file(), state=DISABLED).place(x=30, y=110)  
            Button(self.frame1,  image=self.button2_bg, borderwidth=0, bg="white",  command=lambda:self.url_file(multiple_file=True)).place(x=30, y=260)  
            Button(self.frame4, image=self.submit_button_file, borderwidth=0, bg="white", command=self.execute_url).place(x=150,y=15)
            Button(self.frame4, image=self.download_button, borderwidth=0, bg="white", command=self.saveFile).place(x=300,y=15)

    def open_file(self, multiple_file=None):
        
        if multiple_file:    
            self.filepath = filedialog.askopenfilename(multiple=True)
        
        else:
            self.filepath = filedialog.askopenfilename(multiple=False)

        self.file_name.set(self.filepath)

    def url_file(self, multiple_file=None):

        if not self.url.get():
            messagebox.showerror("Error", "Please upload url of resource item")
            return

        if multiple_file:
            self.url_list.append(self.url.get())
            self.url.set("")
            self.new_set = list(set(self.url_list))
        
        else:
            self.url_list = []
            self.url_list.append(self.url.get())
            self.url.set("")
            self.new_set = list(set(self.url_list))

    def execute_file(self):
        
        path=None
        
        if self.filepath:
            path = self.filepath
        else:
            messagebox.showerror("Error", "Please upload file of resource item")
        
        if path:
            
            if type(path) == tuple:
                
                json_array = []
                
                for file_path_name in path:
                    json_schema_value = self.path_and_file_execution(file_path_name)
                    if json_schema_value:
                        json_array.append(json_schema_value)
                
                self.txt.delete("1.0","end")
                
                if json_array:
                    self.txt.insert('end', json.dumps(json_array, indent=6))

            else:
                
                json_schema_value = self.path_and_file_execution(path)
                self.txt.delete("1.0","end")
                if json_schema_value:
                    self.txt.insert('end', json.dumps(json_schema_value, indent=6))

    def path_and_file_execution(self, path):

        json_object = None
        f = open(path)
        data = json.load(f)
        json_object = self.file_fetching(data)     
        return json_object

    def execute_url(self):

        json_array = []
        
        if not self.new_set: 
            messagebox.showerror("Error", "Please upload url of resource item")

        else:
            
            for i in self.new_set:
                try:
                    response = requests.get(i)              
                    if response:
                        data = response.json()["results"][0]
                        json_object = self.file_fetching(data)
                        if json_object:
                            json_array.append(json_object)
                
                except:
                    messagebox.showerror("Error", "Please upload proper url of resource item")

            self.txt.delete("1.0","end")
            if json_array:
                self.txt.insert('end', json.dumps(json_array, indent=6))

    def file_fetching(self, data):
        json_object = None
                    
        if data.get("dataDescriptor","") == "":
            messagebox.showerror("Error", "The file doesnt have data descriptor")

        else:
            self.data_descriptor = data["dataDescriptor"]
            json_object = self.json_schema_generator()

        return json_object 

    def saveFile(self):
        
        try:
            
            json_string = self.txt.get("1.0", END)
            json_object = json.loads(json_string)
        except:
            messagebox.showerror("Error", "Please generate schema to download")
            return

        file = filedialog.asksaveasfile(initialdir="D:/",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Json file",".json"),
                                        ("All files", ".*"),
                                    ])
        if file:
            json.dump(json_object, file, indent=6)
            self.txt.delete("1.0","end")
        
    def id_type_generator(self, type_list): 

        '''
        Reads the list containing info of type of data descriptor 

        Params
        ------
        type_list
            Read the type key and convert it to 
        
        Returns
        -------
        type
            if the type is not datDescriptor then the element  
            from the type list will be returned as type
        '''

        for i in type_list: 
            if "DataDescriptor" not in i.split(":")[1]:
                return i.split(":")[1]
        return None

    def property_type(self, key):

        '''
        Reads the key containing info of property type 

        Params
        ------
        key
            Read the key and fetch the property type
        
        Returns
        -------
        property_type
            property type containing information of type of 
            the property
        '''

        property_type = self.data_descriptor[key]["dataSchema"].split(":")[1]
        return property_type

    def basic_schema_generator(self):
        
        '''
        Creating the basic schema 

        Returns
        -------
        schema
            basic schema containing all the 
            basic properties
        '''

        schema = {}
        schema["$id"]= "https://voc.iudx.org.in/"    
        schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"    
        schema["type"] = "object"
        schema["properties"] = {}
        schema["properties"]["id"] = {}
        schema["properties"]["id"]["type"] = "string"
        schema["required"] = []
        schema["required"].append("id")
        schema["additionalProperties"] = False
        
        type = self.data_descriptor["type"]
        id_type = self.id_type_generator(type)
        
        if id_type:
            schema["$id"] = schema["$id"]+id_type  

        return schema

    def location_schema_generator(self, schema, key, location_type):

        '''
        creating the schema for the location property

        Params
        ------
        schema, key, location_type
            all the params have been used to create
            schema for location

        Returns
        -------
        schema
            according to location type, schema will be generated
            and will be returned the updated schema
        '''

        polygon = {}
        polygon["type"] = "object"
        polygon["properties"] = {}
        polygon["properties"]["coordinates"] = {}
        polygon["properties"]["coordinates"]["type"] = "array"
        polygon["properties"]["coordinates"]["items"] = {}
        polygon["properties"]["coordinates"]["items"]["type"] = "array"
        polygon["properties"]["coordinates"]["items"]["items"] = {}
        polygon["properties"]["coordinates"]["items"]["items"]["type"] = "array"
        polygon["properties"]["coordinates"]["items"]["items"]["items"] =  {}
        polygon["properties"]["coordinates"]["items"]["items"]["items"]["type"] =  "number"
        
        point = {}
        point["type"] = "array"
        point["items"] = {}
        point["items"]["type"] = "number"
        
        line_string = {}
        line_string["type"] = "array"
        line_string["items"] = {}
        line_string["items"]["type"] = "array"
        line_string["items"]["items"] = {}
        line_string["items"]["items"]["type"] = "number" 
        
        schema["properties"][key] = {}
        schema["properties"][key]["type"] = "object"
        schema["properties"][key]["properties"] = {}
        
        if location_type == "polygon":
            schema["properties"][key]["properties"]["geometry"] = polygon
            
        elif location_type == "LineString":
            schema["properties"][key]["properties"]["coordinates"] = line_string
        
        else:
            schema["properties"][key]["properties"]["coordinates"] = point

        return schema
            
    def datetime_schema_generator(self, schema, key):

        '''
        Reads the schema and update the schema
        according to the property type

        Params
        ------
        schema, key
            all the params have been used to create a
            schema for datetime property type
        
        Returns
        -------
        schema
            Schema containing information of type
            and format
        '''

        schema["properties"][key] = {}
        schema["properties"][key]["type"] = "string"
        schema["properties"][key]["format"] = "date-time"

        return schema

    def array_schema_generator(self, schema, key, property_type_name):

        '''
        Reads the schema and update the schema
        according to the property type

        Params
        ------
        schema, key, property_type_name
            all the params have been used to create a
            schema for array type
        
        Returns
        -------
        schema
            Schema containing information of type
            and format
        '''
        
        append_dict = {}
        append_dict["type"] = "array"
        append_dict["items"] = {}
        append_dict["items"]["type"]= property_type_name

        schema["properties"][key] = {}
        schema["properties"][key]["anyOf"] = []
        schema["properties"][key]["anyOf"].append(append_dict)
        schema["properties"][key]["anyOf"].append({"type":property_type_name}) 
        
        return schema

    def basic_type_schema_property(self, schema, key, property_type_name):
        
        '''
        Reads the schema and update the schema
        according to the property type

        Params
        ------
        schema, key, property_type_name
            all the params have been used to create a
            schema for datetime property type
        
        Returns
        -------
        schema
            Schema containing information of type
        '''

        schema["properties"][key] = {}
        schema["properties"][key]["type"] = property_type_name
        
        return schema

    def time_series_aggregation_checker(self, schema, key, time_series_list):
        
        '''
        Reads the schema and update the schema
        according to the property type

        Params
        ------
        schema, key, time_series_list
            all the params have been used to create 
            a schema according to time series aggregation
            type
        
        Returns
        -------
        schema
            Schema containing information of type
            and format
        '''
        
        property_dict = {}
        property_dict["Text"] = "string"
        property_dict["Number"] = "number"
                
        schema["properties"][key] = {}
        schema["properties"][key]["type"] = "object"
        schema["properties"][key]["properties"] = {}
        schema["properties"][key]["required"] = []

        for tsa_val in self.data_descriptor[key].keys():

            if tsa_val in time_series_list:
                
                property_type = self.data_descriptor[key][tsa_val]["dataSchema"].split(":")[1] 
                schema["properties"][key]["properties"][tsa_val] = {}
                schema["properties"][key]["properties"][tsa_val]["type"] = property_dict.get(property_type)
                schema["properties"][key]["required"].append(tsa_val)
        
        return schema

    def json_schema_generator(self):
        
        '''
        Schema will be generated to data descriptor
        
        Returns
        -------
        schema
            Schema containing information of type
            and format of all the property type
        '''      
        property_dict = {}
        property_dict["Text"] = "string"
        property_dict["Number"] = "number"
        
        array_type = ["mediaURL", "comments", "routeStopSequence"]
        
        schema = self.basic_schema_generator()

        for key in self.data_descriptor.keys():

            if key not in ["@context", "type", "dataDescriptorLabel", "description"]:
                time_series_list = ["instValue","avgOverTime", "maxOverTime", "minOverTime", "availableSpotNumber", "totalSpotNumber", "occupiedSpotNumber", "deviceBatteryStatus", "deviceSimNumber", "deviceID", "rfID", "measurand", "deviceModel", "deviceName"] 

#                 time_series_list = ["instValue","avgOverTime", "maxOverTime", "minOverTime"] 
                schema["required"].append(key)
                if any(tsa_val in time_series_list for tsa_val in self.data_descriptor[key].keys()):                    
                    schema = self.time_series_aggregation_checker(schema, key, time_series_list)
                
                elif key == "location":
                    location_type = self.data_descriptor["location"]["dataSchema"].split(":")[1] 
                    schema = self.location_schema_generator(schema, key, location_type)
                
                elif self.property_type(key) == "DateTime":
                    schema = self.datetime_schema_generator(schema, key)

                elif key in array_type:
                    property_type_name = property_dict.get(self.property_type(key))
                    schema = self.array_schema_generator(schema, key, property_type_name)
                
                else:
                    property_type_name = property_dict.get(self.property_type(key))
                    schema = self.basic_type_schema_property(schema, key, property_type_name)

        return schema

root = Tk()
ob = json_schema_generator_ui(root)
root.mainloop()




























