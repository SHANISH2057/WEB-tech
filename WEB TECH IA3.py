<!DOCTYPE html> 
<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>TUNE TRADERS</title> 
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"> 
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.7.1/dist/jquery.slim.min.js"></script> 
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script> 
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js"></script> 
    <style> 
        body { 
            margin: 0; 
            padding: 0; 
            background-color: #f4f4f4; 
            color: #333; 
        } 
        header { 
            background-color: #4CAF50; 
            color: white; 
            text-align: center; 
            padding: 1px; 
        } 
        nav { 
            background-color: #333; 
            color: white; 
            padding: 0.5em; 
        } 
        nav ul { 
            list-style: none; 
            padding: 0; 
            display: flex; 
            justify-content: center; 
        } 
        nav ul li { 
            margin: 0 1em; 
        } 
        nav ul li a { 
            color: white; 
            text-decoration: none; 
        } 
        main { 
            padding: 1em; 
        } 
        section { 
            margin-bottom: 2em; 
        } 
        footer { 
            background-color: #333; 
            color: white; 
            text-align: center; 
            padding: 1em 0; 
        } 
        .hidden { 
            display: none; 
        } 
    </style> 
</head> 
<body> 
    <header> 
        <h1>MUSIC WONDER WORLD</h1> 
        <nav> 
            <ul> 
                <li><a href="#home">Home</a></li> 
                <li><a href="#instruments">Instruments</a></li> 
                <li><a href="#cart">Cart</a></li> 
                <li><a href="#contact">Contact</a></li> 
                <li>  
                    <div class="container"> 
                        <div class="dropdown"> 
                            <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">LOGIN</button> 
                            <div class="dropdown-menu"> 
                                <a class="dropdown-item" href="userlog.py">USER</a> 
                                <a class="dropdown-item" href="adminlog.py">ADMIN</a> 
                                <a class="dropdown-item" href="employeelog.py">EMPLOYEE</a> 
                            </div> 
                        </div> 
                    </div> 
                </li> 
            </ul> 
        </nav> 
    </header> 

    <main> 
        <section id="home"> 
            <h2>Welcome to Music Wonder World</h2> 
            <p>Explore various musical instruments and make purchases online.</p> 
        </section> 

        <section id="instruments"> 
            <h2>Instruments</h2> 
            <div class="container-fluid"> 
                <div class="row"> 
                    <div class="col-xs-12 col-sm-6 col-md-3 col-lg-4"> 
                        <div class="card"> 
                            <img class="card-img-top" src="./mainproject/m1.jpg" alt="Image not found" height="200" width="100%"> 
                            <h5 class="card-title">GUITAR</h5> 
                            <p>Description</p> 
                            <a href="#" class="btn btn-primary">PLACE ORDER</a> 
                        </div> 
                    </div> 
                    <div class="col-xs-12 col-sm-6 col-md-3 col-lg-4"> 
                        <div class="card"> 
                            <img class="card-img-top" src="./mainproject/m2.jpg" alt="Image not found" height="200" width="100%"> 
                            <h5 class="card-title">VEENA</h5> 
                            <p>Description</p> 
                            <a href="#" class="btn btn-primary">PLACE ORDER</a> 
                        </div> 
                    </div> 
                    <div class="col-xs-12 col-sm-6 col-md-3 col-lg-4"> 
                        <div class="card"> 
                            <img class="card-img-top" src="./mainproject/m3.jpg" alt="Image not found" height="200" width="100%"> 
                            <h5 class="card-title">TUBAS</h5> 
                            <p>Description</p> 
                            <a href="#" class="btn btn-primary">PLACE ORDER</a> 
                        </div> 
                    </div> 
                    <div class="col-xs-12 col-sm-6 col-md-3 col-lg-4"> 
                        <div class="card"> 
                            <img class="card-img-top" src="./mainproject/m4.jpg" alt="Image not found" height="200" width="100%"> 
                            <h5 class="card-title">PIANO</h5> 
                            <p>Description</p> 
                            <a href="#" class="btn btn-primary">PLACE ORDER</a> 
                        </div> 
                    </div> 
                    <div class="col-xs-12 col-sm-6 col-md-3 col-lg-4"> 
                        <div class="card"> 
                            <img class="card-img-top" src="./mainproject/m5.jpg" alt="Image not found" height="200" width="100%"> 
                            <h5 class="card-title">FLUTE</h5> 
                            <p>Description</p> 
                            <a href="#" class="btn btn-primary">PLACE ORDER</a> 
                        </div> 
                    </div> 
                    <div class="col-xs-12 col-sm-6 col-md-3 col-lg-4"> 
                        <div class="card"> 
                            <img class="card-img-top" src="./mainproject/m3.jpg" alt="Image not found" height="200" width="100%"> 
                            <h5 class="card-title">DRUMS</h5> 
                            <p>Description</p> 
                            <a href="#" class="btn btn-primary">PLACE ORDER</a> 
                        </div> 
                    </div> 
                </div> 
            </div> 
        </section> 

        <section id="cart"> 
            <h2>Your Cart</h2> 
            <div id="cart-items"></div> 
            <button id="checkout-button">Checkout</button> 
        </section> 

        <section id="contact"> 
            <h2>Contact Us</h2> 
            <p>Mobile: 6382187690</p> 
            <p>Email: musicworld@gmail.com</p> 
        </section> 
    </main>   

    <footer> 
        <p>&copy; 2024 Music Wonder World</p> 
    </footer> 

    <script> 
        document.addEventListener('DOMContentLoaded', () => { 
            const cartItems = document.getElementById('cart-items'); 
            const checkoutButton = document.getElementById('checkout-button'); 
            let cart = []; 

            function displayInstruments(instruments) { 
                const instrumentList = document.getElementById('instrument-list'); 
                instruments.forEach(instrument => { 
                    const item = document.createElement('div'); 
                    item.classList.add('instrument'); 
                    item.innerHTML = ` 
                        <h3>${instrument.name}</h3> 
                        <p>Price: $${instrument.price}</p> 
                        <button onclick="addToCart(${instrument.id})">Add to Cart</button> 
                    `; 
                    instrumentList.appendChild(item); 
                }); 
            } 

            fetch('/api/instruments') 
                .then(response => response.json()) 
                .then(data => displayInstruments(data)); 

            window.addToCart = function (id) { 
                fetch(`/api/instruments/${id}`) 
                    .then(response => response.json()) 
                    .then(instrument => { 
                        cart.push(instrument); 
                        displayCart(); 
                    }); 
            }; 

            function displayCart() { 
                cartItems.innerHTML = ''; 
                cart.forEach(item => { 
                    const cartItem = document.createElement('div'); 
                    cartItem.classList.add('cart-item'); 
                    cartItem.innerHTML = ` 
                        <h4>${item.name}</h4> 
                        <p>Price: $${item.price}</p> 
                    `; 
                    cartItems.appendChild(cartItem); 
                }); 
            } 

            checkoutButton.addEventListener('click', () => { 
                alert('Proceeding to checkout'); 
            }); 
        }); 
    </script> 
</body> 
</html>
