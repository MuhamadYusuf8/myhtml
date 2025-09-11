const wrapper = document.querySelector('.wrapper');
const loginlink = document.querySelector('.login-link');
const registerlink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnlogin-popup');
const iconClose = document.querySelector('.icon-close');

registerlink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginlink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});

const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', (event) => {

    event.preventDefault(); 


    const email = loginForm.querySelector('input[type="email"]').value;
    const password = loginForm.querySelector('input[type="password"]').value;

     if (email === 'user@gmail.com' && password === 'password') {
            alert('Login berhasil!');
            window.location.href = 'main2.html'; 
        } else {
            alert('Username atau password salah. Silakan coba lagi.');
        }
    });