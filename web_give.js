document.addEventListener('DOMContentLoaded', () => {
    const screens = document.querySelectorAll('.screen-container');
    const loadingScreen = document.getElementById('loading-screen');
    const mainMenu = document.getElementById('main-menu');
    const progressBar = document.querySelector('.progress');
    const progressPercent = document.querySelector('.progress-percent');
    const menuButtons = document.querySelectorAll('.menu-btn');
    const navButtons = document.querySelectorAll('.nav-btn');

    // Data untuk setiap fitur
    const messages = [
        "Hi,",
        "Happy Birthday!",
        "Hari ini aku pengen kamu ngerasain semua hal positif dan keajaiban yang cuma bisa didapetin kalo kamu ada di dunia ini.",
        "Semoga segala keinginanmu tercapai, apalagi yang kocak-kocak dan gak biasa, karena kamu tuh unik banget! Aku selalu percaya kalau kamu bisa melewati semua tantangan dengan kekuatan dan semangat yang luar biasa.",
        "Selalu Bersyukur dan Berterima Kasih kediri Sendiri Karna Sudah Bertahan Sejauh ini. Kamu bener-bener bikin hari-hari Orang orang yang ada di sekitar kamu jadi lebih bahagia dan senang dan penuh warna. Semoga di tahun yang baru ini, kamu makin bahagia, makin sukses, dan tentunya makin dikuatkan Imannya.",
    ];
    let currentMessageIndex = 0;
    const messageText = document.querySelector('.message-text');

    const galleryImages = [
        { src: 'photo1.jpg', label: 'Our First Date' },
        { src: 'photo2.jpg', label: 'Birthday Moment' },
        { src: 'photo3.jpg', label: 'Adventure Time' },
        { src: 'photo4.jpg', label: 'Cozy Together' },
        { src: 'photo5.jpg', label: 'Sweet Memories' },
        { src: 'photo6.jpg', label: 'Laugh Together' },
        { src: 'photo7.jpg', label: 'Perfect Day' },
        { src: 'photo8.jpg', label: 'Love Forever ❤️' }
    ];
    let currentImageIndex = 0;
    const galleryImg = document.getElementById('gallery-img');
    const imageLabel = document.querySelector('.image-label');
    const capturedCount = document.getElementById('captured-count');

    // Fungsi untuk mengubah layar
    const switchScreen = (targetId) => {
        screens.forEach(screen => screen.classList.remove('active'));
        document.getElementById(targetId).classList.add('active');
    };

    // Loading screen animation
    let progress = 0;
    const interval = setInterval(() => {
        progress += 1;
        progressBar.style.width = `${progress}%`;
        progressPercent.textContent = `${progress}%`;
        if (progress >= 100) {
            clearInterval(interval);
            setTimeout(() => {
                loadingScreen.classList.remove('active');
                mainMenu.classList.add('active');
            }, 500);
        }
    }, 20);

    // Menu button functionality
    menuButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetId = button.dataset.target;
            switchScreen(targetId);

            // Inisialisasi konten untuk layar yang dituju
            if (targetId === 'message-screen') {
                currentMessageIndex = 0;
                displayMessage();
            } else if (targetId === 'gallery-screen') {
                currentImageIndex = 0;
                displayGalleryImage();
            }
        });
    });

    // Navigasi tombol "Kembali"
    navButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetId = button.dataset.target;
            switchScreen(targetId);
        });
    });

    // --- Message Screen Logic ---
    const displayMessage = () => {
        messageText.innerHTML = messages.slice(0, currentMessageIndex + 1).join('<br><br>');
        document.querySelector('.next-message').style.display = (currentMessageIndex < messages.length - 1) ? 'inline-block' : 'none';
        document.getElementById('skip-message').style.display = 'inline-block';
    };

    document.getElementById('next-message').addEventListener('click', () => {
        if (currentMessageIndex < messages.length - 1) {
            currentMessageIndex++;
            displayMessage();
        }
    });

    document.getElementById('skip-message').addEventListener('click', () => {
        currentMessageIndex = messages.length - 1;
        displayMessage();
    });

    // --- Gallery Screen Logic ---
    const displayGalleryImage = () => {
        if (galleryImages[currentImageIndex]) {
            galleryImg.src = galleryImages[currentImageIndex].src;
            imageLabel.textContent = galleryImages[currentImageIndex].label;
            capturedCount.textContent = currentImageIndex + 1;
        }
    };

    document.querySelector('.next-image').addEventListener('click', () => {
        if (currentImageIndex < galleryImages.length - 1) {
            currentImageIndex++;
            displayGalleryImage();
        } else {
            // Kembali ke menu utama setelah galeri selesai
            switchScreen('main-menu');
        }
    });

    // --- Tetris Logic (placeholder) ---
    // Logika game Tetris akan sangat kompleks dan memerlukan kode tambahan yang signifikan.
    // Kode di bawah ini hanya menunjukkan bagaimana elemen HTML akan berinteraksi.
    // Anda bisa mencari library Tetris di GitHub atau membuatnya sendiri.

    // placeholder untuk game Tetris
    const tetrisCanvas = document.getElementById('tetris-board');
    if (tetrisCanvas) {
        const ctx = tetrisCanvas.getContext('2d');
        tetrisCanvas.width = 300;
        tetrisCanvas.height = 600;
        
        ctx.fillStyle = '#1a1a1a'; // Ganti warna background tetris
        ctx.fillRect(0, 0, tetrisCanvas.width, tetrisCanvas.height);
    }
});