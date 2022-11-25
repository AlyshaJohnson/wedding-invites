// --------------------------------- countdown clock

const weddingDate = document.getElementById("wedding-date").textContent;
const weddingTime = document.getElementById("wedding-time").textContent;

// Set the date we're counting down to
var countDownDate = new Date(weddingDate).getTime(weddingTime);

// Update the count down every 1 second
function makeTimer() {
  // Get today's date and time
  var now = new Date().getTime();
  // Find the distance between now and the count down date
  var difference = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(difference / (1000 * 60 * 60 * 24));
  var hours = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((difference % (1000 * 60)) / 1000);

  // Display the result in the element with id="demo"
  document.getElementById("countdown").innerHTML = days + "d " + hours + "h " +
    minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text
  if (difference < 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "EXPIRED";
  }
};

setInterval(makeTimer, 1000);

// --------------------------------- geocoding & map

let map, latitude, longitude;
let markers = [];
let venue1Button = document.getElementById("venue1-button");
let venue2Button = document.getElementById("venue2-button");
let activeButton = document.getElementsByClassName("active");
let venue1Lat = document.getElementById("venue1_lat").textContent;
let venue1Lon = document.getElementById("venue1_lon").textContent;
let venue2Lat = document.getElementById("venue2_lat").textContent;
let venue2Lon = document.getElementById("venue2_lon").textContent;

function initMap() {
  initEventListeners();
  getLocation();
  map = new google.maps.Map(document.getElementById("map"), {
    center: mapLocation,
    zoom: 9,
  });
  addMarkers()
}

function initEventListeners() {
  venue1Button.addEventListener('click', makeActive);
  venue2Button.addEventListener('click', makeActive);
}

function makeActive(event) {
  if (event.target == venue1Button) {
    venue2Button.classList.remove('active');
    event.target.classList.add('active');
    activeButton[0] = venue1Button;
  } else if ((event.target == venue2Button)) {
    venue1Button.classList.remove('active');
    event.target.classList.add('active');
    activeButton[0] = venue2Button;
  }
  initMap();
}

function getLocation() {
  if (activeButton[0] == venue1Button) {
    latitude = Number(venue1Lat)
    longitude = Number(venue1Lon)
  } else if (activeButton[0] == venue2Button) {
    latitude = Number(venue2Lat)
    longitude = Number(venue2Lon)
  }
  mapLocation = { lat: latitude, lng: longitude }
}

function removeMarkers() {
  if (markers.length >= 1) {
    markers.setMap(null)
  }
}

function addMarkers() {
  markers = new google.maps.Marker({position: mapLocation});
  markers.setMap(map);
}
