#!C:\python\python.exe
print("Content-Type:text/html\n\r")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Web Development Request</title>
  <link rel="stylesheet" href="forget.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.1/css/all.min.css" integrity="sha512-5Hs3dF2AEPkpNAR7UiOHba+lRSJNeM2ECkwxUIxC1Q/FLycGTbNapWXB4tP889k5T5Ju8fs4b1P5z/iB4nMfSQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />

</head>
<body>
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
    <div class="content">
   <script src="script.js"></script>
  
  <section class="forget-form">
    <h2>Reset Password</h2>
    <p>Enter your email address and Reset your Password</p>
    <form action="forgetaction.py" method="post" class="form">
    
      <label for="username">User Name:</label>
      <input type="username" id="email" name="uname" placeholder="Enter your username" required>
      
      <label for="email">Email Address:</label>
      <input type="email" id="email" name="uemail" placeholder="Enter your email" required>
      <label for="changepassword">Change password :</label>
      <input type="password" id="changepassword" name="cpassword" placeholder="Enter New password" required>
      <label for="confirmpassword">Confirm password :</label>
      <input type="cpassword" id="confirmpassword" name="confpassword" placeholder="Confirm your password" required>

      <button type="submit" class="btn-submit">submit</button>
    </form>
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
