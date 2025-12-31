#!C:\python\python.exe
print("Content-Type:text/html\n\r")
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
        
    </div>

    <div class="main">
        <div class="login-container">
            <p class="title">Let's Get Start</p>
            <div class="separator"></div>
            <p class="welcome-message"></p>

            <form class="login-form" form action="signupaction.py" method ="post">
                <div class="form-control">
                    <input type="text" placeholder="Username" name="uname" required>
                    <i class="fas fa-user"></i>
                </div>
                <div class="form-control">
                    <input type="email" placeholder="E-mail" name="uemail" required>
                    <i class="fas fa-envelope"></i>
                </div>
                <div class="form-control">
                    <input type="password" placeholder="Password" name="upwd" required>
                    <i class="fas fa-lock"></i>
                </div>
                <div class="form-control">
                    <input type="password" placeholder="Confirm Password" name="cpwd" required>
                    <i class="fas fa-unlock"></i>
                </div>

                <button class="submit">Sign up</button>
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
