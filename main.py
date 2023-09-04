import tkinter as tk
import random
import link_generator
import webbrowser
import time
# Function to generate random fields
def generate_fields(input_token:tk.Entry,input_department:tk.Entry,input_course:tk.Entry):
   token = input_token.get()
   course = input_course.get()
   department = input_department.get()
   for link in link_generator.generate_links(token=token,list_department=department,list_course=course):
      webbrowser.open(url=link)
      time.sleep(1)
    
   #  output_label.config(text="Generated Fields: " + ', '.join(map(str, generated_fields)))
def main():
   # Create the main application window
   app = tk.Tk()
   app.title("Field Generator App")

   # Create an token input field
   token_label = tk.Label(app, text="Enter Token:")
   token_label.pack()
   input_token = tk.Entry(app)
   input_token.pack()
   
   department_label = tk.Label(app, text="Enter Department Number:")
   department_label.pack()
   input_department = tk.Entry(app)
   input_department.pack()
   
   
   course_label = tk.Label(app, text="Enter Course Number:")
   course_label.pack()
   input_course = tk.Entry(app)
   input_course.pack()



   # Create a "Generate" button
   generate_button = tk.Button(app, text="Generate Links", command=lambda : generate_fields(input_token,input_department,input_course))
   generate_button.pack()

   # Create a label to display the generated fields
   output_label = tk.Label(app, text="Generated Fields: ")
   output_label.pack()

   # Start the Tkinter main loop
   app.mainloop()

if __name__ == '__main__':
   main()
