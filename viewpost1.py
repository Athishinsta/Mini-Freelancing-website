#!C:\python\python.exe
print("Content-Type:text/html\n\r")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Main page</title>
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="viewpost1.css">
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
        <section class="topcontent">
            <h3>Web Development</h3>
            <h5>Job : Web Development</h5>
            <h5>Price : 20.00$/hr</h5>
            <h4>Tools Uesd in Web Development</h4>   
            <p>1. Front-End Development Tools</p>
            <p>     HTML / CSS / JavaScript , Frameworks (Bootstrap , JavaScript) , Code Editor (Visual Studio Code) , GitHub.</p> 

            <p>2. Back-End Development Tools</p>
            <p>     Python , Php , Java , Ruby , Node JS</p> 
            <p>3. Databases</p>

            <p>     Mongo DB , MySQL , SQLite</p> <br>
            <p>>  Web design trends change with time.</p>
            <p>>  When you find a web designer, the freelancer will make your website design as per the latest trends and your brand guidelines.</p> 
            <p>>  The design of a website has to also be SEO friendly.</p>
            <p>>  While the design of a website is what makes the visitors stick to it, its SEO attributes help the page appear on top of the results in search engines.</p> 
            <p>>  Since both these aspects of interface design are interrelated, you can hire web designers online to get SEO-friendly designs.</p>

            <p>>  The competition for selling products or services online is high, primarily because of the number of choices available.</p> 
            <p>>  It is very easy for them to switch from one brand to another, attractive and efficient website design or digital asset can make a difference with your UI and customer acquisition.
            </p>
            <h3>Benefits of Hiring a Professional Web Designer</h3>
            <p>>  Website designing services are not offered as one-size-fits-all.</p>
            <p>>  Depending on the business requirements and brand requirements, the design of websites and other assets are created differently.</p>
            <p>>  If you still wonder why to hire a web designer, remember that they will make sure your website gets designed to suit your specific business needs.</p>
            <p>>  The designer will request details of your business and the objective of the website and accordingly approach the design.</p>
            <p>>  Website designers will also ensure that each page has quality UX on both desktop and mobile applications.</p> 
        </section>
        <section class="bottomcontent">
            <form action="apply.py" method="post" class="form">
                <h3>If you Satisfied With our Post Join Us</h3>
                <button>Apply Now</button>
            </form>
        </section>
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
