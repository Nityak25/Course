"""
1.introduce about bot to user 
2.ask user name
3.wish user with his name 
4.give list of courses from vedic with coach name and info of that course and ask user to select course
5.give sessions names realated to users selection and ask user to select the session number 
6.privode session link to user 
7.print-if u want any other info plase contact me i will be alwas there for u
"""


#defining a function which will give recorded session link
def linkgetter(course_num):
    link=[]


    #WEB DEVELOPMENT BOOTCAMP
    if course_num==2:
        link=["https://youtu.be/UxoX5fGQeiY","https://youtu.be/yyFxGoxyLQM","https://youtu.be/xUmM1ucWnJM","https://youtu.be/UcHg0KPWNkY","https://youtu.be/k2XJcSpUfbM","https://youtu.be/1Y8rKnPTzPc"]



    #Building Chatbots with Google Assistant Workshop
    elif course_num==4:
        link=["https://teams.microsoft.com/l/meetup-join/19%3ameeting_NTFkNjM0M2UtY2ZiZC00YTViLWJiMTAtZDk3NDg5YmE3NjYw%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d","https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZGI5N2ZjNGUtYzhiNy00ZWZhLTg2YzgtNjdmNTM5YTE5NTE4%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d"]
    


    #Full Stack Web Development with Node js
    elif course_num==3:
        link=["https://teams.microsoft.com/l/meetup-join/19%3ameeting_MDc3Y2QwZTctOTQ5ZS00ZjhhLTk2ODMtNGJhNTI4MWZlNjYy%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d","https://youtu.be/BcFb8HWKupI","https://youtu.be/dTSPbW-FCRE","https://youtu.be/C5FFsBLWcME","https://youtu.be/uwAsEB6AegU","https://youtu.be/TE8N9M_KnFc","https://youtu.be/V9yrSVkAUks","https://youtu.be/YxWZhTUGkCk","https://youtu.be/TAwcv9x1T28","https://youtu.be/Qi7SV2nWjOU","https://teams.microsoft.com/l/meetup-join/19%3ameeting_YzQ1NmIzYTUtY2M4MC00ODY1LTk0YzctZjE2ODllZmYxNDA3%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d"]
    
    
    
    #Python for Engineers
    elif course_num==5:
        link=["https://www.youtube.com/watch?v=1zz5VAizJEE","https://www.youtube.com/watch?v=25uW13yKZmE","https://www.youtube.com/watch?v=C6X71gjB9pA","https://youtu.be/hxc7SibPbW8"]
    
    
    

    #PCB Design Workshop
    else:
        link=["https://teams.microsoft.com/l/meetup-join/19%3ameeting_YjEyNWJkMGItMmVmNS00M2YzLTg3YTAtMWRiZTA3MmMzOWFi%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d","https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZGJiYmE2YzUtNjAzNS00YmQ1LTk2NTctZjcyMzhkMTgxOWQ0%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d","https://teams.microsoft.com/l/meetup-join/19%3ameeting_N2JjNGUxMzAtNjU4Yy00MzdkLWFkN2UtMjJlODg5NmM4OGZh%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d","https://teams.microsoft.com/l/meetup-join/19%3ameeting_YTJkZGIzZDYtNTFlYi00MWIyLTljM2MtYzFkZjQ3NDM1ZmIw%40thread.v2/0?context=%7b%22Tid%22%3a%2283187130-08a6-47ca-9d15-94facab49d99%22%2c%22Oid%22%3a%22582ccf99-7f9c-444d-a5c6-eacab40021b0%22%2c%22IsBroadcastMeeting%22%3atrue%7d"]
    
    
    
    
    #ask user to select a class number to get session link
    class_num=int(input("Please select a class number which you want to go through  ::> "))
    print()



    #it will give the link for user selected class
    try:
       class_link=link[class_num-1]
        print("Recorded video link of class you have selected is here :")
        print("           "+class_link)
        print()
        print("If you want any other information plase contact me i am available always for u")

    except:
        print("Sorry you have choosen a wrong class number :(")
    
    
    

#defining a function which will give information
def course_info(course_num):
    
    classname=[]



    #WEB DEVELOPMENT BOOTCAMP
    if course_num==2:
        print("*** Welcome to Become a Web development pro with these skills...!*** - by Prashanth")
        print()
        print("You can get all about HTML,CSS,Bootstrap,Javascript ")
        print()
        classname=["Class one: Introducing the web development and HTML(tags) from roots.","Class two: Introducing CSS by styling the web pages by making a web page as assignment","Class three: Introducing Bootstrap by building a responsive web pages and an assignment","Class four: Practicing building webpages by using HTML,CSS,Bootstrap.","Class five: Getting excited to learn new things in HTML,CSS,Bootstrap.","Class six: Introducing Javascript with a calculator working assignment."]
        



    #Building Chatbots with Google Assistant Workshop
    elif course_num==4:
        print("***Welcome to building chatbots! workshop *** -by Prashanth")
        print()
        print("Chatbots have developed significantly with the introduction of products such as Siri, Cortana, and Google Assistant.")
        print()
        classname=["Class one: Introduction to Chatbots Your first Chatbot","Class two: Building Chatbots with DialogFlow and Deploying to Google Assistant"]
        




    #Full Stack Web Development with Node js
    elif course_num==3:
        print("*** Welcome to Full Stack development with node js *** - by prashanth")
        print()
        print("Full stack development includes pretty much any project where you're working on (or building) both the front and back end of a site or app at the same time.")
        print()
        classname=["Class one: Course Introduction and Revision","Class two: Introduction to Javascript","Class three: Introduction to Node Js","Class four: Understanding Node Js CAll back functions","Class five: Understanding API's","Class six: Introduction to Chatbots","Class seven: Building Telegram Chatbots with API's","Class eight: Getting Started with No SQL Database","Class nine: Connecting MongoDB in Telegram Chatbots","Class ten: Building Web Applications with Express Js","Class eleven: Building Web Applications with Node Js"]
        



    #Python for Engineers
    elif course_num==5:
        print(" *** Welcome to learning Python for ML *** - by Abhinav Dayal")
        print()
        print("Python Skills. If we intend to leverage Python in order to perform machine learning, having some base understanding of Python is crucial.")
        print()
        classname=["Class one: ML Introduction","Class two: Python-Getting Acquainted","Class three: Designing our first Python Project","Class four: Design Thinking-Industry Expert Perspective"]
        




    #PCB Design Workshop
    else:
         print("*** Welcome to PCB Design *** - by Teja")
         print()
         print("PCB design includes how to design a PCB by including different electonic materials like sensors")
         print()
         classname=["Class one: Information about PCB and it's uses","Class two: Steps involved in circuit design","Class three: Reading Datasheet and Start to draw a simple Schematic using some sensors","Class four: Pullup resistors,Decoupling capacitors,PCB Power,Adafruit,EEVBlog"]

    


    for i in range(len(classname)):
        print(classname[i])
        print()
    linkgetter(course_num)
