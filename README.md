# SOAP/XML Meter Confirmation Service

This project is a **SOAP/XML mock service** built with **FastAPI**.  
It simulates meter confirmation requests and returns SOAP/XML responses based on the meter number provided.

---

## 🚀 How It Works

The service exposes one endpoint:

```
POST /meter/confirm/
```

- Accepts **SOAP/XML requests**
- Parses the meter number (`msno`) from the request body
- Returns different SOAP/XML responses depending on the meter number

---

## 📋 Meter Number Logic (msno)

| Meter Number   | Response Type       | Description                          |
|----------------|---------------------|--------------------------------------|
| `01234567890`  | ✅ Success           | Returns a successful confirmation    |
| `01234567891`  | ⚠️ Specified Fault  | Returns a SOAP fault for this meter  |
| `01234567892`  | ❌ Meter Not Found  | Returns "Meter not found" response   |
| Any other      | ⚡ Invalid Format   | Returns an invalid format response   |

---

## 🧪 Test Cases (with Expected SOAP/XML Responses)

### 1. Success (01234567890)
**Request:**
```bash
curl.exe -X POST http://127.0.0.1:8000/meter/confirm/ -H "Content-Type: text/xml" -d "@tests/payload_success.xml"
```

**Expected Response:**
```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ConfirmMeterResponse>
      <status>SUCCESS</status>
      <message>Meter confirmed successfully</message>
    </ConfirmMeterResponse>
  </soap:Body>
</soap:Envelope>
```

---

### 2. Specified Fault (01234567891)
**Request:**
```bash
curl.exe -X POST http://127.0.0.1:8000/meter/confirm/ -H "Content-Type: text/xml" -d "@tests/payload_fault_91.xml"
```

**Expected Response:**
```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>SOAP-ENV:Server</faultcode>
      <faultstring>Specified meter fault</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

---

### 3. Meter Not Found (01234567892)
**Request:**
```bash
curl.exe -X POST http://127.0.0.1:8000/meter/confirm/ -H "Content-Type: text/xml" -d "@tests/payload_fault_92.xml"
```

**Expected Response:**
```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ConfirmMeterResponse>
      <status>FAILED</status>
      <message>Meter not found</message>
    </ConfirmMeterResponse>
  </soap:Body>
</soap:Envelope>
```

---

### 4. Invalid Format (e.g. "123")
**Request:**
```bash
curl.exe -X POST http://127.0.0.1:8000/meter/confirm/ -H "Content-Type: text/xml" -d "@tests/payload_invalid.xml"
```

**Expected Response:**
```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>SOAP-ENV:Client</faultcode>
      <faultstring>Invalid meter format</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>
```

---

## 📂 Project Structure

```
my-soap-service/
├── app/
│   └── main.py            # FastAPI app with SOAP/XML endpoint
├── tests/
│   ├── payload_success.xml
│   ├── payload_fault_91.xml
│   ├── payload_fault_92.xml
│   └── payload_invalid.xml
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Prince1989/meter-confirmation-service.git
   cd my-soap-service
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Test with curl (use `curl.exe` on Windows PowerShell).

---

## 🌐 Alternative Testing

You can also use:
- **Postman** (send raw XML in body)
- **Swagger UI** at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---
## 🚀 One-Click Deploy

### Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Prince1989/meter-confirmation-service)

# Meter Confirmation Service

Deployed on Render:  
👉 **https://meter-confirmation-service.onrender.com/**

---

## Endpoints

- `/` → Health check & service info  
- `/confirm-meter/{meter_id}` → Confirm a meter by ID  
  - Example: [https://meter-confirmation-service.onrender.com/confirm-meter/12345](https://meter-confirmation-service.onrender.com/confirm-meter/12345)
- `/docs` → Interactive Swagger UI (test endpoints directly in the browser)

---

## How to Test

1. Open the base URL:  
   [https://meter-confirmation-service.onrender.com/](https://meter-confirmation-service.onrender.com/)  
   You should see service info.

2. Try a confirmation:  
   [https://meter-confirmation-service.onrender.com/confirm-meter/12345](https://meter-confirmation-service.onrender.com/confirm-meter/12345)  
   → Returns `{"meter_id":"12345","confirmed":true}`

3. Explore all endpoints via Swagger UI:  
   [https://meter-confirmation-service.onrender.com/docs](https://meter-confirmation-service.onrender.com/docs)


✅ This README includes everything required to **run and test** the project immediately.
