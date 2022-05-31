// Initialize Firebase
//The project has been deleted in firebase
//fill in your own config info 
var config = {
  apiKey: "AIzaSyAsp0rmvoqMTenZ9TpgKu8qcerzWDCTJyE",
  authDomain: "dieukhiendenbangnodemcu.firebaseapp.com",
  databaseURL: "https://dieukhiendenbangnodemcu-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "dieukhiendenbangnodemcu",
  storageBucket: "dieukhiendenbangnodemcu.appspot.com",
  messagingSenderId: "433988844880",
  appId: "1:433988844880:web:f90ed9511c6d308e290055",
  measurementId: "G-HCS8JL513Q"
};
firebase.initializeApp(config);

$(document).ready(function(){
  var database = firebase.database();
  var S1;

  database.ref().on("value", function(snap){
    S1 = snap.val().S1;
    if(S1 == 1){
      $(".lightStatus").text("The light is on");
    } else {
      $(".lightStatus").text("The light is off");
    }
  });

  $(".lightButton").click(function(){
    var firebaseRef = firebase.database().ref().child("S1");

    if(S1 == 1){
      firebaseRef.set(2);
      S1 = 0;
    } else {
      firebaseRef.set(1);
      S1 = 1;
    }
  });
});
