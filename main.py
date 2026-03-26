<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentinel-X Web Interface</title>
    
    <!-- Memuat Library PyScript agar Python Jalan di Browser -->
    <link rel="stylesheet" href="https://pyscript.net">
    <script type="module" src="https://pyscript.net"></script>
    
    <style>
        body { font-family: sans-serif; background: #121212; color: #00ff00; padding: 20px; }
        #terminal { background: #000; border: 1px solid #333; padding: 15px; border-radius: 5px; min-height: 200px; white-space: pre-wrap; }
        h1 { color: #fff; border-bottom: 2px solid #00ff00; display: inline-block; }
    </style>
</head>
<body>

    <h1>Sentinel-X System</h1>
    <div id="terminal">Sedang memuat sistem Python...</div>

    <!-- Menjalankan file main.py milikmu -->
    <script type="py" config='{"packages": []}'>
import sys
from pyscript import display

# Mengarahkan output print ke terminal di browser
class Output:
    def write(self, text):
        display(text, target="terminal", append=True)
    def flush(self):
        pass

sys.stdout = Output()

# Memanggil isi file main.py kamu
try:
    import main
except Exception as e:
    print(f"\n[ERROR] Gagal memuat main.py: {e}")
    </script>

</body>
</html>
