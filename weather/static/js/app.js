if (halfmoon.readCookie("darkModeOn") == "yes") {
  halfmoon.toggleDarkMode();
}

const searchForm = document.querySelector("#search-form");
const searchBtn = document.querySelector("#search-btn");
const searchInput = document.querySelector("#city");
const changeLocationBtn = document.querySelector("#change-location");
const userLocationBtn = document.querySelector("#user-location-btn");

searchBtn.addEventListener("click", () => {
  if (searchInput.value == "") {
    searchInput.parentElement.classList.add("search-empty");
  } else {
    searchForm.submit();
  }
});
searchInput.addEventListener("change", () => {
  searchInput.parentElement.classList.remove("search-empty");
});

// get the user position on click
userLocationBtn.addEventListener("click", () => {
  navigator.permissions.query({ name: "geolocation" }).then(function (result) {
    if (result.state == "granted" || result.state == "prompt") {
      getLocation();
    } else if (result.state == "denied") {
      userLocationBtn.setAttribute("data-toggle", "tooltip");
      userLocationBtn.setAttribute("data-placement", "bottom");
      userLocationBtn.setAttribute(
        "data-title",
        "You need to give us Location Permission"
      );
    }
  });
});

// change focus to the input filed on click
if (changeLocationBtn) {
  changeLocationBtn.addEventListener("click", () => {
    searchInput.focus();
  });
}

// get the user position
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    console.log("Geolocation is not supported by this browser.");
  }
  function showPosition(position) {
    let lat = position.coords.latitude;
    let long = position.coords.longitude;
    searchForm.lat.value = lat;
    searchForm.long.value = long;
    searchForm.submit();
  }
}
