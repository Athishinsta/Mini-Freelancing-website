#!C:\python\python.exe
print("Content-Type:text/html\n\r")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Services</title>
    <link rel="stylesheet" href="service.css">
    <script src="https://kit.fontawesome.com/0014ad3e43.js" crossorigin="anonymous"></script>
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
    <header>
        <h1>Our Services</h1>
    </header>
    <main>
        <div class="services-container">
            
            <div class="service">
                
                <h2>Video Editing</h2>
                <p>We use advanced tools like Adobe Premiere Pro, Final Cut Pro, and DaVinci Resolve to bring your videos to life.</p>
                <button class="read-more" data-target="video-editing">Read More</button>
            </div>
           
            <div class="service">
                
                <h2>Image Editing</h2>
                <p>Enhance your images with Photoshop, Lightroom, and other professional tools for stunning visuals.</p>
                <button class="read-more" data-target="image-editing">Read More</button>
            </div>
            
            <div class="service">
               
                <h2>Logo Designing</h2>
                <p>Create unique and professional logos using Adobe Illustrator and Canva.</p>
                <button class="read-more" data-target="logo-designing">Read More</button>
            </div>
           
            <div class="service">
                
                <h2>Project Development</h2>
                <p>End-to-end project solutions using Agile methodologies and the latest tech stack.</p>
                <button class="read-more" data-target="project-development">Read More</button>
            </div>
            
            <div class="service">
               
                <h2>Website Development</h2>
                <p>Build responsive and dynamic websites with HTML, CSS, JavaScript, and frameworks like React and Angular.</p>
                <button class="read-more" data-target="website-development">Read More</button>
            </div>
            
            <div class="service">
                
                <h2>Social Media Management</h2>
                <p>Boost your online presence with tailored strategies and content management on all platforms.</p>
                <button class="read-more" data-target="social-media-management">Read More</button>
            </div>
        </div>
       
        <div class="details-section" id="video-editing">
            <h2>Video Editing Details</h2>
            <video controls style="width: 600px;border-radius: 15px;" >
                <source src="videos/example.mp4" type="video/mp4" >
                Your browser does not support the video tag.
            </video>
            <p style="font-weight: bold;">We specialize in transforming raw footage into captivating videos that align with your brand's vision. Whether you're creating content for YouTube, a commercial, an event highlight reel, or a corporate video, our editing services are designed to enhance your story. From seamless transitions, motion graphics, color grading, and sound design, we ensure that every detail of the video is polished and professional. We work with you to understand the goals of the video, the target audience, and the message you want to convey, ensuring the final product is both engaging and effective..</p>
        <h3 style="color: #C7B96F;">Support:</h3>
      <p style="font-weight: bold;"> We offer unlimited revisions to ensure the final video meets your expectations, no matter the complexity. We support a variety of video formats for online platforms, social media, or broadcast. We also assist with video encoding, compression, and delivery to ensure compatibility across all devices and platforms.</p></div>
        <div class="details-section" id="image-editing">
            <h2>Image Editing Details</h2>
            <img src="images/pexels-george-milton-7014342.jpg" alt="Image Editing Example" width="700px" height="500px" style="border-radius: 15px;">
            <p style="font-weight: bold;">Enhance your photos, adjust lighting, and create stunning visuals with professional image editing tools.Our image editing services are designed to transform your photos into stunning visuals that communicate your brand’s message. We provide a wide range of services, including basic photo enhancements, retouching, and color correction. For e-commerce, we specialize in background removal, image optimization, and product styling to ensure your products stand out. We also offer advanced techniques such as photo manipulation, creative compositing, and the application of artistic effects. Whether you need professional headshots, social media content, or commercial photography editing, we use industry-standard tools to ensure the highest quality.</p>
            <h3 style="color: #C7B96F;">Support:</h3>
            <p style="font-weight: bold;">We understand the importance of precision in image editing, which is why we offer unlimited revisions to meet your exact specifications. All images are delivered in high-resolution formats suitable for print and digital use, and we ensure that the final product is consistent with your vision. Our team is ready to work with you through every step of the editing process to ensure that the final result aligns with your brand standards.</p>

            </div>
        <div class="details-section" id="logo-designing">
            <h2>Logo Designing Details</h2>
            <img src="images/logo.jpg" alt="Logo Design Example" width="700px" height="500px" style="border-radius: 15px;">
            <p style="font-weight: bold;">Create custom logos tailored to your brand using modern design techniques and tools.A great logo is the cornerstone of your brand identity. At Javaan Technologies, we specialize in creating logos that capture the essence of your business while making a lasting impression. Our design process involves extensive research to understand your brand's values, target audience, and competitive landscape. We create logos that are not only visually striking but also versatile and timeless, ensuring they work well across all mediums, from websites and social media to print materials. We focus on simplicity, ensuring that your logo is both memorable and functional, effectively representing your brand’s personality.</p>
            <h3 style="color: #C7B96F;">Support:</h3>
            <p style="font-weight: bold;">We provide multiple logo concepts for you to choose from and allow for revisions to ensure the logo is exactly what you envision. Our services include providing the logo in various file formats for use on different platforms and media. We also offer brand guidelines to ensure consistency in how your logo is used across all materials.</p>
          </div>
        <div class="details-section" id="project-development">
            <h2>Project Development Details</h2>
            <img src="images/people-working-as-team-company.jpg" alt="Project Development Example" width="800px" height="500px" style="border-radius: 15px;">
            <p style="font-weight: bold;">Comprehensive project development services, from ideation to execution, tailored to your needs.At Javaan Technologies, we provide comprehensive project development services, guiding your idea from inception to completion. Whether it's a software application, a website, a mobile app, or a custom business solution, our approach is results-driven. We work closely with you to define clear objectives, set milestones, and establish realistic timelines. Our team uses agile development methodologies to ensure flexibility and timely delivery while maintaining high-quality standards. We focus on creating scalable, secure, and user-friendly solutions that not only meet but exceed your expectations.</p>
        
            <h3 style="color: #C7B96F;">Support:</h3>
            <p style="font-weight: bold;">Our project development services extend beyond just delivery. After launch, we offer ongoing support to ensure everything runs smoothly. This includes regular updates, bug fixes, performance enhancements, and additional features. Our team is available for troubleshooting, system upgrades, and providing solutions to any emerging needs. We aim for long-term partnerships, providing continuous maintenance and ensuring the longevity of the project.</p>
            </div>
        <div class="details-section" id="website-development">
            <h2>Website Development Details</h2>
          <img src="images/web.jpg"  width="800px" height="500px" style="border-radius: 15px; ">
            <p style="font-weight: bold;">Web develop modern, responsive websites that align with your business objectives.We craft visually stunning, responsive, and user-friendly websites tailored to meet your business goals. From simple informational websites to complex e-commerce platforms and custom web applications, our team ensures every detail is optimized for performance and usability. We focus on creating a seamless user experience (UX) while maintaining modern design aesthetics. Our expertise includes front-end and back-end development, CMS integration, SEO optimization, and mobile-first design, ensuring your website stands out and functions flawlessly across all devices.</p>
            <h3 style="color: #C7B96F;">Support:</h3>
            <p style="font-weight: bold;">We provide comprehensive post-launch support, including regular updates, security patches, and performance optimization. Additionally, our team is available for troubleshooting, scaling, and adding new features as your business grows.</p>

          </div>
        <div class="details-section" id="social-media-management">
            <h2>Social Media Management Details</h2>
            <img src="images/media.jpg" alt="Social Media Example" width="800px" height="500px" style="border-radius: 15px;">
            <p style="font-weight: bold;">Our social media management services are designed to help you build a strong, consistent presence across all major social media platforms, including Facebook, Instagram, Twitter, LinkedIn, and more. We work with you to develop a social media strategy that aligns with your business goals, target audience, and brand voice. Our services include content creation, post scheduling, and managing daily interactions with your followers to foster engagement. We also offer community management, ensuring that comments and messages are responded to promptly, which helps build trust and loyalty with your audience. Whether you’re looking to increase brand awareness, drive traffic to your website, or engage your community, our approach is designed to help you achieve measurable results.</p>
            <h3 style="color: #C7B96F;">Support:</h3>
            <p style="font-weight: bold;">Our team provides regular analytics and performance reports to track the effectiveness of your social media campaigns. We adjust strategies based on data insights to continuously optimize performance and engagement. We also stay updated on the latest trends and platform updates to ensure that your social media presence remains relevant and effective. Our goal is to help you stay ahead of the competition and build a loyal online community.

            </p>
            </div>
    </main>
    <script src="serve.js"></script>
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
