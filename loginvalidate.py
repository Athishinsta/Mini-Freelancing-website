#!C:\python\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

form = cgi.FieldStorage()

uname=form.getvalue('uname')
upwd=form.getvalue('upwd')


dbcon = pymysql.connect(host="localhost",user="root",password="root", db="freelancing_user_details")
cursor = dbcon.cursor()



flag1 = False
flag2 = False

if(dbcon):
    
    query2 = """select uname from users"""
    result2 = cursor.execute(query2)
    
    for names in cursor:
        for i in names:
            if(i == uname):
                flag1 = True
                break

    query3 = """select upwd from users where uname = "%s" """%(uname)
    result3 = cursor.execute(query3)

    for pwd in cursor:
        for j in pwd:
            if(j == upwd):
                flag2 = True
                break

            
    if(uname == "admin" and upwd == "admin123"):
        query4 = """select * from client_applicants"""
        result4 = cursor.execute(query4)
    
        
        #admin page
        print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main page</title>
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="admin.css">
</head>
<body>
    <div class="container">
        <nav class="navbar">
            <div class="logo">
               <img src="jt1.png" width="290px" height="60px">
            </div>
            <div class="menu-bar" id="mobile-menu">
                <i class="fas fa-bars"></i>
            </div>
            
            <ul class="nav-list">
                <li><a href="index.py"><i class="fas fa-home"></i> Home</a></li>
                <li><a href="about us.py"><i class="fas fa-info-circle"></i> About</a></li>
                <li><a href="service.py"><i class="fas fa-briefcase"></i> Services</a></li>
                <li><a href="contact us.py"><i class="fas fa-envelope"></i> Contact</a></li>
                <li><a href="login.py"><i class="fa-solid fa-right-to-bracket"></i></i>Login</a></li>
                <li><a href="signup.py"><i class="fa-solid fa-registered"></i>Signup</a></li>
            </ul>
        </nav>
       <script src="script.js"></script>
    </div>

    <div class="content">
         
        <div class="section1">
            <h1>All APPLCATION DETAILS</h1>
        </div>
        <div class="section2" style="color:#031d44">
            <table style="border:0px solid #031d44; border-spacing:0px; border-collapse:collapse; ">
                <tr>
                    <th>Full Name</th>
                    <th>e-mail address</th>
                    <th>Project Description</th>
                    <th>Budget</th>
                    <th>Deadline</th>
                    <th>Phone Number</th>
                </tr>""")
        
        res = cursor.fetchall()
        count = 0
        for row in res:
            count = count + 1
            tname = row[0]
            print("""<tr><td>%s</td>"""%(tname))
            tmail = row[1]
            print("""<td>%s</td>"""%(tmail))
            tdesc = row[2]
            print("""<td>%s</td>"""%(tdesc))
            tBudget = row[3]
            print("""<td>%s</td>"""%(tBudget))
            tdeadline = row[4]
            print("""<td>%s</td>"""%(tdeadline))
            tnumber = row[5]
            print("""<td>%s</td></tr>"""%(tnumber))

        print("""
            </table>
        </div>
    </div>
    <div class="section2" style="color:#031d44">
        <h1>USER MESSAGES</h1>
        <table style="border:0px solid #031d44; border-spacing:0px; border-collapse:collapse;">
                <tr>
                    <th>User Name</th>
                    <th>e-mail address</th>
                    <th>Message</th>
                </tr>
    """)
        query5 = """select * from Messages"""
        result5 = cursor.execute(query5)
        
        res = cursor.fetchall()
        for row in res:
            cname = row[0]
            print("""<tr><td>%s</td>"""%(cname))
            cmail = row[1]
            print("""<td>%s</td>"""%(cmail))
            cmessage = row[2]
            print("""<td>%s</td></tr>"""%(cmessage))
            
        
        print("""
        </table>  
    </div>
    <div class="logout">
    <a href="index.py" style="background-image: linear-gradient(to right, #031d44, #15a0e1); border: 0px">LOG OUT</a>
    </div>
    <footer class="footer">
        <p>&copy; 2024 Javaan Technologies | All rights reserved</p>
        <li><a href="#"><i class="fa-brands fa-facebook"></i></a></li>
        <li><a href="https://www.instagram.com/_javaantech_official?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="><i class="fa-brands fa-instagram"></i></a></li>
        <li><a href="https://www.linkedin.com/in/team-javaan-976477339?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTkPl6KPUThqlbepU%2FozAjw%3D%3D"><i class="fa-brands fa-linkedin-in"></i></a></li>
        <li><a href="https://www.upwork.com/freelancers/~0146f51b4e2ab016ee?mp_source=share"><i class="fa-brands fa-upwork"></i></a></li>
       
    </footer>
