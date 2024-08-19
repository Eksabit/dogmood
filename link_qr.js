document.getElementById('open-popup').onclick = function(event) {
    event.preventDefault();
    document.getElementById('popup').style.display = 'flex';

    // Генерация QR-кода
    var qr = new QRious({
        element: document.getElementById('qr-code'),
        value: 'https://t.me/+BFHkpWtDcvAzNGVi', // Замените на ссылку на ваш Telegram канал
        size: 200
    });
};

document.getElementById('close-popup').onclick = function() {
    document.getElementById('popup').style.display = 'none';
};

// Закрытие окна при клике вне его
window.onclick = function(event) {
    if (event.target == document.getElementById('popup')) {
        document.getElementById('popup').style.display = 'none';
    }
};
