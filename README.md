# 6-8-Connecting-with-the-WhatsApp-API
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21932947)

## Let's go back to ***Monitoring for Events***
If we are printing on the terminal many times each time we press our button, we need to fix that first before anything else. This will enable us to avoid making unnecessary API calls.

When calling APIs in your programs, avoid making excessive API calls. This can cause multiple problems, including:
- Confusing people who use the system - why did we send 10 notifications instead of 1?
- Costing extra money - we are paying 10 times as much money if we send 10 API calls when we only needed 1.
- The API might reject requests to call it if we call it more than is necessary. This is called rate limiting.

Step 1:
- Copy the app.py program from *Monitoring for Events*
- Paste it into app.py in this Codespace
- Change the code so it only prints one time every time the button is pressed (unless it already is doing this)
- Commit and sync your code to GitHub
- Clone the code in the Raspberry Pi
- Run the code on the Raspberry Pi and push the button to be sure it is working correctly

Step 2:
- Write a program called testwhatsapp.py
- Create a global string variable called sector_name containing your sector name
- Write a function int the program called send_alert()
- Import the Requests library
- Inside the send_alert() function, call the WhatsApp API using the Requests library
- Test the send_alert() function by calling it in the testwhatsapp.py program
- Be sure you get the alert

Step 3:
- Modify app.py, and paste the sector_name variable and the send_alert() function into the app.py 
- When a button is pressed, in addition to printing a message, call the send_alert() function
- Commit and sync the code to GitHub

Step 4:
- Go back to the Raspberry Pi SSH session and pull the latest code
- Run the program again
- Push the button
- You should receive a message
- Congratulations! You have a working prototype!

