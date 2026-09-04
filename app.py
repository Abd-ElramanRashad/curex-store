<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CureX - Healthcare Solutions</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Cairo', sans-serif; background-color: #f8fafc; margin: 0; padding: 0; color: #1e293b; }
        header { background: #1B365D; color: white; padding: 20px 40px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        .logo-text h1 { margin: 0; font-size: 26px; color: #ffffff; }
        .logo-text span { color: #00A896; font-size: 13px; font-weight: 600; display: block; }
        .hero { background: linear-gradient(135deg, #1B365D 0%, #028090 100%); color: white; text-align: center; padding: 50px 20px; }
        .container { max-width: 1200px; margin: 30px auto; padding: 0 20px; }
        .products-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .product-card { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 4px solid #00A896; display: flex; flex-direction: column; justify-content: space-between; }
        .product-card h3 { margin-top: 0; color: #1B365D; }
        .price { font-size: 18px; color: #00A896; font-weight: bold; margin: 10px 0; }
        .stock-info { font-size: 12px; color: #64748b; margin-bottom: 15px; }
        input, button { width: 100%; padding: 10px; margin-top: 8px; border: 1px solid #cbd5e1; border-radius: 6px; box-sizing: border-box; font-family: 'Cairo', sans-serif; }
        button { background: #1B365D; color: white; border: none; font-weight: bold; cursor: pointer; transition: 0.3s; }
        button:hover { background: #00A896; }
        footer { background: #0f172a; color: #94a3b8; text-align: center; padding: 30px 20px; margin-top: 50px; }
        footer h3 { color: white; }
        .success-msg { background: #d1fae5; color: #065f46; padding: 15px; border-radius: 6px; text-align: center; margin-bottom: 20px; font-weight: bold; display: none; }
    </style>
</head>
<body>

    <header>
        <div class="logo-text">
            <h1>CureX</h1>
            <span>Healthcare Solutions</span>
        </div>
    </header>

    <div class="hero">
        <h2>نظام طلبات السلع والمنتجات الطبية</h2>
        <p>اطلب احتياجاتك بكل سهولة ويسر وسنتواصل معك فوراً</p>
    </div>

    <div class="container">
        <div id="successAlert" class="success-msg">تم إرسال طلبك بنجاح! سيتم التواصل معك قريباً.</div>
        
        <h2 style="color: #1B365D; border-bottom: 2px solid #00A896; padding-bottom: 10px;">السلع المتاحة حالياً</h2>
        
        <div class="products-grid" id="productsContainer">
            <!-- المنتجات المستخرجة من شيت الإكسيل بتاعك -->
        </div>
    </div>

    <footer>
        <h3>نحن هنا للمساعدة</h3>
        <p>العنوان: البحيرة، دمنهور، العمرية</p>
        <p>رقم الهاتف: 01068260189</p>
        <p style="margin-top: 15px; font-size: 12px;">© 2026 CureX Healthcare Solutions</p>
    </footer>

    <script>
        // المنتجات الموجودة في شيت الإكسيل الخاص بك
        const products = [
            { code: "ITM-001", name: "Digital Blood Pressure Monitor", category: "Medical Devices", price: 650.0, stock: 5 },
            { code: "ITM-002", name: "Digital Infrared Thermometer", category: "Medical Devices", price: 270.0, stock: 7 },
            { code: "ITM-003", name: "N95 Medical Face Masks (Box)", category: "Consumables", price: 95.0, stock: 18 },
            { code: "ITM-004", name: "Medical Examination Gloves (Box)", category: "Consumables", price: 110.0, stock: 10 },
            { code: "ITM-005", name: "Pulse Oximeter Fingertip", category: "Medical Devices", price: 180.0, stock: 7 },
            { code: "ITM-006", name: "Stethoscope Dual Head", category: "Diagnostic Tools", price: 340.0, stock: 3 }
        ];

        const container = document.getElementById('productsContainer');

        products.forEach(p => {
            const card = document.createElement('div');
            card.className = 'product-card';
            card.innerHTML = `
                <div>
                    <h3>${p.name}</h3>
                    <div class="stock-info">الفئة: ${p.category} | الرصيد المتاح: ${p.stock} قطعة</div>
                    <div class="price">${p.price} ج.م</div>
                </div>
                <form onsubmit="submitOrder(event, '${p.name}', ${p.price})">
                    <input type="number" placeholder="الكمية المطلوبة" min="1" max="${p.stock}" required>
                    <input type="text" placeholder="الاسم الكريم" required>
                    <input type="text" placeholder="رقم الهاتف" required>
                    <input type="text" placeholder="العنوان بالتفصيل" required>
                    <input type="email" placeholder="البريد الإلكتروني (اختياري)">
                    <button type="submit">تأكيد الطلب</button>
                </form>
            `;
            container.appendChild(card);
        });

        function submitOrder(event, itemName, price) {
            event.preventDefault();
            const alertBox = document.getElementById('successAlert');
            alertBox.style.display = 'block';
            event.target.reset();
            window.scrollTo({ top: 0, behavior: 'smooth' });
            setTimeout(() => { alertBox.style.display = 'none'; }, 5000);
        }
    </script>
</body>
</html>
