## APSMİKRO

Kurumsal çoklu-şube destekli satış/stok/cari altyapısı. Bu depo;

- Backend: FastAPI (Python) — kimlik doğrulama, şube yönetimi, temel CRUD
- Frontend: (ileride) React + TypeScript web yönetim paneli
- El Terminali: (ileride) Windows/WinForms .NET istemcisi

### Hızlı Başlangıç (Backend)

1) Gereksinimler: Python 3.11+
2) Bağımlılıkları kurun ve sunucuyu çalıştırın:

```bash
cd backend
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3) Çevre değişkenleri için `.env` dosyanızı `backend` klasörüne ekleyin. Örnek için `.env.example` dosyasına bakın.

### Yol Haritası

- Kullanıcı/rol yönetimi, yetkilendirme
- Çoklu şube (tanım, yetki, varsayılan depo vb.)
- Stok, cari, satış, satınalma modülleri (kademeli)
- El terminali istemcisi (Windows) API entegrasyonu
- Web yönetim paneli (React) — login ve şube modülü

Bu proje MS Yazılım çözümlerini referans alarak geliştirilecektir.

# apsmikro