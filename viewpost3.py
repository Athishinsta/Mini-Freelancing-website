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
            <h3>Image Editing</h3>
            <h5>Job : Image Editing</h5>
            <h5>Price : 5.00$/hr</h5>
            <h4>Tools Uesd in Image Editing</h4>   
            <p>1. Adobe Photoshop</p>
            <p>     It is used by professionals for advanced photo manipulation, graphic design, and digital art creation.</p> 

            <p>2. GIMP (GNU Image Manipulation Program)</p>
            <p>GIMP is a free, open-source alternative to Adobe Photoshop. It provides many advanced features for photo manipulation and graphic design.

            </p> 
            <p>3. Adobe Lightroom</p>

            <p> Adobe Lightroom is primarily used for photo editing, organizing, and batch processing.</p> 
            <p>4. Affinity Photo</p>
            <p>Affinity Photo is an affordable alternative to Photoshop, offering similar professional-grade image editing tools and features.</p> 
            <p>5. Canva</p>
            <p>Canva is an easy-to-use, browser-based design tool for creating social media graphics, posters, and other marketing materials.</p> 
            <p>6. Pixlr</p>

            <p>Pixlr is a browser-based image editor that offers a blend of basic and advanced editing features.</p> 
            <h3>Benefits of Hiring a Professional Image Editor</h3>
            <p>>  For Free Alternatives: GIMP and Paint.NET provide powerful features without the price tag.</p>
            <p>>  For Professional Editing: Adobe Photoshop and Affinity Photo are excellent choices for high-end image manipulation and creative work.</p>
            <p>>  For Simple Edits: Canva, Fotor, and Pixlr are great tools for casual users or those needing quick edits for social media or marketing.</p>
            <p>>  For Vector Graphics: CorelDRAW and Adobe Illustrator are ideal for creating scalable vector designs.</p> 
        </section>
        <section class="bottomcontent">
            <a href="apply2.py" class="form" style="text-decoration: none;">
                <h3>If you Satisfied With our Post Join Us</h3>
                <button>Apply Now</button>
            </a>
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
