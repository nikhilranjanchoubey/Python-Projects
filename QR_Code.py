# --------------------- Option :- 1 --------------------------------------
import qrcode

# Taking UPI ID as a input
upi_id = input("Enter your UPI ID = ")

# upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAG

# UPI Payment URL Format
# upi://pay?
# pa = Payee Address (UPI ID of receiver)
# pn = Payee Name
# am = Amount to be paid
# cu = Currency (usually INR)
# tn = Transaction Note / Message

# Example:
# upi://pay?pa=nikhil@upi&pn=Nikhil&am=500&cu=INR&tn=PaymentForCourse

# Defining the payment URL based on the UPI ID and the payment app
# You can modify these URLs based on the payment apps you want to support

# f'' is called an f-string
# It allows Python to insert variables inside strings
# Example: name = "Nikhil"
# print(f"Hello {name}")
# Output = Hello Nikhil

# URL Parameters:
# pa  = Payee Address (Receiver's UPI ID)
# pn  = Payee Name
# mc  = Merchant Code
# %20 = Space in URL

# PhonePe payment URL
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Paytm payment URL
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Google Pay payment URL
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR Code to image file (Optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (you may need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()


# --------------------- Option :- 2 -----------------------------------------
import qrcode

# Taking UPI ID as input
upi_id = input("Enter your UPI ID = ")

# Taking additional payment details
name = input("Enter Receiver Name = ")
amount = input("Enter Amount = ")
note = input("Enter Payment Note = ")

# ---------------------------------------------------
# UPI Payment URL Format
#
# upi://pay?
# pa = Payee Address (UPI ID)
# pn = Payee Name
# am = Amount
# cu = Currency
# tn = Transaction Note
#
# Example:
# upi://pay?pa=nikhil@upi&pn=Nikhil&am=500&cu=INR&tn=CourseFee
# ---------------------------------------------------

# f-string allows variables inside strings
# Example:
# name = "Nikhil"
# print(f"Hello {name}")

# Creating UPI Payment URL
upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn={note}"

# Generate QR Code
qr = qrcode.make(upi_url)

# Save QR Code Image
qr.save("upi_payment_qr.png")

# Show QR Code
qr.show()

print("QR Code Generated Successfully!")