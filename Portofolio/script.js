// script.js
document.addEventListener('DOMContentLoaded', () => {
    // ---- Bagian 1: Animasi Preloader ----
    const preloader = document.querySelector('.preloader');
    const preloaderH1 = document.querySelector('.preloader-content .anim-h1');
    const preloaderH2 = document.querySelector('.preloader-content .anim-h2');
    const header = document.querySelector('.header');
    const homeSection = document.querySelector('#home');
    const otherSections = document.querySelectorAll('.section:not(#home)');

    // Setel awal animasi preloader
    setTimeout(() => {
        preloaderH1.style.animation = 'slideUpH1 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards';
    }, 500);

    // Setel animasi untuk H2 setelah H1 selesai
    setTimeout(() => {
        preloaderH2.style.animation = 'slideUpH2 0.7s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards';
    }, 1200);

    // Fade out preloader dan mulai animasi halaman utama setelahnya
    setTimeout(() => {
        preloader.classList.add('fade-out');

        // Tampilkan header dan section secara bertahap
        setTimeout(() => {
            header.classList.add('show');
            homeSection.classList.add('show');

            // Tambahkan animasi slide-in ke konten utama
            document.querySelector('.intro-content').classList.add('animated');
            document.querySelector('.avatar').classList.add('animated');
            typeWriter();
        }, 800);

        setTimeout(() => {
            otherSections.forEach(section => section.classList.add('show'));
        }, 1500);
    }, 2000);

    const typingTextElement = document.getElementById('typing-text');
    const textToType = "Calon Web Developer";
    let i = 0;

    function typeWriter() {
        if (i < textToType.length) {
            typingTextElement.innerHTML += textToType.charAt(i);
            i++;
            setTimeout(typeWriter, 100);
        } else {
            typingTextElement.style.borderRight = 'none';
        }
    }

    // --- Logika Filter Skills dengan Animasi ---
    const filterButtons = document.querySelectorAll('.filter-btn');
    const skillItems = document.querySelectorAll('.skill-item');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const category = btn.dataset.category;

            skillItems.forEach(item => {
                const isMatch = category === 'all' || item.classList.contains(category);
                item.style.display = isMatch ? 'flex' : 'none';
            });
        });
    });

    // --- Bagian Animasi Proyek saat Scroll ---
    const projectCards = document.querySelectorAll('.project-card');

    const projectObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const delay = entry.target.dataset.delay || 0;
                setTimeout(() => {
                    entry.target.classList.add('show');
                }, delay);
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });

    projectCards.forEach((card, index) => {
        card.dataset.delay = index * 200;
        projectObserver.observe(card);
    });

    // --- Perbaikan: Animasi Ikon Sosial yang bergerak seperti di video ---
    const scrollingSocialIconsContainer = document.querySelector('.scrolling-social-icons');
const initialIcons = scrollingSocialIconsContainer.innerHTML;
scrollingSocialIconsContainer.innerHTML += initialIcons;
scrollingSocialIconsContainer.innerHTML += initialIcons;
    // --- Bagian Smooth Scrolling untuk Tautan Navigasi ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    // --- Logika Tab Contact ---
    const contactTabButtons = document.querySelectorAll('.contact-tab-btn');
    const contactContents = document.querySelectorAll('.contact-content');

    contactTabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Hapus kelas 'active' dari semua tombol
            contactTabButtons.forEach(b => b.classList.remove('active'));
            // Tambahkan kelas 'active' ke tombol yang diklik
            btn.classList.add('active');

            // Sembunyikan semua konten tab
            contactContents.forEach(content => content.classList.remove('show'));

            // Tampilkan konten yang sesuai dengan data-tab
            const targetTab = btn.dataset.tab;
            document.getElementById(`${targetTab}-tab`).classList.add('show');
        });
    });

    // --- Logika Animasi Angka Stats ---
    const statsSection = document.getElementById('stats');
    const statItems = document.querySelectorAll('.stat-item h3');

    const statsObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                statItems.forEach(item => {
                    const target = parseInt(item.innerText.replace('+', ''));
                    let current = 0;
                    const increment = target / 100;
                    const interval = setInterval(() => {
                        current += increment;
                        if (current >= target) {
                            item.innerText = target + '+';
                            clearInterval(interval);
                        } else {
                            item.innerText = Math.ceil(current) + '+';
                        }
                    }, 20);
                });
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });

    statsObserver.observe(statsSection);
});
