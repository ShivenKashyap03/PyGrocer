![image](https://user-images.githubusercontent.com/112420208/199553159-1a3a1d80-4833-44b4-a9cc-b79b6fdb3f2a.png)

# What is it?
A simple demonstration to show how an app could be implemented to order basic nessecities over the internet, and how using a simple sql database, various functions can be branched out, such as plotting a graph of sales for a store over a period of time.

# Dependencies:
- The project uses tkinter and ttk (which are pre-installed with any python distribution) to render widgets and the associated themes.
- Apart from tkinter, the native modules os and datetime are also used.
- PIL (dep. Pillow) is used to render all the images as PhotoImage objects.
- sqlite3 is used to handle the database interactions.
- matplotlib is used for plotting the graph.

# Installation:
Click on Code -> Download ZIP, and extract the zip anywhere on your computer.
Further, run the pygrocer.py source code file in the folder using any Python3.x compiler.

# Features:
1. Supports toggling between Dark and Light Themes (at the bottom of the application window, a Checkbutton can be used for the same.)
<img src="https://user-images.githubusercontent.com/112420208/188271690-760d9204-e8e0-4fe2-b8a7-d6785e8c9474.png">
<img src="https://user-images.githubusercontent.com/112420208/188271698-721538b3-8fc6-4612-8035-4bb7d94b2b5e.png">

2. A login prompt to switch between Administrator and User demonstrations:
![image](https://user-images.githubusercontent.com/112420208/188271731-71447f68-aafa-4810-887a-4130facb72c9.png)![image](https://user-images.githubusercontent.com/112420208/195977178-98799932-c3bb-4e15-a2fa-a3413e7346b2.png)


`he username and password for the Administrator session are "shiven", and for the User account - "tulika".`

3. Demonstrating ordering items as User session:
![image](https://user-images.githubusercontent.com/112420208/188271792-eb7fa525-7d05-4373-8b8d-006b4b2d1164.png)
![image](https://user-images.githubusercontent.com/112420208/188271813-eb9d03e0-094b-478d-91ce-9838a9e07f74.png)

Further, the user can see their invoice:
![image](https://user-images.githubusercontent.com/112420208/188271835-19a047ac-e763-4d15-a3ec-2e75dc0ff982.png)
![image](https://user-images.githubusercontent.com/112420208/188271840-746e2caa-2123-48c1-a658-10c23df14359.png)

If "Confirm Order" is clicked, the shopping details are written to the database (after validity checks), and can be used for plotting graphs for the administrator.
![image](https://user-images.githubusercontent.com/112420208/188271895-e4140c2c-14ca-4278-b83a-a3da7b0c636e.png)

4. As an administrator, one can visualize the graph for the past sales over the previous months of the year by clicking on "Visualize past sales", or get the sql database content by clicking on "Check sales record" and copy the output from the console window that runs alongside.
![image](https://user-images.githubusercontent.com/112420208/188271954-d1b624fe-49b2-458f-a73d-2b13cf7a8bde.png)

![image](https://user-images.githubusercontent.com/112420208/188271967-6c856655-4b66-47c2-847f-d02f1a19cf46.png)
![image](https://user-images.githubusercontent.com/112420208/188271972-69adf35f-f3f6-45ee-8841-090c6c4d2a8e.png)

# Side Notes:
the project is a very minimalistic demonstration, and therefore, lacks many features that one would intuitively expect from such an app, but improvements for the same are along the way.
Also, it supports only windows for the moment, since managing file paths on most linux distributions via python is very clunky and cumbersome, plus, tkinter builds on ubuntu based distros have a lot of inconsistencies in rendering widget themes.

![image](https://user-images.githubusercontent.com/112420208/199550984-db4b93ca-7e56-47af-a87b-40640afc66a2.png)