</body>
</html>
""")
    
    elif(flag1 == True and flag2 == True):
        
        if(dbcon):
            query="""insert into logindetails values('%s','%s')"""%(uname,upwd)
            result = cursor.execute(query)

            if(result>0):
                dbcon.commit()
            else:
                print("Not inserted")
                dbcon.rollback()
            
        print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main page</title>
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <nav class="navbar">
            <div class="logo">
               <img src="jt1.png" width="290px" height="60px">
            </div>
            <div class="menu-bar" id="mobile-menu">
                <i class="fas fa-bars"></i>
            </div>
            
            <ul class="nav-list">
                <li><a href="index.py"><i class="fas fa-home"></i> Home</a></li>
                <li><a href="about us.py"><i class="fas fa-info-circle"></i> About</a></li>
                <li><a href="service.py"><i class="fas fa-briefcase"></i> Services</a></li>
                <li><a href="contact us.py"><i class="fas fa-envelope"></i> Contact</a></li>
                <li><a href="login.py"><i class="fa-solid fa-right-to-bracket"></i></i>Login</a></li>
                <li><a href="signup.py"><i class="fa-solid fa-registered"></i>Signup</a></li>
            </ul>
        </nav>
       <script src="script.js"></script>
    </div>

    <div class="content">
         
        <div class="section1">
        <form action="searchaction.py" method="post">
            <h1>Hire Freelancers in India</h1>
            <h4>Browse More than 300000 freelancers in India</h4>
            <h5>Hire skilled freelancers on Javaan, and get work done on a flexible and secure platform.</h5>
            <input style="margin-right:10px;" type="text" name="textbox" placeholder="Search.." required>
            <button class="fa fa-search" style="font-size:22px; font-weight:bold; border:1px solid #eef4ed;"></button>
        </form>
        </div>
    </div> 
    <section id="products" class="product-container">
        <h2>Available Skills in Javaan Technologies</h2>
        <div class="products">
            <form action="viewpost1.py">
                <div class="product">
                  <h3>Web Development</h3>
                  <p class="price">23000+ Freelancers</p>
                  <button  data-name="Priject Development" data-price="29.99">View Post</button>
              </div>
              </form>
              <form action="viewpost2.py">
                <div class="product">
                  <h3>Project Management</h3>
                  <p class="price">25000+ Freelancers</p>
                  <button  data-name="Priject Development" data-price="29.99">View Post</button>
              </div>
              </form>
            
      <form action="viewpost3.py">
      <div class="product">
          <h3>Image Editing</h3>
          <p class="price">27000+ Freelancers</p>
          <button  data-name="Image Editting" data-price="29.99">View Post</button>
      </div>
      </form>
      <form action="viewpost4.py">
      <div class="product">
          <h3>Social Media Management</h3>
          <p class="price">29000+ Freelancers</p>
          <button  data-name="Social Media Management" data-price="29.99">View Post</button>
      </div>
      </form>
      <form action="viewpost5.py">
      <div class="product">
          <h3>Video Editing</h3>
          <p class="price">31000+ Freelancers</p>
          <button  data-name="video Editing" data-price="79.99">View Post</button>
      </div>
      </form>
      <form action="viewpost6.py">
      <div class="product">
          <h3>Logo Design</h3>
          <p class="price">50000+ Freelancers</p>
          <button data-name="Logo Design" data-price="49.99">View Post</button>
      </div>
      </form>
            <script>alert("Login Successful!");</script>
        </div>
    </section>

    <footer class="footer">
        <p>&copy; 2024 Javaan Technologies | All rights reserved</p>
        <li><a href="#"><i class="fa-brands fa-facebook"></i></a></li>
        <li><a href="https://www.instagram.com/_javaantech_official?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="><i class="fa-brands fa-instagram"></i></a></li>
        <li><a href="https://www.linkedin.com/in/team-javaan-976477339?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTkPl6KPUThqlbepU%2FozAjw%3D%3D"><i class="fa-brands fa-linkedin-in"></i></a></li>
        <li><a href="https://www.upwork.com/freelancers/~0146f51b4e2ab016ee?mp_source=share"><i class="fa-brands fa-upwork"></i></a></li>
       
    </footer>
</body>
</html>
""")

    elif(flag1 == True and flag2 == False):
        print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link rel="stylesheet" href="login.css">
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    <title>Login landing page</title>
</head>
<body>
    
    <div class="container">    
    <nav class="navbar">
        <div class="logo">
           <img src="jt1.png" width="290px" height="60px">
        </div>
        <div class="menu-bar" id="mobile-menu">
            <i class="fas fa-bars"></i>
        </div>
        
        <ul class="nav-list">
            <li><a href="index.py"><i class="fas fa-home"></i> Home</a></li>
            <li><a href="about us.py"><i class="fas fa-info-circle"></i> About</a></li>
            <li><a href="service.py"><i class="fas fa-briefcase"></i> Services</a></li>
            <li><a href="contact us.py"><i class="fas fa-envelope"></i> Contact</a></li>
            <li><a href="login.py"><i class="fa-solid fa-right-to-bracket"></i></i>Login</a></li>
            <li><a href="signup.py"><i class="fa-solid fa-registered"></i>Signup</a></li>
        </ul>
    </nav>
   <script src="script.js"></script>
    </div>
    </div>
    <div class="section">
    <div class="side">
        <img src="./images/img.svg" alt="">
    </div>

    <div class="main">
        <div class="login-container">
            <p class="title">Welcome Back</p>
            <div class="separator"></div>
            <p class="welcome-message">Please, provide login credential to proceed and have access to all our services</p>

            <form class="login-form" form action="loginvalidate.py" method="post">
                <div class="form-control">
                    <input type="text" placeholder="Username" name="uname">
                    <i class="fas fa-user"></i>
                </div>
                <div class="form-control">
                    <input type="password" placeholder="Password" name="upwd">
                    <i class="fas fa-lock"></i>
                </div>
                <script>document.write("Entered Password is Wrong!");</script>
                <a href="forget.py">forget password</a>
                <button class="submit">Login</button>
            </form>
        </div>
    </div>
    </div>
    <footer class="footer">
        <p>&copy; 2024 Javaan Technologies | All rights reserved</p>
        <li><a href="#"><i class="fa-brands fa-facebook"></i></a></li>
        <li><a href="https://www.instagram.com/_javaantech_official?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="><i class="fa-brands fa-instagram"></i></a></li>
        <li><a href="https://www.linkedin.com/in/team-javaan-976477339?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTkPl6KPUThqlbepU%2FozAjw%3D%3D"><i class="fa-brands fa-linkedin-in"></i></a></li>
        <li><a href="https://www.upwork.com/freelancers/~0146f51b4e2ab016ee?mp_source=share"><i class="fa-brands fa-upwork"></i></a></li>
       
    </footer>
    
