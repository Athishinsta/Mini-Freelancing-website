#!C:\python\python.exe
print("Content-Type:text/html\n\r")

import cgi

form = cgi.FieldStorage()

searchcontent=form.getvalue('textbox')

searchcontent = searchcontent.lower() 

if(searchcontent == "web development" or searchcontent == "web design" or searchcontent == "web" or searchcontent == "website"):

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

elif(searchcontent == "project management" or searchcontent == "project development" or searchcontent == "project"):
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
            <h3>Project Management</h3>
            <h5>Job : Project Management</h5>
            <h5>Price : 40.00$/hr</h5>
            <h4>Tools Uesd in Project Management</h4>   
            <p>1. Project Management Tools</p>
            <p>     Trello , Jira , Asana.</p> 

            <p>2. Version Control and Code Management</p>
            <p>     Git , Github , Bitbucket</p> 
            <p>3. Communication and Collaboration Tools</p>

            <p>    Slack , Microsoft, Zoom , Google Workshop </p>
            <p>4. Design and Prototyping Tools</p>
            <p>    Figma , Adobe XD , InVision , Sketch</p> 
            <p>5. Development Tools</p>
            <p>   VS Code , Postman , Docker , Vagrant</p> 
            <p>6. Continuous Integration/Continuous Deployment (CI/CD) Tools</p>

            <p>   Jenkins , Travis CI , Circle CI , GitLab CI</p> 
            <p>7. Testing and Quality Assurance Tools</p>
            <p>   Selenium , JUnit , Mocha , Cypress , TestRail</p>
            <h3>Benefits of Hiring a Professional Project Developer</h3>
            <p>>  Collaboration: Enhanced teamwork and communication boost productivity and morale.</p>
            <p>>  Clarity and Focus: Clear goals and well-defined objectives lead to better alignment of the team and stakeholders.</p>
            <p>>  Quality and Standards: Better quality management through structured testing and reviews.</p>
            <p>>  Resource and Risk Management: Proper planning ensures efficient use of resources and reduces risks.</p> 
        </section>
        <section class="bottomcontent">
            <a href="apply1.py" class="form" style="text-decoration: none;">
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

elif(searchcontent == "image editing" or searchcontent == "photo editing" or searchcontent == "poster making" or searchcontent == "image"):
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

elif(searchcontent == "social media management" or searchcontent == "social media content management" or searchcontent == "social media" or searchcontent == "socialmedia" or searchcontent == "social"):
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
            <h3>Social Media Management</h3>
            <h5>Job : Social Media Management</h5>
            <h5>Price : 50.00$/hr</h5>
            <h4>Tools Uesd in Social Media Management</h4>   
            <p>1. Hootsuite</p>
            <p> One of the most popular and comprehensive social media management platforms.</p> 

            <p>2. Buffer</p>
            <p> Buffer is a streamlined tool for scheduling posts, tracking performance, and engaging with audiences.

            </p> 
            <p>3. Sprout Social</p>

            <p>Sprout Social is a feature-rich platform designed for managing social media profiles, tracking performance, and engaging with audiences.</p> 
            <p>4. Later</p>
            <p> Later (formerly known as "Post Planner") is a social media scheduling tool focused on visual content, particularly for Instagram.</p> 
            <p>5. CoSchedule</p>
            <p>CoSchedule is a marketing calendar and social media management tool that integrates scheduling, content creation, and marketing campaigns.</p> 
            <p>6. Zoho Social</p>

            <p>Zoho Social is a social media management tool for businesses, offering features like scheduling, monitoring, and reporting.</p> 
            <h3>Benefits of Hiring a Professional Social Media Manager</h3>
            <p>>  Social media management is a crucial part of modern marketing that offers a wide range of benefits for businesses and content creators.</p>
            <p>>   From increasing brand visibility and engagement to tracking performance and optimizing content, it helps businesses reach their goals effectively.</p>
            <p>>  If you still wonder why to hire a web designer, remember that they will make sure your website gets designed to suit your specific business needs.</p>
            <p>>   With the right tools and strategies, social media management becomes an invaluable resource for growing and maintaining a successful online presence.</p> 
        </section>
        <section class="bottomcontent">
            <a href="apply4.py" class="form" style="text-decoration: none;">
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

