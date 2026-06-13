import hashlib, uuid
hwid = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()[:16].upper()
print("Kode akses:", hwid)
print("Kirim kode akses itu ke dev untuk dapat akses.")
