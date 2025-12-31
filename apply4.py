#!C:\python\python.exe
print("Content-Type:text/html\n\r")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Web Development Request</title>
  <link rel="stylesheet" href="apply.css">
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
   <script src="script.js"></script>
  <header class="header">
    <h1>Apply for   Social Media Management Services</h1>
    <p>Please fill out the form to request our social media management services.</p>
  </header>

 
  <section class="request-form">
    <h2>Kindly Fill The Form</h2>
    <form action="applyaction.py" method="post" class="form">
      <label for="clientName">Full Name:</label>
      <input type="text" id="clientName" placeholder="Enter your name" name="aname" required>

      <label for="email">Email Address:</label>
      <input type="email" id="email" placeholder="Enter your email" name="aemail" required>

      <label for="projectDetails">Project Details:</label>
      <textarea id="projectDetails" placeholder="Describe your project" name = "adetails" required></textarea>

      <label for="budget">Budget ($):</label>
      <input type="number" id="budget" placeholder="Enter your budget" name = "abudget" required>

      <label for="deadline">Deadline:</label>
      <input type="date" id="deadline" name = "adeadline" required>

      <label for="phone">Phone Number:</label>
      <input type="tel" id="phone" placeholder="Enter your phone number" name = "aphonenumber" required>

      <button type="submit" class="btn-submit">Apply Now</button>
    </form>
  </section>

  
  <section class="payment">
    <h2>Make Payment</h2>
    <p>To confirm your request, please scan the QR code below for payment.</p>
    <div class="qr-code">
      <img src="WhatsApp Image 2024-11-29 at 8.35.43 PM.jpeg" alt="QR Code">
    </div>
    <p>Scan the QR code to make a payment and confirm your project request.</p>
  </section>
  <header class="header">
    <h1> You Can Also Apply For These Services</h1>
   
  </header>
  <section id="products" class="product-container">
    
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
      <button  data-name="Video Editing" data-price="29.99">Apply Now</button>
  </div>
  </form>
  <form action="apply3.py">
  <div class="product">
      <h3>Video Editing</h3>
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

""")
