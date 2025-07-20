import os

# Define base path where HTML files will be saved
base_path = r"C:\\Users\\rishi\\Desktop\\E-com (2)\\E-com\\img\\try\\"

# Ensure the directory exists
os.makedirs(base_path, exist_ok=True)

# HTML template
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecommerce Website</title>

    <!-- FontAwesome link -->
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.10.0/css/all.css">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <!-- Header Section -->
    <section id="header"> <!-- top bar-->
        <!-- Fixed alt attribute and removed stray quotes -->
        <a class ="active" href="index.html"><img src="img/logo.png" class="logo" alt="Logo"></a>

        <div>
            <ul id="navbar">
                <li><a class ="active" href="index.html">Home</a></li>
                <li><a class ="active"href="shop.html">Shop</a></li>
                <li><a class ="active"href="log.html">Login</a></li>
                <li><a class ="active"href="about.html">About</a></li>
                <li><a class ="active"  href="cart.html"><i class="fas fa-shopping-cart"></i></a></li>
            </ul>
        </div>
      </section>

    <!-- Product Details Section -->
    <section id="prodetails" class="section-p1">
        <div class="single-pro-image">
            <img src="{main_img}" width="100%" id="MainImg" alt="Main Product Image">

            <div class="small-img-group">
                {small_imgs}
            </div>
        </div>

        <div class="single-pro-details">
            <h6>Home / T-Shirts</h6>
            <h4>Men's Fashion T-Shirts</h4>
            <h2>₹599</h2>
            <select>
                <option>Select size</option>
                <option>XL</option>
                <option>XXL</option>
                <option>Small</option>
                <option>Large</option>
            </select>
            <input type="number" value="1" min="1">
            <button class="normal">Add To Cart</button>
            <h4>Product Details</h4>
            <span>This is a high-quality men's fashion t-shirt, perfect for casual wear.</span>
        </div>
    </section>

    <!-- Featured Products Section -->
    <section id="pro" class="section-p1">
        <h2>Featured Products</h2>
        <p>New Summer New Clothes</p>
        <div class="pro-con">
            <div class="pi">
                <img src="{main_img}" alt="Printed Casual Shirt">
                <div class="des">
                    <span>Luna</span>
                    <h5>Men's Printed Casual Shirt</h5>
                    <div class="star">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                    </div>
                    <h4>₹599</h4>
                </div>
                <a href="#"><i class="fal fa-shopping-cart cart"></i></a>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="footer-container">
            <div class="footer-section">
                <h3>Contact Us</h3>
                <p>Address: 123 Sample Street, Fictional City, Wonder State, 45678</p>
                <p>Email: contact@samplewebsite.com</p>
                <p>Phone: +123 456 7890</p>
            </div>

            <div class="footer-section">
                <h3>Affiliated Companies</h3>
                <ul class="affiliates-list">
                    <li>GPay</li>
                    <li>Razorpay</li>
                    <li>Luna</li>
                    <li>Gucci</li>
                    <li>Prada</li>
                </ul>
            </div>

            <div class="footer-section newsletter">
                <h3>Subscribe to Our Newsletter</h3>
                <p>Get updates on best deals, flash offers, and stock clearances.</p>
                <form action="#" method="POST" class="newsletter-form">
                    <input type="email" placeholder="Enter your email" required>
                    <button type="submit">Subscribe</button>
                </form>
            </div>
        </div>

        <div class="footer-bottom">
            <p>© 2025 Sample Website. All rights reserved.</p>
        </div>
    </footer>

    <script>
        var MainImg = document.getElementById("MainImg");
        var smallimg = document.getElementsByClassName("small-img");

        for (let i = 0; i < smallimg.length; i++) {{
            smallimg[i].onclick = function() {{
                MainImg.src = smallimg[i].src;
            }};
        }}
    </script>

    <script src="script.js"></script>
</body>
</html>
"""

for i in range(9, 17):  # Products 9 to 16
    # Start from image 33
    main_img = f"img/prolist/{32 + (i - 9) * 4 + 1}.jpeg"

    # Generate small images for each product
    small_imgs = "".join([
        f'<div class="small-img-col">\n<img src="img/prolist/{32 + (i - 9) * 4 + j}.jpg" width="100%" class="small-img" alt="Product Image {j}">\n</div>\n'
        for j in range(1, 5)
    ])

    # Format HTML content
    html_content = html_template.format(main_img=main_img, small_imgs=small_imgs)
    file_path = os.path.join(base_path, f"s{i}product.html")

    # Write HTML file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Generated: {file_path}")

