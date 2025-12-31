#!C:\python\python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql

form = cgi.FieldStorage()

aname=form.getvalue('aname')
aemail=form.getvalue('aemail')
adetails=form.getvalue('adetails')
abudget=form.getvalue('abudget')
adeadline = form.getvalue('adeadline')  
aphonenumber = form.getvalue('aphonenumber')


dbcon = pymysql.connect(host="localhost",user="root",password="root", db="freelancing_user_details")
cursor = dbcon.cursor()

if(dbcon):

    query="""insert into client_applicants values('%s','%s','%s','%s','%s','%s')"""%(aname,aemail,adetails,abudget,adeadline,aphonenumber)
    result = cursor.execute(query)

    if(result>0):
        dbcon.commit()
    else:
        print("Not inserted")
        dbcon.rollback()
else:
    print("error is connecting db")

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
            <h1>Hire Freelancers in India</h1>
            <h4>Browse More than 300000 freelancers in India</h4>
            <h5>Hire skilled freelancers on Javaan, and get work done on a flexible and secure platform.</h5>
            <input type="text" placeholder="Search.." required>
        </div>
    </div> 
    <section id="products" class="product-container">
        <h2>Available Skills in Javaan Technologies</h2>
        <div class="products">
            <form action="apply.py">
                <div class="product">
                  <h3>Web Development</h3>
                  <p class="price">$29.99</p>
                  <button  data-name="Priject Development" data-price="29.99">Apply Now</button>
              </div>
              </form>
              <form action="apply1.py">
                <div class="product">
                  <h3>Project Development</h3>
                  <p class="price">$29.99</p>
                  <button  data-name="Priject Development" data-price="29.99">Apply Now</button>
              </div>
              </form>
            
      <form action="apply2.py">
      <div class="product">
          <h3>Image Editing</h3>
          <p class="price">$29.99</p>
          <button  data-name="Image Editting" data-price="29.99">Apply Now</button>
      </div>
      </form>
      <form action="apply3.py">
      <div class="product">
          <h3>Video Editing</h3>
          <p class="price">$29.99</p>
          <button  data-name="Video Editing" data-price="29.99">Apply Now</button>
      </div>
      </form>
      <form action="apply4.py">
      <div class="product">
          <h3>Social Media Management</h3>
          <p class="price">$29.99</p>
          <button  data-name="Social Media Management" data-price="79.99">Apply Now</button>
      </div>
      </form>
      <form action="apply5.py">
      
      <div class="product">
          <h3>Logo Design</h3>
          <p class="price">$29.99</p>
          <button data-name="Logo Design" data-price="49.99">Apply Now</button>
      </div>
      </form>
            
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
<script>alert("your application is uploaded sucessfully");</script>
""")
