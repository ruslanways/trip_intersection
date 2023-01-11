function validateForm() {
  const dates = document.querySelectorAll(".form-control");
  if (
    Date.parse(dates[1].value) < Date.parse(dates[0].value) ||
    Date.parse(dates[3].value) < Date.parse(dates[2].value)
  ) {
    alert("Departure date must be later than arrival date!\nPlease correct.");
    return false;
  }
}
