<!DOCTYPE html>
<html lang="id">
<head>m
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartGuard AI - Fraud Detection Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body class="bg-gray-50 text-gray-800">

    <nav class="bg-blue-600 p-4 text-white shadow-lg">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-xl font-bold">🛡️ SmartGuard AI</h1>
            <span class="text-sm bg-blue-700 px-3 py-1 rounded">Hackathon 2026 Prototype</span>
        </div>
    </nav>

    <main class="container mx-auto mt-8 p-4">
        <!-- Header Section -->
        <div class="mb-8">
            <h2 class="text-2xl font-semibold">Monitoring Transaksi Real-Time</h2>
            <p class="text-gray-600">Sistem AI mendeteksi anomali pada setiap transaksi masuk.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <!-- Form Input Simulasi -->
            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100 md:col-span-1">
                <h3 class="font-bold mb-4">Input Transaksi Baru</h3>
                <div class="space-y-4">
                    <div>
                        <label class="block text-sm font-medium">Jumlah Transaksi (Rp)</label>
                        <input id="amount" type="number" placeholder="Contoh: 500000" class="w-full border rounded-lg p-2 mt-1 focus:ring-2 focus:ring-blue-500">
                    </div>
                    <div>
                        <label class="block text-sm font-medium">Lokasi Transaksi</label>
                        <select id="location" class="w-full border rounded-lg p-2 mt-1">
                            <option value="Jakarta">Jakarta (Sering)</option>
                            <option value="Bandung">Bandung (Sering)</option>
                            <option value="Papua">Papua (Jarang)</option>
                            <option value="Luar Negeri">Luar Negeri (Mencurigakan)</option>
                        </select>
                    </div>
                    <button onclick="analyzeTransaction()" class="w-full bg-blue-600 text-white font-bold py-2 rounded-lg hover:bg-blue-700 transition">Analisis dengan AI</button>
                </div>
            </div>

            <!-- Visualisasi & Status -->
            <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100 md:col-span-2">
                <h3 class="font-bold mb-4">Hasil Analisis AI</h3>
                <div id="resultBox" class="hidden p-4 rounded-lg text-center border-2 mb-4">
                    <p id="resultText" class="font-bold text-lg"></p>
                    <p id="resultReason" class="text-sm mt-1"></p>
                </div>
                <div class="h-64 flex items-center justify-center bg-gray-50 rounded-lg border-dashed border-2 border-gray-200">
                    <canvas id="transactionChart"></canvas>
                </div>
            </div>
        </div>

        <!-- Tabel Transaksi -->
        <div class="bg-white p-6 rounded-xl shadow-md border border-gray-100">
            <h3 class="font-bold mb-4">Riwayat Transaksi Terakhir</h3>
            <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                    <thead>
                        <tr class="bg-gray-100">
                            <th class="p-3 border">Waktu</th>
                            <th class="p-3 border">ID User</th>
                            <th class="p-3 border">Jumlah</th>
                            <th class="p-3 border">Status AI</th>
                        </tr>
                    </thead>
                    <tbody id="transactionLog">
                        <tr>
                            <td class="p-3 border">18:05:22</td>
                            <td class="p-3 border">USR-001</td>
                            <td class="p-3 border">Rp 150.000</td>
                            <td class="p-3 border text-green-600 font-bold font-sm italic">✓ Normal</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <script>
        function analyzeTransaction() {
            const amount = document.getElementById('amount').value;
            const location = document.getElementById('location').value;
            const resultBox = document.getElementById('resultBox');
            const resultText = document.getElementById('resultText');
            const resultReason = document.getElementById('resultReason');
            const logTable = document.getElementById('transactionLog');

            if (!amount) return;

            resultBox.classList.remove('hidden');
            
            // Logika Sederhana Simulasi AI (Bisa diganti dengan API Azure Machine Learning)
            let isFraud = false;
            let reason = "Pola transaksi sesuai dengan profil pengguna.";

            if (amount > 5000000 || location === "Luar Negeri") {
                isFraud = true;
                reason = amount > 5000000 ? "Jumlah transaksi jauh di atas rata-rata harian." : "Login dari lokasi tidak dikenal (Luar Negeri).";
            }

            if (isFraud) {
                resultBox.className = "p-4 rounded-lg text-center border-2 border-red-500 bg-red-50 text-red-700 block";
                resultText.innerText = "🚨 TRANSAKSI DICURIGAI FRAUD";
                resultReason.innerText = reason;
            } else {
                resultBox.className = "p-4 rounded-lg text-center border-2 border-green-500 bg-green-50 text-green-700 block";
                resultText.innerText = "✅ TRANSAKSI AMAN";
                resultReason.innerText = reason;
            }

            // Tambah ke Tabel
            const now = new Date().toLocaleTimeString();
            const newRow = `<tr>
                <td class="p-3 border">${now}</td>
                <td class="p-3 border">USR-999</td>
                <td class="p-3 border">Rp ${parseInt(amount).toLocaleString()}</td>
                <td class="p-3 border ${isFraud ? 'text-red-600' : 'text-green-600'} font-bold italic">${isFraud ? '⚠ Fraud' : '✓ Normal'}</td>
            </tr>`;
            logTable.innerHTML = newRow + logTable.innerHTML;
        }

        // Dummy Chart
        const ctx = document.getElementById('transactionChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['10m ago', '8m ago', '6m ago', '4m ago', '2m ago', 'Now'],
                datasets: [{
                    label: 'Volume Transaksi',
                    data: [12, 19, 3, 5, 2, 3],
                    borderColor: 'rgb(59, 130, 246)',
                    tension: 0.1
                }]
            },
            options: { responsive: true, maintainAspectRatio: false }
        });
    </script>
</body>
</html>
