function validateForm() {
  const dates = document.querySelectorAll(".form-control");
  if (
    dates[1].valueAsNumber < dates[0].valueAsNumber ||
    dates[3].valueAsNumber < dates[2].valueAsNumber
  ) {
    alert("Departure date must be later than arrival date!\nPlease correct.");
    return false;
  }
}
