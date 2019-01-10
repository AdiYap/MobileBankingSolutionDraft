# MobileBankingSolutionDraft

This app is meant to simulate a banking app. The key features are the realtime updating of the user's bank balance,
and the ability to pay bills and perform bank transfers.

Each time a user pays a bill or does a transfer, the amount paid is accurately reflected in the bank balance. The
action itself is recorded with the timestamp, amount paid and the type of transaction (Bills and Transfer are the
only two categories as of yet)

The backend database used in this app is hosted on Firebase. The implementation code is as follows:

--------------------------------------------------------------------------------------------------------------------
<script src="https://www.gstatic.com/firebasejs/5.7.2/firebase.js"></script>
<script>
  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyAfFE2Kr7u_vyq_oSSrb_9gdwJ_xiFXpLE",
    authDomain: "design-thinking-assignment.firebaseapp.com",
    databaseURL: "https://design-thinking-assignment.firebaseio.com",
    projectId: "design-thinking-assignment",
    storageBucket: "design-thinking-assignment.appspot.com",
    messagingSenderId: "758596598031"
  };
  firebase.initializeApp(config);
</script>

--------------------------------------------------------------------------------------------------------------------

The name of the project on Firebase is: Design thinking assignment. The home page of the app is "index.html". You 
can return to it at anytime by clicking on "EZ-eBanking" at the top left of the screen, or on "Main Menu", if you 
are on one of the other two pages.

To test the app, you may perform a bill payment and/or bank transfer. To do this, click on either "Pay a Bill", or
"Arrange a Bank transfer".

----------------------------------------------------------
Pay a Bill (bills.html)
----------------------------------------------------------

This page has just one text field; this is where you enter the amount you wish to pay. The user's bank balance is
conveniently displayed just above it, marked "Savings account:". To test that the code is working, simply input an
amount in the textfield, then click "Confirm". You should see the amount deducted from the bank balance accordingly.


----------------------------------------------------------
Arrange a Bank Transfer (transfer.html)
----------------------------------------------------------

This page has two textfields, one for the "Recipient Account No", and one for the "Amount to Pay". You may ignore
the one marked "Recipient Account No" for now; it is non-functional.

Similarly to the Pay a Bill page, simply enter an amount into the "Amount to Pay" textfield, then click "Confirm".
You should see the amount deducted from the bank balance.



----------------------------------------------------------
Transaction history (in home page; home.html)
----------------------------------------------------------

The table displaying the transaction history is located at the bottom of the home page. All actions performed with
this app should accurately reflect there.

