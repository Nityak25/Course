def course_displayer():
    d=["Course-1:PCB Design Workshop","Course-2:Web Development Bootcamp","Course-3:Full Stack Web Development with Node js","Course-4:Building Chatbots with Google Assistant Workshop","Course-5:Python for Engineers"]
    for i in range(len(d)):
        print(d[i])
        print()
    course_num=int(input("Please select a course number that you want to learn ::> "))

    #it will give info related to user's selected course and classes info
    if course_num<=5 and course_num>=1:
        course_info(course_num)
    else:
        print("Sorry you have selected a wrong course number :(")
        
    
def greetings():
    
    print("Welcome to learningbot I can provide information related to all the courses in vedic along with their sessions links :)")
    print()
    
    #asking user name and greeting him
    name=input("May I know your name? please!")
    print()
    print("Hi! "+name.upper()+" a very warm welcome to you")
    print()
    course_displayer()
    
    
#introduction of bot user
greetings()
 
