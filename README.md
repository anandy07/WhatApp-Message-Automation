
# 📩 WhatsApp Message Automation with Python & Twilio

Automate sending WhatsApp messages using **Python** and **Twilio API**. This script allows users to schedule messages to be sent at a specific time without manual intervention.

---

## 🚀 Features
✅ **Automated WhatsApp Messaging** – No manual intervention needed!  
✅ **Message Scheduling** – Send messages at a specific date & time.  
✅ **User Input Driven** – Enter recipient number, message, and schedule.  
✅ **Twilio API Integration** – Uses Twilio’s WhatsApp Sandbox.  
✅ **Error Handling** – Prevents sending messages for past dates.  

---

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/whatsapp-message-automation.git
cd whatsapp-message-automation
```

### 2️⃣ **Install Dependencies**
Make sure you have Python installed, then run:
```bash
pip install twilio
```

### 3️⃣ **Set Up Twilio API**
- Sign up at [Twilio](https://www.twilio.com/)
- Get your **Account SID** and **Auth Token** from the Twilio Console
- Activate the **Twilio WhatsApp Sandbox** by sending "join <sandbox-name>" to Twilio’s WhatsApp number

### 4️⃣ **Configure Twilio Credentials**
Edit the script and replace these values with your Twilio credentials:
```python
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
client = Client(account_sid, auth_token)
```

---

## 📜 How It Works
1. **User inputs recipient number, message, and schedule.**
2. **Script calculates delay** (if time is in the future).
3. **Python waits until scheduled time** using `time.sleep()`.
4. **Message is sent automatically** via Twilio API.
5. **Success confirmation** is displayed.

---

## 📌 Usage
Run the script using:
```bash
python main.py
```

### Example Input:
```
Enter the recipient name = John
Enter the recipient WhatsApp number with country code (e.g +1234) = +1234567890
Enter the message you want to send to John: Hello, this is a test message!
Enter the date to send the message (YYYY-MM-DD): 2025-02-21
Enter the time to send the message (HH:MM in 24-hour format): 14:30
```

### Example Output:
```
Message scheduled to be sent to John at 2025-02-21 14:30:00.
Message sent successfully! Message SID: SMxxxxxxxxxxxxxxxxxxxx
```

---

## ⚠️ Troubleshooting
### **Common Errors & Fixes**
1. **Twilio WhatsApp Sandbox not activated?**  
   - Ensure you’ve sent the activation message from your phone.
2. **Invalid phone number format?**  
   - Use `+` followed by country code and number (e.g., `+1234567890`).
3. **Message not sent?**  
   - Check Twilio logs for error details.
4. **Scheduled time is in the past?**  
   - The script will warn and ask for a future time.

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 👨‍💻 Author
Developed by Anand Yadav. Contributions are welcome! 😊

---

## ⭐ Contribute & Support
If you like this project, **give it a star ⭐** on GitHub! Pull requests & suggestions are welcome.