elif(searchcontent == "video editing"):
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
            <h3>Video Editing</h3>
            <h5>Job : Video Editing</h5>
            <h5>Price : 20.00$/hr</h5>
            <h4>Tools Uesd in Video Editing</h4>   
            <p>1. Adobe Premiere Pro</p>
            <p>     Adobe Premiere Pro is one of the leading video editing tools used by professionals in the film, television, and digital media industries.</p> 

            <p>2. Final Cut Pro</p>
            <p>Final Cut Pro is a professional video editing software developed by Apple.

            </p> 
            <p>3. DaVinci Resolve</p>

            <p> DaVinci Resolve, developed by Blackmagic Design, is a powerful video editing and color grading software used in professional film production.</p> 
            <p>4. iMovie</p>
            <p> iMovie is a simple, user-friendly video editing software developed by Apple, available on macOS and iOS devices.</p> 
            <p>5. HitFilm Express</p>
            <p>HitFilm Express is a free video editing and visual effects software that offers both basic editing tools and advanced VFX capabilities.</p> 
            <p>6. Lightworks</p>

            <p>Lightworks is a professional video editing software used in Hollywood film editing.</p> 
            <h3>Benefits of Hiring a Professional Video Editing</h3>
            <p>>  It allows creators to refine their ideas, engage their audience, and produce polished content that stands out.</p>
            <p>>  Video editing enhances creativity, improves communication, and contributes to the quality of content, whether it’s for professional filmmaking, marketing, or personal projects.</p>
            <p>>  If you still wonder why to hire a web designer, remember that they will make sure your website gets designed to suit your specific business needs.</p>
            <p>>  Whether you are a beginner or a professional, the benefits of video editing are essential for producing high-quality and effective videos.</p> 
        </section>
        <section class="bottomcontent">
            <a href="apply3.py" class="form" style="text-decoration: none;">
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

elif(searchcontent == "logo design"):
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
            <h3>Logo Design</h3>
            <h5>Job : Logo Design</h5>
            <h5>Price : 5.00$/hr</h5>
            <h4>Tools Uesd in Logo Design</h4>   
            <p>1. Adobe Illustrator</p>
            <p>Adobe Illustrator is the industry-standard software for creating vector-based logos.</p> 

            <p>2. CorelDRAW</p>
            <p>CorelDRAW is another powerful vector graphic design tool used for logo creation.

            </p> 
            <p>3. Canva</p>

            <p> Canva is a user-friendly online design tool with templates for logo creation.</p> 
            <p>4. Affinity Designer</p>
            <p> Affinity Designer is a vector graphic design software that's a great alternative to Adobe Illustrator.</p> 
            <p>5. Inkscape</p>
            <p>Inkscape is a free, open-source vector graphic design software that offers many of the same features as Illustrator and CorelDRAW.</p> 
            <p>6. Gravit Designer</p>

            <p>Gravit Designer is a full-featured vector design tool with a cloud-based version and offline apps.</p> 
            <h3>Benefits of Hiring a Professional Logo Design</h3>
            <p>>  Professional tools like Adobe Illustrator and CorelDRAW are perfect for advanced designers, while tools like Canva and Looka cater to beginners and those looking for quick and easy solutions.</p>
            <p>>  The choice of logo design tool depends on the designer's skill level, requirements, and budget.</p>
            <p>>  For those looking for free or open-source alternatives, Inkscape and Gravit Designer are excellent options.</p>
            <p>>  Whether you're creating a logo for a business, personal brand, or project, there's a tool that fits your needs.</p>
        </section>
        <section class="bottomcontent">
            <a href="apply5.py" class="form" style="text-decoration: none;">
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

else:
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
           <script>alert("content not available!");</script> 
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
   