</body>
</html>
""")

    elif(flag1 == False):
        print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <link rel="stylesheet" href="login.css">
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
    <title>Login landing page</title>
</head>
<body>
    
    <div class="container">    
    <nav class="navbar">
        <div class="logo">
           <img src="jt1.png" width="290px" height="60px">
        </div>
        <div class="menu-bar" id="mobile-menu">
            <i class="fas fa-bars"></i>
        </div>
        
        <ul class="nav-list">
            <li><a href="index.py"><i class="fas fa-home"></i> Home</a></li>
            <li><a href="about us.py"><i class="fas fa-info-circle"></i> About</a></li>
            <li><a href="service.py"><i class="fas fa-briefcase"></i> Services</a></li>
            <li><a href="contact us.py"><i class="fas fa-envelope"></i> Contact</a></li>
            <li><a href="login.py"><i class="fa-solid fa-right-to-bracket"></i></i>Login</a></li>
            <li><a href="signup.py"><i class="fa-solid fa-registered"></i>Signup</a></li>
        </ul>
    </nav>
   <script src="script.js"></script>
    </div>
    </div>
    <div class="section">
    <div class="side">
        <img src="./images/img.svg" alt="">
    </div>

    <div class="main">
        <div class="login-container">
            <p class="title">Welcome Back</p>
            <div class="separator"></div>
            <p class="welcome-message">Please, provide login credential to proceed and have access to all our services</p>

            <form class="login-form" form action="loginvalidate.py" method="post">
                <div class="form-control">
                    <input type="text" placeholder="Username" name="uname">
                    <i class="fas fa-user"></i>
                </div>
                <div class="form-control">
                    <input type="password" placeholder="Password" name="upwd">
                    <i class="fas fa-lock"></i>
                </div>
                <script>document.write("User does not exist!");</script>
                <button class="submit">Login</button>
            </form>
        </div>
    </div>
    </div>
    <footer class="footer">
        <p>&copy; 2024 Javaan Technologies | All rights reserved</p>
        <li><a href="#"><i class="fa-brands fa-facebook"></i></a></li>
        <li><a href="https://www.instagram.com/_javaantech_official?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="><i class="fa-brands fa-instagram"></i></a></li>
        <li><a href="https://www.linkedin.com/in/team-javaan-976477339?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTkPl6KPUThqlbepU%2FozAjw%3D%3D"><i class="fa-brands fa-linkedin-in"></i></a></li>
        <li><a href="https://www.upwork.com/freelancers/~0146f51b4e2ab016ee?mp_source=share"><i class="fa-brands fa-upwork"></i></a></li>
       
    </footer>
    
</body>
</html>
""")
else:
    print("error is connecting db")


