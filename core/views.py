from django.shortcuts import render, redirect
import razorpay
import datetime
import time

# Create your views here.
def index(request):
    return render(request, "main.html")        

def payment(request,id):
        client = razorpay.Client(auth=("rzp_test_FBbs2mmdX6xLBz", "VhImbxk2A6RhGttMJG4q9WuQ"))
        # amount = 199
        # payment = client.order.create({'amount': amount*100,
        #                                'currency': 'INR', 
        #                                'payment_capture': '1'})
        # print('helo')
        # print(payment['id'])
        # print(payment['amount'])
        # return render(request, 'main.html', {'payment':payment})
        # Create a subscription
        date_time = datetime.datetime(2023, 11, 12, 21, 20)
        start_at = time.mktime(date_time.timetuple())

        subscription_params = {
            "plan_id": id,  # Replace with the actual plan ID
            "total_count": 12,          # Number of payments to be made
            "customer_notify": 1,
            "customer_id": "cust_Mn1TOKEsBKeMe5",  # Replace with the actual customer ID
            "start_at": start_at  # Start date (timestamp), replace with the desired start date
        }

        subscription = client.subscription.create(data=subscription_params)
        subscription_id = subscription["id"]

        subscriptionData = {
                'id': subscription_id
        }

        # authentication_link = client.subscription.authenticate(subscription_id)
        # print(authentication_link)
        return render(request, 'payment.html', {'subscriptionData':subscriptionData})

def success(request):
      
    return render(request, "success.html")
