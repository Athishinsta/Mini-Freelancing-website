#!C:\python\python.exe
print("Content-Type:text/html\n\r")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Javaan Technologies Contact Us</title>
    <link rel="stylesheet" href="contact.css">
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css" integrity="sha512-5Hs3dF2AEPkpNAR7UiOHba+lRSJNeM2ECkwxUIxC1Q/FLycGTbNapWXB4tP889k5T5Ju8fs4b1P5z/iB4nMfSQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</head>
<body>

<div id="id">
   
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
    
    <section id="contact">
        <div id="content">
            <h2>Contact Us</h2>
            <p>Have a query or want to explore our services?
                Contact our friendly team here....!
            </p>
        </div>
       
       
        <div id="container">
            <div id="contactinfo">
                <div id="box">
                    <div id="icon">
                        <b></b><i class="fa-solid fa-location-dot"></i></div>
                        <div id="text">
                            <h3>Address</h3>
                            <p>JAVAAN TECHNOLOGIES,<br>CSE ,HICET</p>
                        </div>
                    </div>
                    <div id="box">
                        <div id="icon">
                            <b></b><i class="fa-solid fa-phone"></i></div>
                            <div id="text">
                                <h3>Phone</h3>
                                <p>637-954-6752</p>
                            </div>
                        </div>
                        <div id="box">
                            <div id="icon">
                                <b></b><i class="fa-solid fa-envelope"></i></div>
                                <div id="text">
                                    <h3>Email</h3>
                                    <p>javaantechnologies@gmail.com</p>
                                </div>
                            </div>
                            <h2 id="txt">Connect with us</h2>
                            <ul id="social">
                                <li><a href="#"><i class="fa-brands fa-facebook"></i></a></li>
                                <li><a href="https://www.instagram.com/_javaantech_official?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw=="><i class="fa-brands fa-instagram"></i></a></li>
                                <li><a href="https://www.linkedin.com/in/team-javaan-976477339?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BTkPl6KPUThqlbepU%2FozAjw%3D%3D"><i class="fa-brands fa-linkedin-in"></i></a></li>
                                <li><a href="https://www.upwork.com/freelancers/~0146f51b4e2ab016ee?mp_source=share"><i class="fa-brands fa-upwork"></i></a></li>
                            </ul>
                            </div>
            
            <div id="contactform">
                <form action="contactaction.py" method="post">
                    <h2>Send Message</h2>
                    <div id="inputbox">
                        <input type="text" name="cname" required="required">
                        <span>Full Name</span>
                    </div>
                    <div id="inputbox">
                        <input type="email" name="cmail" required="required">
                        <span>Email</span>
                    </div>
                    <div id="inputbox">
                        <textarea required="required" name="cmessage"></textarea>
                        <span>Type your Message...</span>
                    </div>
                    <div id="inputbox">
                        <input type="submit" value="Send">
                        
                    </div>
                </form>
            </div>
            </div>
    </section>
    <footer class="footer">
        <p>&copy; 2024 Javaan Technologies | All rights reserved</p>
        <p><i class="fa fa-instagram"></i></p>
        <p><i class="fa fa-whatsapp"></i></p>
        <p><i class="fa fa-linkedin"></i></p>
        <p><i class="fa fa-twitter"></i></p>
    </footer>
</div>
    
</body>
</html>
""")
