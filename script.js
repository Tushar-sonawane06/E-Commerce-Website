document.addEventListener("DOMContentLoaded", function () {
    let cartItemsContainer = document.getElementById("cart-items");
    let cartSubtotalElement = document.getElementById("cart-subtotal");
    let cartTotalElement = document.getElementById("cart-total");
    let checkoutBtn = document.getElementById("checkout-btn");
    let modal = document.getElementById("qr-modal");
    let closeBtn = document.querySelector(".close-btn");

    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    function updateCart() {
        cartItemsContainer.innerHTML = "";
        let total = 0;

        cart.forEach((item, index) => {
            let row = document.createElement("tr");
            row.innerHTML = `
                <td><button class="remove-btn" data-index="${index}"><i class="fa fa-trash"></i></button></td>
                <td><img src="${item.image}" alt="Product" class="cart-img"></td>
                <td>${item.name}</td>
                <td class="price">₹${item.price}</td>
                <td><input type="number" value="${item.quantity}" class="qty-input" data-index="${index}"></td>
                <td class="subtotal">₹${(item.price * item.quantity).toFixed(2)}</td>
            `;
            cartItemsContainer.appendChild(row);
            total += item.price * item.quantity;
        });

        cartSubtotalElement.textContent = `₹${total.toFixed(2)}`;
        cartTotalElement.textContent = `₹${total.toFixed(2)}`;
        localStorage.setItem("cart", JSON.stringify(cart));
    }

    cartItemsContainer.addEventListener("change", function (e) {
        if (e.target.classList.contains("qty-input")) {
            let index = e.target.getAttribute("data-index");
            cart[index].quantity = parseInt(e.target.value);
            updateCart();
        }
    });

    cartItemsContainer.addEventListener("click", function (e) {
        if (e.target.closest(".remove-btn")) {
            let index = e.target.closest(".remove-btn").getAttribute("data-index");
            cart.splice(index, 1);
            updateCart();
        }
    });

    checkoutBtn.addEventListener("click", function (e) {
        e.preventDefault();
        let totalAmount = cartTotalElement.textContent;
        document.getElementById("popup-total").textContent = totalAmount;
        modal.style.display = "flex";
    });

    closeBtn.addEventListener("click", function () {
        modal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });

    updateCart();
});

// Get Buttons
const signupBtn = document.querySelector(".signupbtn");
const signinBtn = document.querySelector(".signinbtn");

// Get Form Fields
const nameField = document.querySelector(".namefield");
const title = document.querySelector(".title");
const signupUnderline = document.querySelector(".underline");

// Add Click Event Listeners
signupBtn.addEventListener("click", function() {
    nameField.style.display = "block"; // Show Name Field
    title.textContent = "Sign Up"; 
    signupUnderline.style.transform = "translateX(0)"; 
    
    signupBtn.classList.remove("disable");
    signinBtn.classList.add("disable");
});

signinBtn.addEventListener("click", function() {
    nameField.style.display = "none"; // Hide Name Field
    title.textContent = "Sign In"; 
    signupUnderline.style.transform = "translateX(100%)"; 

    signinBtn.classList.remove("disable");
    signupBtn.classList.add("disable");
});
